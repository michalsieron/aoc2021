const std = @import("std");

const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

const DAYS = 18;

pub fn main() !void {
    var fish_count = [_]usize{0} ** 9;

    var data_it = std.mem.tokenize(u8, data, ",\n");
    while (data_it.next()) |fish_str| {
        const fish = try std.fmt.parseUnsigned(u4, fish_str, 10);
        fish_count[fish] += 1;
    }

    var i: usize = 0;
    while (i < DAYS) : (i += 1) {
        std.mem.rotate(usize, &fish_count, 1);
        fish_count[6] += fish_count[8];
    }

    var answer: usize = 0;
    for (fish_count) |count| answer += count;
    try stdout.print("answer: {}\n", .{answer});
}
