const std = @import("std");
const stdout = std.io.getStdOut().writer();

const data = @embedFile("test_data.txt");
const SIZE = blk: {
    @setEvalBranchQuota(99999);
    break :blk std.mem.count(u8, data, "\n");
};

const Point = struct {
    const Self = @This();

    x: usize,
    y: usize,
    cost: usize = std.math.maxInt(usize),

    pub fn toInt(self: Self) usize {
        return self.y * SIZE + self.x;
    }

    pub fn fromInt(n: usize) Self {
        const y = n / SIZE;
        const x = n % SIZE;
        return Self{ .x = x, .y = y };
    }

    pub fn compare(self: Self, other: Self) std.math.Order {
        return std.math.order(self.cost, other.cost);
    }
};

const destination = Point{ .x = SIZE - 1, .y = SIZE - 1 };

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var cave = blk: {
        var new_cave: [SIZE][SIZE]u8 = undefined;
        var data_it = std.mem.tokenize(u8, data, "\n");
        var y: usize = 0;
        while (data_it.next()) |line| : (y += 1) {
            for (line) |r, x|
                new_cave[y][x] = r - '0';
        }
        break :blk new_cave;
    };

    var pq = std.PriorityQueue(Point, Point.compare).init(allocator);
    defer pq.deinit();

    var dist = std.AutoHashMap(usize, usize).init(allocator);
    defer dist.deinit();

    for (cave) |row, y| {
        for (row) |_, x| {
            const p = Point{ .x = x, .y = y };
            try dist.put(p.toInt(), std.math.maxInt(usize));
        }
    }

    {
        const start = Point{ .x = 0, .y = 0, .cost = 0 };
        try pq.add(start);
        try dist.put(start.toInt(), 0);
    }

    while (pq.removeOrNull()) |u| {
        if (u.y > 0) {
            var up = Point{
                .x = u.x,
                .y = u.y - 1,
                .cost = u.cost +| cave[u.y - 1][u.x],
            };
            if (up.cost < dist.get(up.toInt()).?) {
                try dist.put(up.toInt(), up.cost);
                try pq.add(up);
            }
        }
        if (u.x < SIZE - 1) {
            var right = Point{
                .x = u.x + 1,
                .y = u.y,
                .cost = u.cost +| cave[u.y][u.x + 1],
            };
            if (right.cost < dist.get(right.toInt()).?) {
                try dist.put(right.toInt(), right.cost);
                try pq.add(right);
            }
        }
        if (u.y < SIZE - 1) {
            var down = Point{
                .x = u.x,
                .y = u.y + 1,
                .cost = u.cost +| cave[u.y + 1][u.x],
            };
            if (down.cost < dist.get(down.toInt()).?) {
                try dist.put(down.toInt(), down.cost);
                try pq.add(down);
            }
        }
        if (u.x > 0) {
            var left = Point{
                .x = u.x - 1,
                .y = u.y,
                .cost = u.cost +| cave[u.y][u.x - 1],
            };
            if (left.cost < dist.get(left.toInt()).?) {
                try dist.put(left.toInt(), left.cost);
                try pq.add(left);
            }
        }
    }

    if (dist.get(destination.toInt())) |cost| {
        try stdout.print("answer: {}\n", .{cost});
    } else unreachable;
}
