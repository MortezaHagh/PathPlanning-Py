import numpy as np
from common.create_model_base import CreateBaseModel


class CreateLPAStarModel(CreateBaseModel):
    def __init__(self, setting, has_dynamic_obsts=False, use_rnd=False, map_id=1):
        CreateBaseModel.__init__(self, has_dynamic_obsts, use_rnd, map_id=map_id)
        print('Create LPA* Model from Base Model')

        if setting['adj_type'] == '4adj':
            ixy = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            nAdj = 4
        elif setting['adj_type'] == '8adj':
            ixy = [[1, 0], [0, 1], [0, -1], [-1, 0],
                   [1, 1], [-1, -1], [-1, 1], [1, -1]]
            nAdj = 8

        if setting['dist_type'] == 'manhattan':
            edge_len = 2
        elif setting['dist_type'] == 'euclidean':
            edge_len = np.sqrt(2)

        self.adj_type = setting['adj_type']
        self.dist_type = setting['dist_type']
        self.expand_method = setting['expand_method']

        # successors and predecessors
        successors = [np.array([], dtype='int')
                      for i in range(self.nodes.count)]
        succ_cost = [np.array([])
                     for i in range(self.nodes.count)]
        predecessors = [np.array([], dtype='int')
                        for i in range(self.nodes.count)]
        pred_cost = [np.array([])
                     for i in range(self.nodes.count)]

        for inode in range(self.nodes.count):
            if not inode in self.obsts.nodes:
                xnode = self.nodes.x[inode]
                ynode = self.nodes.y[inode]

                for iadj in range(nAdj):
                    ix = ixy[iadj][0]
                    iy = ixy[iadj][1]
                    newx = xnode+ix
                    newy = ynode+iy

                    # check if the Node is within array bound
                    if (self.map.x_min <= newx <= self.map.x_max) and (self.map.y_min <= newy <= self.map.y_max):
                        new_node = inode+ix+iy*(self.map.nx)

                        # check if it is obstacle
                        if not new_node in self.obsts.nodes:
                            successors[inode] = np.append(successors[inode], new_node)
                            predecessors[new_node] = np.append(predecessors[new_node], inode)

                            # edge cost
                            if ix != 0 and iy != 0:
                                cost = edge_len
                            else:
                                cost = 1

                            # new successor
                            succ_cost[inode] = np.append(succ_cost[inode], cost)
                            pred_cost[new_node] = np.append(pred_cost[new_node], cost)

        self.successors = successors
        self.succ_cost = succ_cost
        self.predecessors = predecessors
        self.pred_cost = pred_cost

        self.start_node = self.robot.start_node
        self.G = np.inf*np.ones(self.nodes.count)
        self.RHS = np.inf*np.ones(self.nodes.count)
