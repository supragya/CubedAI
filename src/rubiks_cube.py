class rubiks_cube:
	# Init
	def __init__(self):
		self.faceslist = ('top', 'bottom', 'front', 'right', 'left', 'back')

		self.facecolor = {'top' : 'white',
							'front': 'green',
							'bottom': 'blue',
							'right': 'red',
							'left': 'orange',
							'back': 'yellow'}

		self.ordering = {'up':('back', 'right', 'front', 'left'),
					'bottom':('front', 'right', 'left', 'back'),
					'front':('up', 'right', 'bottom', 'left'),
					'right':('up', 'back', 'bottom', 'front'),
					'left':('up', 'front', 'bottom', 'back'),
					'back':('up', 'left', 'bottom', 'right')}

		self.stickersize = 1
		self.inmargin = 0.1

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
		# 0 is the bottome left point, 35 is the top right point
		# The point looks as follows:
		#
		# 30  31  32  33  34  35
		# 24  25  26  27  28  29
		# ...
		# ...
		# ...
		# 0   1   2   3   4   5
		self.frontface = []
		self.rightface = []
		self.leftface = []
		self.backface = []
		self.topface = []
		self.bottomface = []
		for point in self.face:
			self.frontface.append(point[0], point[1], -self.inmargin)
			self.backface.append(point[0], point[1], self.stickersize*3 + self.inmargin)
			self.rightface.append(self.stickersize*3 + self.inmargin, point[0], point[1])
			self.leftface.append(-self.inmargin, point[0], point[1])
			self.topface.append(point[0], self.stickersize*3 + self.inmargin, point[1])
			self.bottomface.append(point[0], -self.inmargin, point[1])

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
		colorloss = 0.15 
		self.colors = {'active':
							{'red': (1, 0, 0),
							'blue': (0, 0, 1),
							'green': (0, 1, 0),
							'white': (1, 1, 1),
							'orange': (1, 0.647, 0),
							'yellow': (0, 1, 1)},
						'inactive':
							{'red': (1 - colorloss, 0, 0),
							'blue': (0, 0, 1 - colorloss),
							'green': (0, 1 - colorloss, 0),
							'white': (1 - colorloss, 1 - colorloss, 1 - colorloss),
							'orange': (1 - colorloss, 0.647 - colorloss*0.647, 0),
							'yellow': (0, 1 - colorloss, 1 - colorloss)}
						}

rb = rubiks_cube()
