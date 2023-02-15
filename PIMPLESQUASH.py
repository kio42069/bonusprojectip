import pygame
import os

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PimpleSquash")
MOON_WIDTH, MOON_HEIGHT = 200, 200
MOON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Pimplesquash','moon.png')),(MOON_WIDTH, MOON_HEIGHT))


def draw_win(bg, angle):
    loc = MOON_IMAGE.get_rect().center
    MOON = pygame.transform.rotate(MOON_IMAGE, angle)
    MOON.get_rect().center = loc
    WIN.blit(bg,(0,0))
    WIN.blit(MOON,(WIDTH//2-MOON_WIDTH//2,HEIGHT//2-MOON_HEIGHT//2))
    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()
    angle = 0
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Pimplesquash","space.png")),(WIDTH+700, HEIGHT))
        draw_win(bg,angle)
        angle += 90
    main()
    
if __name__ == "__main__":
    main()
