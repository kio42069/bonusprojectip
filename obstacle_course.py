import pygame
import os

WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HydroHopper")


FPS = 60


def draw_win(bg):
    WIN.blit(bg, (0,0))
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    x = 1
    while run:
        bg = pygame.transform.scale((pygame.image.load(os.path.join('Assets_Game',f'bgs{x}.png'))),(WIDTH,HEIGHT))
        x += 1
        if x > 3:
            x = 1
            print(1)
        draw_win(bg)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
    main()
    
if __name__ == "__main__":
    main()