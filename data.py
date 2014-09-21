class Data:
    def __init__(self, x, y, class_id):
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