import pygame
import os


MAN_WIDTH = 100
MAN_HEIGHT = 100
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HydroHopper")


FPS = 60
MAN = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Game','man.png')),(MAN_WIDTH, MAN_HEIGHT))

def draw_win(bg, man):
    WIN.blit(bg, (0,0))
    WIN.blit(MAN, (man.x, man.y))
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    img_num = 1
    man = pygame.Rect(100, 300, MAN_WIDTH, MAN_HEIGHT)
    while run:
        bg = pygame.transform.scale((pygame.image.load(os.path.join('Assets_Game',f'bgs{img_num}.png'))),(WIDTH,HEIGHT))
        img_num += 1
        if img_num > 3:
            img_num = 1
        draw_win(bg, man)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
    main()
    
if __name__ == "__main__":
    main()