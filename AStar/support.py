import numpy as np


class Neighbor(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.cost = 0
        self.node = 0


class Closed(object):
    def __init__(self):
        self.count = 0
        self.nodes = []


class TopNode(object):
    def __init__(self):
        self.ind = 0
        self.dir = 0
        self.node = 0
        self.p_node = 0
        self.g_cost = 0
        self.f_cost = 0
        self.visited = False


class Open(object):
    def __init__(self, top_node):
        self.list = [top_node]
        self.count = 1
        self.nodes = [top_node.node]


class Sol(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dirs = 0
        self.nodes = 0
        self.proc_time = 0