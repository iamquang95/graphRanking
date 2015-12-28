#!/usr/bin/python
# -*- coding: utf8 -*-

import csv
import matplotlib.pyplot as plt


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


def show_line_chart_score():
    score = []
    for record in record_list:
        score.append(sum(record.score[0:6]))
    score = sorted(score)
    print score

    fig, ax = plt.subplots()
    ax.set_title('Total 2 days')

    xs = range(0, len(score))
    ys = score
    ax.plot(xs, ys)

    plt.show()


def show_bar_chart_score_distribution():
    thresholds = [0, 10, 17, 23, 30, 40]
    score = []
    for record in record_list:
        score.append(sum(record.score[0:6]))
    labels = ['< 10', '10-17', '17-23', '23-30', '> 30']
    explode = [0, 0, 0, 0, 0]
    fracs = [0, 0, 0, 0, 0]
    for x in score:
        for i in xrange(0, len(fracs)):
            if (thresholds[i] <= x) and (x <= thresholds[i + 1]):
                fracs[i] += 1
                break
    colors = ['#756565', '#CCC2C2', '#965A38', '#A8A8A8', '#C98910']
    plt.pie(fracs, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=90)
    plt.show()

read_data(problem_name, record_list)
# show_line_chart_score()
show_bar_chart_score_distribution()
