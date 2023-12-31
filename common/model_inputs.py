

class ModelInputs():
    def __init__(self, map_id=1):
        print("Inputs for creating model")

        # map_1 - map_2
        if map_id == 1:
            self.map_1()
        elif map_id == 2:
            self.map_2()
        elif map_id == 3:
            self.map_3()

    def map_1(self):

        # area
        lim = 26
        self.lim = lim
        self.x_min = 0
        self.y_min = 0
        self.x_max = lim
        self.y_max = lim

        # obstacles
        xc1 = [3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9, 11, 11, 11]
        yc1 = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]
        xc2 = xc1*4
        yc2 = yc1 + [y+6 for y in yc1] + \
            [y+11 for y in yc1] + [y+16 for y in yc1]
        xc3 = [x+12 for x in xc2]
        yc3 = yc2
        self.x_obst = xc2 + xc3
        self.y_obst = yc2 + yc3

        # robots
        self.robot_count = 4
        self.heading = 0
        self.xs = 1
        self.ys = 1
        self.xt = 7
        self.yt = 7


    def map_2(self):

        # area
        lim = 32
        self.lim = lim
        self.x_min = 1
        self.y_min = 1
        self.x_max = lim
        self.y_max = lim

        # data
        oo = [[2, 4, 5, 8, 12, 20, 21, 29, 30, 32], [3, 6, 7, 8, 10, 12, 27, 29, 32],
              [4, 9, 14, 15, 19, 27, 30], [13, 21, 23, 24, 27, 28, 30, 32],
              [1, 3, 12, 15, 17, 28], [6, 30], [2, 14, 15, 19, 21, 23, 24, 26, 30],
              [1, 3, 4, 9, 11, 12, 15, 20, 24, 28, 29, 32],
              [7, 10, 19, 30, 31, 32],
              [3, 11, 16, 17, 20, 21, 22, 28],
              [1, 2, 8, 10, 17, 22, 30],
              [8, 9, 11, 14, 17, 18, 20],
              [5, 9, 11, 19, 24, 25, 26, 27, 29, 32],
              [8, 13, 14, 18, 19, 21, 23, 29],
              [1, 10, 12, 15, 18, 27, 30],
              [8, 9, 12, 17, 18, 21, 27, 30],
              [1, 2, 11, 12, 13, 14, 24, 25],
              [1, 2, 4, 6, 10, 12, 26, 31, 32],
              [4, 5, 9, 11, 28],
              [7, 20], [2, 6, 8, 23, 29, 32], [3, 6, 9, 11, 23, 30],
              [32], [1, 7, 12, 24], [11, 16, 17, 21, 22, 23],
              [1, 6, 22, 24, 28], [5, 14, 15, 24, 27, 29],
              [2, 13, 17, 20, 25, 28, 30],
              [4, 16, 17], [1, 2, 6, 7, 10, 15, 20, 30],
              [4, 6, 12, 17, 18, 21, 23, 25, 26, 27, 29],
              [9, 15, 18, 25, 26, 28, 30, 31, 21]]


        # obstacles data
        oxy = []
        for i, o in enumerate(oo):
            for oi in o:
                oxy.append([oi, i+1])
        ox = [o[0] for o in oxy]
        oy = [o[1] for o in oxy]

        # obstacles
        self.x_obst = ox  # ox []
        self.y_obst = oy  # oy []

        # robot
        self.heading = 0
        self.xs = 1
        self.ys = 1
        self.xt = 31
        self.yt = 31

    def map_3(self):

        # area
        lim = 32
        self.lim = lim
        self.x_min = 1
        self.y_min = 1
        self.x_max = lim
        self.y_max = lim

        # obstacles
        self.x_obst = []
        self.y_obst = []

        # robot
        self.heading = 0
        self.xs = 1
        self.ys = 1
        self.xt = 31
        self.yt = 31

    # ---------------------------
    # r10=[12,15,26,31] t10=[]
    # r11=[15,16] t11=[5,31]
    # r12=[10,12,19,25]   t12=[31]
    # r13=[2] t13=[7,13,22,28]
    # r14=[3,21,24,27]    t14=[4]
    # r15=[3,24]  t15=[19,28]
    # r16=[1,25,32]   t16=[6]
    # r17=[15,32] t17=[20]
    # r18=[15,29] t18=[7,16,19]
    # r19=[8,19,26,27]    t19=[25]
    # r20=[5,8]   t20=[21]
    # r21=[16,22,27]  t21=[11,13,14]
    # r22=[27]    t22=[16,31]
    # r23=[8,17,18,25,31] t23=[30]
    # r24=[23,27] t24=[13,19,20,28]
    # r25=[12]    t25=[1,7,14,31]
    # r26=[2] t26=[20]
    # r27=[22]    t27=[10,20,32]
    # r28=[19]    t28=[11,27]
    # r29=[]      t29=[24]
    # r30=[29]    t30=[]
    # r31=[31]    t31=[13,28]
    # r32=[]      t32=[8]


if __name__ == "__main__":
    mi = ModelInputs(map_id=2)
