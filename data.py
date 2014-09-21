class Data:
    def __init__(self, x, y, class_id):
        self.x = x
        self.y = y
        self.class_id = class_id

    def __str__(self):
        return "[{} {}] - {}".format(self.x, self.y, self.class_id)