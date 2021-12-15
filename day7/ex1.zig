const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");

pub fn main() !void {
    var crabs = std.ArrayList(usize).init(std.heap.page_allocator);
    defer crabs.deinit();

    var data_it = std.mem.tokenize(u8, data, ",\n");
    while (data_it.next()) |token| {
        const crab = try std.fmt.parseUnsigned(usize, token, 10);
        try crabs.append(crab);
    }

    std.sort.sort(usize, crabs.items, {}, comptime std.sort.asc(usize));

    const median = crabs.items[crabs.items.len / 2];
    var answer: usize = 0;
    for (crabs.items) |crab| {
        const diff = @intCast(i65, crab) - @intCast(i65, median);
        answer += std.math.lossyCast(usize, try std.math.absInt(diff));
    }
    try stdout.print("answer: {}\n", .{answer});
}
