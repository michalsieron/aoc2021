const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");
const Polymer = std.AutoHashMap([2]u8, usize);
const STEPS = 10;

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var letter_count = [_]usize{0} ** 26;

    var data_it = std.mem.tokenize(u8, data, "\n");
    const template = data_it.next().?;

    for (template) |l| letter_count[l - 'A'] += 1;

    var rules = std.AutoHashMap([2]u8, u8).init(allocator);
    defer rules.deinit();

    var polymer = Polymer.init(allocator);
    defer polymer.deinit();

    for (template[0 .. template.len - 1]) |_, i| {
        const key = template[i..][0..2].*;
        _ = try polymer.getOrPutValue(key, 0);
        polymer.getPtr(key).?.* += 1;
    }

    var new_polymer = Polymer.init(allocator);
    defer new_polymer.deinit();

    while (data_it.next()) |rule| {
        const pair = rule[0..2].*;
        const insert = rule[rule.len - 1];
        try rules.put(pair, insert);
    }

    var step: usize = 0;
    while (step < STEPS) : (step += 1) {
        new_polymer.clearRetainingCapacity();
        var polymer_it = polymer.iterator();
        while (polymer_it.next()) |ab_count| {
            const ab = ab_count.key_ptr.*;
            const c = rules.get(ab).?;
            const ac = [2]u8{ ab[0], c };
            const cb = [2]u8{ c, ab[1] };
            const count = ab_count.value_ptr.*;

            _ = try new_polymer.getOrPutValue(ac, 0);
            new_polymer.getPtr(ac).?.* += count;

            _ = try new_polymer.getOrPutValue(cb, 0);
            new_polymer.getPtr(cb).?.* += count;

            letter_count[c - 'A'] += count;
        }
        std.mem.swap(Polymer, &polymer, &new_polymer);
    }

    std.sort.sort(usize, &letter_count, {}, comptime std.sort.asc(usize));
    const most = letter_count[letter_count.len - 1];
    const least = for (letter_count) |c| {
        if (c > 0) break c;
    } else unreachable;

    try stdout.print("answer: {}\n", .{most - least});
}
