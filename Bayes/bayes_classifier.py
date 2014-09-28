class BayesClassifier:
    # 0 - spam, 1 - not spam

    def __init__(self, train_data):
        self.train_data = train_data
        words_cnt = dict()
        spam_size = 0
        for letter in train_data:
            if letter.spam:
                spam_size += 1
            for word in letter.subject + letter.body:
                if not word in words_cnt:
                    words_cnt[word] = [0, 0]
                words_cnt[word][0 if letter.spam else 1] += 1
        self.spam_word_prob = dict()
        for key, value in words_cnt.iteritems():
            self.spam_word_prob[key] = [value[0] / (value[0] + value[1], value[1] / (value[0] + value[1]))]
        self.prob_classes = [spam_size / len(train_data), (len(train_data) - spam_size) / len(train_data)]

    def get_class(self, test_letter):
        cur_prob_classes = {0: self.prob_classes[0], 1: self.prob_classes[1]}
        for word in test_letter.subject + test_letter.body:
            for i in range(0, 2):
                cur_prob_classes[i] *= self.spam_word_prob[word][i]

        return max(cur_prob_classes, key=cur_prob_classes.get)[0]
