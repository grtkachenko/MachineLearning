class Message:
    def __init__(self, subject, body, spam):
        self.subject = subject
        self.body = body
        self.spam = spam

    def __str__(self):
        res = "spam : " if self.spam else "legit : "
        res += "\nSubject : " + str(self.subject) + "\n" + str(self.body) + "\n"
        return res