const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

pub fn main() !void {
    var crabs = std.ArrayList(usize).init(std.heap.page_allocator);
    defer crabs.deinit();

    var sum: usize = 0;
    var data_it = std.mem.tokenize(u8, data, ",\n");
    while (data_it.next()) |token| {
        const crab = try std.fmt.parseUnsigned(usize, token, 10);
        try crabs.append(crab);
        sum += crab;
    }

    const mean = try std.math.divCeil(usize, sum, crabs.items.len);
    var answers = [_]usize{ 0, 0, 0 };

    for (crabs.items) |crab| {
        answers[0] += cost(crab, mean - 1);
        answers[1] += cost(crab, mean);
        answers[2] += cost(crab, mean + 1);
    }
    const answer = std.mem.min(usize, &answers);
    try stdout.print("answer: {}\n", .{answer});
}

fn cost(from: usize, to: usize) usize {
    const diff = if (from > to) from - to else to - from;
    return diff * (diff + 1) / 2;
}
