from collections import defaultdict

# 1
def best_sender(messages, senders):
    res = defaultdict(int)
    for i in range(len(messages)):
        res[senders[i]] += len(messages[i].split())
    return max(res, key=lambda x: (res[x], x))

# 2
def best_sender(messages, senders):
    counts = defaultdict(int)
    for sender, message in zip(senders, messages):
        counts[sender] += len(message.split())
    return max(counts, key=lambda sender: (counts[sender], sender))


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
print(best_sender(messages, senders))

messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
senders = ['Alice', 'userTwo', 'userThree', 'Alice']
print(best_sender(messages, senders))

messages = ['thanks', 'Stepik is useful for', 'thanks', 'np ur welcome', 'practice']
senders = ['Bob', 'Charlie', 'Bob', 'Bob', 'Charlie']
print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']
print(best_sender(messages, senders))
