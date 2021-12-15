const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

pub fn main() !void {
    var count: usize = 0;
    var lines: usize = 0;

    var data_it = std.mem.tokenize(u8, data, " \n");
    while (data_it.next()) |token| {
        switch (token.len) {
            1 => lines += 1, // pipe character
            2, 3, 4, 7 => count += 1, // 1, 7, 4, 8
            else => continue,
        }
    }

    const answer = count - 4 * lines;
    try stdout.print("answer: {}\n", .{answer});
}
