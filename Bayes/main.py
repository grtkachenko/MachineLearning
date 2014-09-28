import os
from Bayes.msg import Message

test_dir = "./test"
data = []
for data_part in os.listdir(test_dir):
    for root, _, files in os.walk(os.path.join(test_dir, data_part), topdown=True):
        msgs = []
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                lines = [line for line in f.readlines()]
                subject = [int(number) for number in lines[0].split()[1:]]
                body = [int(number) for number in lines[2].split()]
                data.append(Message(subject, body, "spmsg" in file))
for test in data:
    print(test)