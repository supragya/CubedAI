class rubiks_cube:

	# Init
	def __init__(self):
		self.faceslist = (
							'top',
							'bottom',
							'front',
							'right',
							'left',
							'back'
						)

		self.ordering = {'up':('back', 'right', 'front', 'left'),
						'bottom':('front', 'right', 'left', 'back'),
						'front':('up', 'right', 'bottom', 'left'),
						'right':('up', 'back', 'bottom', 'front'),
						'left':('up', 'front', 'bottom', 'back'),
						'back':('up', 'left', 'bottom', 'right')
						}

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

		self.surfaceperface = []

rb = rubiks_cube()	