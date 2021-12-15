const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

fn decodeDisplay(input: []u8, output: []u8) usize {
    var mapping: [10]u8 = undefined;

    for (input) |pattern| {
        switch (@popCount(u8, pattern)) {
            2 => mapping[1] = pattern,
            3 => mapping[7] = pattern,
            4 => mapping[4] = pattern,
            7 => mapping[8] = pattern,
            else => continue,
        }
    }

    for (input) |pattern| {
        const common_bd = @popCount(u8, pattern & (mapping[4] & ~mapping[1]));
        const common_cf = @popCount(u8, pattern & mapping[1]);

        switch (@popCount(u8, pattern)) {
            5 => {
                if (common_cf == 2) {
                    mapping[3] = pattern;
                } else if (common_bd == 2) {
                    mapping[5] = pattern;
                } else {
                    mapping[2] = pattern;
                }
            },
            6 => {
                if (common_bd == 1) {
                    mapping[0] = pattern;
                } else if (common_cf == 1) {
                    mapping[6] = pattern;
                } else {
                    mapping[9] = pattern;
                }
            },
            else => continue,
        }
    }

    var result: usize = 0;
    for (output) |o| {
        for (mapping) |m, i| {
            if (m == o)
                result = result * 10 + i;
        }
    }
    return result;
}

pub fn main() !void {
    var answer: usize = 0;

    var data_it = std.mem.tokenize(u8, data, "\n");
    while (data_it.next()) |line| {
        var patterns: [14]u8 = undefined;
        var line_it = std.mem.tokenize(u8, line, " |");
        var i: usize = 0;
        while (line_it.next()) |pattern_str| : (i += 1) {
            var pattern: u8 = 0;
            for (pattern_str) |c| {
                const s = @intCast(u3, c - 'a');
                pattern |= @as(u8, 1) << s;
            }
            patterns[i] = pattern;
        }
        answer += decodeDisplay(patterns[0..10], patterns[10..]);
    }

    try stdout.print("answer: {}\n", .{answer});
}
