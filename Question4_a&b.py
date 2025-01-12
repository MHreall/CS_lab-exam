import pygame
import sys

def main():
    pygame.init()
    
    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Canvas") 

    white = (255, 255, 255)
    screen.fill(white)
    
    red = (255, 0, 0)
    start_pos = (50, 50)  
    end_pos = (50 + 200, 50)  
    line_width = 3
    pygame.draw.line(screen, red, start_pos, end_pos, line_width)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()
                
if __name__ == "__main__":
    main()
