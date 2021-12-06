const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");
const WINDOW_SIZE = 1;

pub fn main() !void {
    var depths_it = std.mem.tokenize(u8, data, "\n");
    var window = blk: {
        var new_window: [WINDOW_SIZE]usize = undefined;
        for (new_window) |_, i| {
            const depth_str = depths_it.next() orelse return error.@"Not enough values";
            new_window[i] = try std.fmt.parseUnsigned(usize, depth_str, 10);
        }

        break :blk new_window;
    };

    var answer: usize = 0;
    while (depths_it.next()) |depth_str| {
        const depth = try std.fmt.parseUnsigned(usize, depth_str, 10);
        if (depth > window[0])
            answer += 1;

        window[0] = depth;
        std.mem.rotate(usize, &window, 1);
    }
    try stdout.print("answer: {}\n", .{answer});
}
