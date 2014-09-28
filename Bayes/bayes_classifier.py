class BayesClassifier:
    # 0 - spam, 1 - not spam

    def __init__(self, train_data):
        self.train_data = train_data
        words_cnt = dict()
        class_size = [0., 0.]
        for letter in train_data:
            class_size[letter.class_id] += 1
            for word in letter.subject + letter.body:
                if not word in words_cnt:
                    words_cnt[word] = [0, 0]
                words_cnt[word][letter.class_id] += 1
        self.word_prob = dict()
        for key, value in words_cnt.items():
            self.word_prob[key] = [value[i] / (value[0] + value[1]) for i in range(2)]
        self.prob_classes = [class_size[i] / len(train_data) for i in range(2)]

    def get_class(self, test_letter):
        cur_prob_classes = [self.prob_classes[0], self.prob_classes[1]]
        for word in test_letter.subject + test_letter.body:
            for i in range(2):
                if word in self.word_prob:
                    cur_prob_classes[i] *= self.word_prob[word][i]

        return 0 if cur_prob_classes[0] > cur_prob_classes[1] else 1
