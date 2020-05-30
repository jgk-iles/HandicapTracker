import tkinter as tk
from tkinter import simpledialog
import pickle


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.players = []

    def add_player(self, name, sex, handicap):
        self.players.append(Player(name, sex, handicap))


class Player:
    def __init__(self, name, sex, handicap=None):
        self.name = name
        self.sex = sex
        self.handicap = handicap
        self.rounds = []
        self.rounds_played = len(self.rounds)
        # self.courses_played = []

    def initial_handicap(self, course_name1, date1, gross1, ss1,
                         course_name2, date2, gross2, ss2,
                         course_name3, date3,  gross3, ss3):
        # Calculates an initial handicap from three round by taking the minimum difference between score and ss out of
        # the three
        self.handicap = min(gross1-ss1, gross2-ss2, gross3-ss3)
        self.rounds.append(Round(course_name1, date1, gross1, ss1))
        self.rounds.append(Round(course_name2, date2, gross2, ss2))
        self.rounds.append(Round(course_name3, date3, gross3, ss3))

    def recalculate_handicap(self):
        pass

    def add_round(self, course_name, date, gross_score, ss):
        self.rounds.append(Round(course_name, date, gross_score, ss))


class Round:
    def __init__(self, course, date, gross_score, ss):
        self.course = course
        self.date = date


class Course:
    def __init__(self, name, par, ss, pars, indexes):
        self.name = name
        self.par = par
        self.ss = ss
        self.holes = []
        for hole in range(18):
            self.holes.append(Hole(pars(hole), indexes(hole)))


class Hole:
    def __init__(self, par, index):
        self.par = par
        self.index = index

