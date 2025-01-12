import pygame
from OpenGL.GL import *

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  
    glVertex2f(x1, y1)        
    glVertex2f(x2, y2)        
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("OpenGL Line Drawing")
    
    
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  

        draw_line(-0.5, -0.5, 0.5, 0.5)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
