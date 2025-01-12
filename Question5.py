import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.5, 0.0, 0.5)
    
    glVertex2f(-0.5, -0.5)  
    glVertex2f(0.5, -0.5)   
    glVertex2f(0.0, 0.5)    
    
    glEnd()

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL Purple Triangle with PyGame")
    
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity() 
    glOrtho(-1, 1, -1, 1, -1, 1)  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
