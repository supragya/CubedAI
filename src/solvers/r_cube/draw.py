import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def showaxis():
    glBegin(GL_LINES)
    vertices = ((0, 0, 0),
                (3, 0, 0),
                (0, 3, 0),
                (0, 0, 3))
    edges = ((0, 1),
            (0, 2),
            (0, 3))
    axiscolors = ((1, 0, 0),
                    (0, 1, 0),
                    (0, 0, 1))
    for x in range(3):
        glColor3fv(axiscolors[x])
        for vertex in edges[x]:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cube(rb):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-1.5, -1.5, -10)
    glRotatef(45, 3, 2.5, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # glRotatef(1, 3, 1, 1) # Rotation matrix
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clearing function
        rb.displaycube()
        # showaxis()
        pygame.display.flip() #updates display
        pygame.time.wait(10)