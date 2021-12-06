const std = @import("std");

const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");
const LINE_LEN = 12;

const LineInt = std.meta.Int(.unsigned, LINE_LEN);

pub fn main() !void {
    var count0 = [_]usize{0} ** LINE_LEN;
    var count1 = [_]usize{0} ** LINE_LEN;

    var data_it = std.mem.tokenize(u8, data, "\n");
    while (data_it.next()) |line| {
        for (line) |d, i| {
            switch (d) {
                '0' => count0[i] += 1,
                '1' => count1[i] += 1,
                else => unreachable,
            }
        }
    }

    var gamma_str = [_]u8{'0'} ** LINE_LEN;
    for (gamma_str) |_, i|
        gamma_str[i] += @boolToInt(count0[i] < count1[i]);

    const gamma = try std.fmt.parseUnsigned(LineInt, &gamma_str, 2);
    const epsilon = ~gamma;

    const answer = @intCast(usize, gamma) * @intCast(usize, epsilon);
    try stdout.print("answer: {}\n", .{answer});
}
