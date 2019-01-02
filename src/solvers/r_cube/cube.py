import random
from OpenGL.GL import *
from OpenGL.GLU import *

class rubiks_cube:
    # Init
    def __init__(self):
        self.faceslist = ('up', 'down', 'front', 'right', 'left', 'back')
        # From now, up is face 0, down is face 1 and so on
        # DO NOT CHANGE THE ORDER OF FACESLIST, CODE MAY BREAK

        self.facecolor = {'up' : 'white',
                        'front': 'green',
                        'down': 'blue',
                        'right': 'red',
                        'left': 'orange',
                        'back': 'yellow'}

        self.ordering = {'up':('back', 'right', 'front', 'left'),
                    'down':('back', 'right', 'front', 'left'),
                    'front':('up', 'right', 'down', 'left'),
                    'right':('up', 'back', 'down', 'front'),
                    'left':('up', 'front', 'down', 'back'),
                    'back':('up', 'left', 'down', 'right')}

        self.faceneighbors = {'up': [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8],
                            'down': [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0],
                            'front': [0, 1, 2, 6, 3, 0, 2, 1, 0, 2, 5, 8],
                            'right': [2, 5, 8, 6, 3, 0, 8, 5, 2, 2, 5, 8],
                            'left': [6, 3, 0, 6, 3, 0, 0, 3, 6, 2, 5, 8],
                            'back': [8, 7, 6, 6, 3, 0, 6, 7, 8, 2, 5, 8]}

        self.stickersize = 1
        self.inmargin = 0.09

        self.facetemplate = []
        for i in range(6):
            for j in range(6):
                cur_x = (i+1)//2*(self.stickersize)
                cur_y = (j+1)//2*(self.stickersize)
                if i%2 == 0:
                    cur_x += self.inmargin
                else:
                    cur_x -= self.inmargin
                if j%2 == 0:
                    cur_y += self.inmargin
                else:
                    cur_y -= self.inmargin
                # print("{} - {} - {} {}".format(i, j, cur_x, cur_y))
                self.facetemplate.append((cur_x, cur_y))
        # print(self.face)

        # Assume that the cube is made up of 36 points (4 points per sticker)
        # 0 is the downe left point, 35 is the up right point
        # The point looks as follows:
        #
        # 30  31  32  33  34  35
        # 24  25  26  27  28  29
        # ...
        # ...
        # ...
        # 0   1   2   3   4   5
        frontface = []
        rightface = []
        leftface = []
        backface = []
        upface = []
        downface = []
        for point in self.facetemplate:
            frontface.append((point[1], point[0], -self.inmargin))
            backface.append((-point[1] + self.stickersize*3, point[0], - self.stickersize*3 - self.inmargin))
            rightface.append((self.stickersize*3 + self.inmargin, point[0], -point[1]))
            leftface.append((-self.inmargin, point[0], point[1] - self.stickersize*3))
            upface.append((point[1], self.stickersize*3 + self.inmargin, -point[0]))
            downface.append((point[1], -self.inmargin, -point[0]))
        # Alert: self.facepoints is depended on self.faceslist config
        self.facepoints = [upface, downface, frontface, rightface, leftface, backface]

        self.surfaceperface = (
                            (0, 1, 7, 6),
                            (2, 3, 9, 8),
                            (4, 5, 11, 10),
                            (12, 13, 19, 18),
                            (14, 15, 21, 20),
                            (16, 17, 23, 22),
                            (24, 25, 31, 30),
                            (26, 27, 33, 32),
                            (28, 29, 35, 34)
                            )

        # We call all those faces active which look towards the camera
        colorloss = 0.45 
        self.colors = {'active':
                            {'red': (1, 0, 0),
                            'blue': (0, 0, 1),
                            'green': (0, 1, 0),
                            'white': (1, 1, 1),
                            'orange': (1, 0.647, 0),
                            'yellow': (1, 1, 0)},
                        'inactive':
                            {'red': (1 - colorloss, 0, 0),
                            'blue': (0, 0, 1 - colorloss),
                            'green': (0, 1 - colorloss, 0),
                            'white': (1 - colorloss, 1 - colorloss, 1 - colorloss),
                            'orange': (1 - colorloss, 0.647 - colorloss*0.647, 0),
                            'yellow': (1 - colorloss, 1 - colorloss, 0)}
                        }
        self.cubeconfig = []
        for face in self.faceslist:
            # CubeFace is a 9 element list containing color from bottom left to top right
            # 6 7 8
            # 3 4 5
            # 0 1 2
            cubeface = []
            for x in range(9):
                cubeface.append(self.facecolor[face])
            self.cubeconfig.append(cubeface)
    
    def displaycube(self):
        glBegin(GL_QUADS)
        activityflag = [1, 0, 1, 0, 1, 0]

        # First render the inactive faces
        for x in range(6):
            if activityflag[x] == 0:
                y = 0
                for surface in self.surfaceperface:
                    for point in surface:
                        glColor3fv(self.colors['inactive'][self.cubeconfig[x][y]])
                        glVertex3fv(self.facepoints[x][point])
                    y += 1
        # Second, render the active faces
        for x in range(6):
            if activityflag[x] == 1:
                y = 0
                for surface in self.surfaceperface:
                    for point in surface:
                        glColor3fv(self.colors['active'][self.cubeconfig[x][y]])
                        glVertex3fv(self.facepoints[x][point])
                    y += 1

        glEnd()

    # Moves that cube can take
    # move_xxy means to rotate face x once in direction of y
    # e.g. move_toc means rotate upface once in clockwise direction
    def move_U(self):
        self.rotateronface('up', 2)
        self.rotateraroundface('up', 3)
    def move_UI(self):
        self.rotateronface('up', -2)
        self.rotateraroundface('up', -3)
    def move_D(self):
        self.rotateronface('down', -2)
        self.rotateraroundface('down', -3)
    def move_DI(self):
        self.rotateronface('down', 2)
        self.rotateraroundface('down', 3)
    def move_F(self):
        self.rotateronface('front', 2)
        self.rotateraroundface('front', 3)
    def move_FI(self):
        self.rotateronface('front', -2)
        self.rotateraroundface('front', -3)
    def move_R(self):
        self.rotateronface('right', 2)
        self.rotateraroundface('right', 3)
    def move_RI(self):
        self.rotateronface('right', -2)
        self.rotateraroundface('right', -3)
    def move_L(self):
        self.rotateronface('left', 2)
        self.rotateraroundface('left', 3)
    def move_LI(self):
        self.rotateronface('left', -2)
        self.rotateraroundface('left', -3)
    def move_B(self):
        self.rotateronface('back', 2)
        self.rotateraroundface('back', 3)
    def move_BI(self):
        self.rotateronface('back', -2)
        self.rotateraroundface('back', -3)

    def rotateronface(self, face, offset):
        c = self.cubeconfig[self.faceslist.index(face)]
        rimpoints = [0, 1, 2, 5, 8, 7, 6, 3]
        buf = [c[x] for x in rimpoints]
        rotatedbuf = [buf[(x + offset)%8] for x in range(8)]
        x = 0
        for y in rimpoints:
            c[y] = rotatedbuf[x]
            x += 1
        self.cubeconfig[self.faceslist.index(face)] = c

    def rotateraroundface(self, face, offset):
        fourfaces = self.ordering[face]
        buf = []
        c = self.faceneighbors[face]
        buf = [self.cubeconfig[self.faceslist.index(fourfaces[x//3])][c[x]] for x in range(12)]
        rotatedbuf = [buf[(x - offset)%12] for x in range(12)]
        for x in range(12):
            self.cubeconfig[self.faceslist.index(fourfaces[x//3])][c[x]] = rotatedbuf[x]

    def scramble(self, minmoves = 10, maxmoves = 30):
        movecount = 0
        if minmoves > maxmoves:
            movecount = maxmoves
        else:
            movecount = random.randint(minmoves, maxmoves)
        moves = []
        for x in range(movecount):
            y = random.randint(0, 12)

            if y == 0:
                moves.append('U')
                self.move_U()
            elif y == 1:
                moves.append('UI')
                self.move_UI()
            elif y == 2:
                moves.append('D')
                self.move_D()
            elif y == 3:
                moves.append('DI')
                self.move_DI()
            elif y == 4:
                moves.append('F')
                self.move_F()
            elif y == 5:
                moves.append('FI')
                self.move_FI()
            elif y == 6:
                moves.append('R')
                self.move_R()
            elif y == 7:
                moves.append('RI')
                self.move_RI()
            elif y == 8:
                moves.append('L')
                self.move_L()
            elif y == 9:
                moves.append('LI')
                self.move_LI()
            elif y == 10:
                moves.append('B')
                self.move_B()
            elif y == 11:
                moves.append('BI')
                self.move_BI()
        return moves