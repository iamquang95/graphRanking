import csv


class Record:

    num_record = 0

    def __init__(self, rank, account, score):
        self.rank = rank
        self.account = account
        string_score = score
        self.score = []
        for i in xrange(0, len(string_score)):
            self.score.append(float(string_score[i]))
        self.sum = sum(self.score)
        Record.num_record += 1

    def get_rank(self):
        return self.rank

    def get_account(self):
        return self.account

    def get_score(self):
        return self.score


problem_name = []
record_list = []


def read_data(problem_name, record_list):
    with open('VO16.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        cnt = 0
        for row in reader:
            if (cnt == 0):
                problem_name.extend(row[2:-1])
            else:
                record_list.append(Record(row[0], row[1], row[2:-1]))
            cnt += 1

read_data(problem_name, record_list)
# print problem_name
# print (record_list[0].get_rank(), record_list[0].get_account(),
#        record_list[0].get_score())
