class Message:
    def __init__(self, subject, body, class_id):
        self.subject = subject
        self.body = body
        self.class_id = class_id

    def __str__(self):
        res = "spam : " if self.class_id == 0 else "legit : "
        res += "\nSubject : " + str(self.subject) + "\n" + str(self.body) + "\n"
        return res