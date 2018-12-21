import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(-1, 1, -1),
	(1, 1, -1),
	(1, 1, 1),
	(-1, 1, 1),

	(-1, -1, -1),
	(1, -1, -1),
	(1, -1, 1),
	(-1, -1, 1)
	)

edges = (
	(0,1),
	(1,2),
	(2,3),
	(3,0),

	(0,4),
	(1,5),
	(2,6),
	(3,7),

	(4,5),
	(5,6),
	(6,7),
	(7,4)
	)

colors = (
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    )

surfaces = (
    (0,1,2,3),
    # (4,5,6,7)
    )

def cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()


def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)
	glRotatef(25, 2, 1, 0)
	# cube()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		# glRotatef(1, 3, 1, 1) # Rotation matrix
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clearing function
		cube()
		pygame.display.flip() #updates display
		pygame.time.wait(10) 

main()