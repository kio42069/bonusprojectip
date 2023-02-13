import pygame
import os
import random
pygame.font.init()

SCORE_FONT = pygame.font.SysFont('comicsans', 40)
GAME_END  = pygame.font.SysFont('comicsans', 100)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
MAN_WIDTH = 100
MAN_HEIGHT = 100
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HydroHopper")

FREQUENCY = 0.4
MAN_HIT = pygame.USEREVENT
OBSTACLE_VEL = 10
VEL = 5
FPS = 60
MAN = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Game','man.png')),(MAN_WIDTH, MAN_HEIGHT))

def draw_win(bg, man, obstacles, man_health, score):
    WIN.blit(bg, (0,0))
    WIN.blit(MAN, (man.x, man.y))
    health_text = HEALTH_FONT.render(f"Lives remaining: {man_health}", 1, (0,0,0))
    WIN.blit(health_text, (10,10))
    score_text = SCORE_FONT.render(f"Score: {int(score)}",1 ,(0,0,0))
    WIN.blit(score_text, (WIDTH-score_text.get_width()-10,10))
    for obstacle in obstacles:
        pygame.draw.rect(WIN, (0,0,0), obstacle)
    pygame.display.update()
    

def draw_end(text):
    draw_text = GAME_END.render(text,1,(0,0,0))
    WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()//2,HEIGHT//2-draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)
    
def movement(keys_pressed, man):
    if keys_pressed[pygame.K_UP] and man.y > HEIGHT//2-30:
        man.y -= VEL
    if keys_pressed[pygame.K_DOWN] and man.y +VEL + man.height < HEIGHT - 15:
        man.y += VEL

def handle_obstacles(obstacles, man):
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_VEL
        if man.colliderect(obstacle):
            obstacles.remove(obstacle)
            pygame.event.post(pygame.event.Event(MAN_HIT))
        elif obstacle.x < 0:
            obstacles.remove(obstacle)
        
def main():
    score = 0
    obstacles = []
    clock = pygame.time.Clock()
    run = True
    img_num = 1
    obstacle_count = 0
    old_obstacle_count = 0
    man_health = 3
    man = pygame.Rect(100, 300, MAN_WIDTH, MAN_HEIGHT)
    while run:
        bg = pygame.transform.scale((pygame.image.load(os.path.join('Assets_Game',f'bgs{int(img_num)}.png'))),(WIDTH,HEIGHT))
        img_num += 0.1
        obstacle_count += FREQUENCY/10
        score += 0.01
        if img_num > 3:
            img_num = 1
        draw_win(bg, man, obstacles, man_health, score)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == MAN_HIT:
                man_health -= 1
        
        if int(obstacle_count) > old_obstacle_count:
            obstacle = pygame.Rect(WIDTH, random.randint(HEIGHT//2-30,HEIGHT), 10, 5)
            obstacles.append(obstacle)
            old_obstacle_count = obstacle_count
        game_end_text = ""    
        if man_health <= 0:
            game_end_text = f"Score: {int(score)}"
        if game_end_text != "":
            draw_end(game_end_text)
            break
        handle_obstacles(obstacles, man)
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, man)
        
    main()
    
if __name__ == "__main__":
    main()