class Point:
    def __init__(self, x, y, class_id=0):
        self.x = float(x)
        self.y = float(y)
        self.class_id = int(class_id)

    def get(self, i):
        if i == 0:
            return self.x
        else:
            return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "[{} {}] - {}".format(self.x, self.y, self.class_id)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def mul_scalar(self, val):
        return Point(self.x * val, self.y * val)