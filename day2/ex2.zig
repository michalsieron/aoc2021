const std = @import("std");

const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

pub fn main() !void {
    var horizontal: usize = 0;
    var depth: usize = 0;
    var aim: usize = 0;

    var lines_it = std.mem.tokenize(u8, data, "\n");

    while (lines_it.next()) |line| {
        var values_it = std.mem.tokenize(u8, line, " ");

        const instr_str = values_it.next() orelse return error.@"No instruction in line";
        const value_str = values_it.next() orelse return error.@"No value in line";

        const value = try std.fmt.parseUnsigned(usize, value_str, 10);

        switch (instr_str[0]) {
            'f' => {
                // forward
                horizontal += value;
                depth += aim * value;
            },
            'u' => aim -= value, // up
            'd' => aim += value, //down
            else => return error.@"Invalid instruction",
        }
    }

    try stdout.print("answer: {}\n", .{horizontal * depth});
}
