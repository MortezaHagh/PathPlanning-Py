import time
import numpy as np
from AStar.support import Open, Sol
from AStar.support import Closed, TopNode
from common.angle_diff import angle_diff
from common.cal_distance import cal_distance


class AStar:
    def __init__(self, model):

        # settings
        self.dir_coeff = 0.0
        self.from_start = True # True False

        # statistics
        self.n_closed = 0
        self.n_opened = 0
        self.n_expanded = 0
        self.n_reopened = 0
        self.n_final_open = 0

        # initialize
        if self.from_start:
            self.start = model.start
            self.goal = model.goal
        else:
            self.goal = model.start
            self.start = model.goal
        self.model = model
        self.closed = Closed()
        top_node = self.create_top_node()
        self.open = Open(top_node)
        self.closed.count += 1
        self.closed.nodes.append(top_node.node)
        self.top_node = top_node

        # start process time
        self.end_time = 0
        start_time = time.process_time()

        # astar
        self.astar()

        # end process time
        self.sol.proc_time = self.end_time - start_time

    # ------------------------------------------------------------

    def astar(self):
        while self.top_node.node != self.goal.node:

            # finding neighbors (successors)
            feas_neighbors = self.expand()

            # update or extend Open list with the successor nodes
            self.update_open(feas_neighbors)

            # select new Top Node
            self.select_top_node()

        # optimal paths
        self.path_nodes = self.optimal_path()

        # create sol
        self.end_time = time.process_time()
        self.create_sol()
        self.n_closed = len(self.closed.nodes)
        self.n_final_open = len(self.open.list)

    # ------------------------------------------------------------

    def expand(self):
        feas_neighbors = []
        neghbors = self.model.neighbors[self.top_node.node]
        for neigh in neghbors:
            if not (neigh.node in self.closed.nodes):
                self.n_expanded += 1
                feas_neighb = TopNode()
                feas_neighb.dir = neigh.dir
                feas_neighb.node = neigh.node
                feas_neighb.p_node = self.top_node.node
                feas_neighb.dir_cost = int(not (self.top_node.dir - neigh.dir) == 0)*self.dir_coeff
                feas_neighb.g_cost = self.top_node.g_cost + neigh.cost + feas_neighb.dir_cost
                h_cost = cal_distance(self.goal.x, self.goal.y, neigh.x, neigh.y, self.model.dist_type)
                feas_neighb.f_cost = feas_neighb.g_cost + h_cost*1
                feas_neighbors.append(feas_neighb)
        return feas_neighbors

    def update_open(self, neighbors):
        if neighbors == []:
            return

        for neigh in neighbors:
            if neigh.node in self.open.nodes:
                ind = self.open.nodes.index(neigh.node)
                if neigh.f_cost < self.open.list[ind].f_cost:
                    # update open
                    self.n_opened += 1
                    self.n_reopened += 1
                    self.open.list[ind] = neigh
                    self.open.list[ind].ind = ind
            else:
                # expand open
                self.open.count += 1
                self.n_opened += 1
                self.open.list.append(neigh)
                self.open.nodes.append(neigh.node)
                self.open.list[-1].ind = self.open.count-1

    def select_top_node(self):
        inds = [op.ind for op in self.open.list if op.visited == False]
        if len(inds) < 0:
            print(" error: Astar failed to find a path, impossible!")
            raise

        f_costs = [self.open.list[ind].f_cost for ind in inds]
        if self.model.expand_method == 'random':
            min_ind = np.argmin(f_costs)
        elif self.model.expand_method == 'heading':
            dtheta = [abs(angle_diff(self.top_node.dir, self.open.list[ind].dir)) for ind in inds]
            costs = [dtheta, f_costs]
            sorted_inds = np.lexsort(costs)
            min_ind = sorted_inds[0]
        top_ind = inds[min_ind]
        self.open.list[top_ind].visited = True
        self.top_node = self.open.list[top_ind]
        self.closed.count += 1
        self.closed.nodes.append(self.top_node.node)

    def optimal_path(self):
        path_nodes = [self.goal.node]
        parent_node = self.top_node.p_node
        parent_ind = self.open.nodes.index(parent_node)
        while parent_node != self.start.node:
            path_nodes.append(parent_node)
            parent_node = self.open.list[parent_ind].p_node
            parent_ind = self.open.nodes.index(parent_node)

        path_nodes.append(self.start.node)
        if self.from_start:
            path_nodes.reverse()
        return path_nodes

    # ------------------------------------------------------------

    def create_top_node(self):
        top_node = TopNode()
        top_node.ind = 0
        top_node.visited = True
        top_node.dir = self.start.dir
        top_node.node = self.start.node
        top_node.p_node = self.start.node
        h_cost = cal_distance(self.start.x, self.start.y, self.goal.x, self.goal.y, self.model.dist_type)
        top_node.g_cost = 0
        top_node.f_cost = h_cost
        return top_node

    def create_sol(self):
        sol = Sol()
        sol.nodes = self.path_nodes
        sol.x = [self.model.nodes.x[i] for i in self.path_nodes]
        sol.y = [self.model.nodes.y[i] for i in self.path_nodes]
        sol.dirs = self.node_to_dir(self.path_nodes)
        self.sol = sol

    def node_to_dir(self, nodes):
        dirs = []
        for i in range(1, len(nodes)):
            x1 = self.model.nodes.x[nodes[i-1]]
            y1 = self.model.nodes.y[nodes[i-1]]
            x2 = self.model.nodes.x[nodes[i]]
            y2 = self.model.nodes.y[nodes[i]]
            dy = y2-y1
            dx = x2-x1
            theta = np.arctan2(dy, dx)
            theta = round(theta, 3)
            dirs.append(theta)

        dirs.append(dirs[-1])
        return dirs
