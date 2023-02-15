def kek():
    import pygame
    import os
    import random
    pygame.font.init()
    pygame.mixer.init()
    from time import time

    SCORE_FONT = pygame.font.SysFont('georgia', 40)
    GAME_END  = pygame.font.SysFont('georgia', 100)
    HEALTH_FONT = pygame.font.SysFont('georgia', 40)
    MAN_WIDTH, MAN_HEIGHT = 100, 100
    ROCK_WIDTH, ROCK_HEIGHT = 100,40
    WIDTH, HEIGHT = 1000,500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("HydroHopper")
    CRASH_SOUND = pygame.mixer.Sound(os.path.join('Assets_Hydrohopper', 'crash.wav'))

    FREQUENCY = 0.4
    MAN_HIT = pygame.USEREVENT
    FPS = 60
    MAN = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Hydrohopper','man.png')),(MAN_WIDTH, MAN_HEIGHT))

    def draw_win(bg, man, obstacles, man_health, score, highscore):
        WIN.blit(bg, (0,0))
        WIN.blit(MAN, (man.x, man.y))
        health_text = HEALTH_FONT.render(f"Lives remaining: {man_health}", 1, (0,0,0))
        WIN.blit(health_text, (10,10))
        score_text = SCORE_FONT.render(f"Score: {int(score)}",1 ,(0,0,0))
        WIN.blit(score_text, (WIDTH-score_text.get_width()-10,10))
        highscore_text = SCORE_FONT.render(f"Highscore: {int(highscore)}",1 ,(0,0,0))
        WIN.blit(highscore_text, (WIDTH-highscore_text.get_width()-10,10+score_text.get_height()))
        ROCK = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Hydrohopper','shark.png')),(ROCK_WIDTH, ROCK_HEIGHT))
        for obstacle in obstacles:
            WIN.blit(ROCK, (obstacle.x, obstacle.y))
            
        pygame.display.update()
        

    def draw_end(text):
        draw_text = GAME_END.render(text,1,(0,0,0))
        WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()//2,HEIGHT//2-draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(1000)
        
    def movement(keys_pressed, man, VEL):
        if keys_pressed[pygame.K_UP] and man.y > 15:
            man.y -= VEL
        if keys_pressed[pygame.K_DOWN] and man.y +VEL + man.height < HEIGHT - 15:
            man.y += VEL

    def handle_obstacles(obstacles, man, OBSTACLE_VEL):
        for obstacle in obstacles:
            obstacle.x -= OBSTACLE_VEL
            if man.colliderect(obstacle):
                obstacles.remove(obstacle)
                pygame.event.post(pygame.event.Event(MAN_HIT))
            elif obstacle.x < 0:
                obstacles.remove(obstacle)
            
    def main():
        OBSTACLE_VEL = 10
        VEL = 5
        score = 0
        obstacles = []
        clock = pygame.time.Clock()
        run = True
        obstacle_count = 0
        old_obstacle_count = 0
        man_health = 999999999
        man = pygame.Rect(100, 300, MAN_WIDTH, MAN_HEIGHT)
        with open("highscore.txt", "r") as file:
            recs = file.readlines()
        recs = [int(x) for x in recs]
        recs.append(0)
        highscore = max(recs)
        start = time()
        while run:
            now = time()
            if int(now-start) % 2 == 0 and int(now-start) != 0:
                OBSTACLE_VEL += 0.01
                VEL += 0.01
            bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Hydrohopper','ocean.jpg')),(WIDTH,HEIGHT))
            obstacle_count += FREQUENCY/10
            score += 0.1
            draw_win(bg, man, obstacles, man_health, score, highscore)
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == MAN_HIT:
                    man_health -= 1
                    CRASH_SOUND.play()

            if int(obstacle_count) > old_obstacle_count:
                obstacle = pygame.Rect(WIDTH, random.randint(0,HEIGHT), ROCK_WIDTH, ROCK_HEIGHT)
                obstacles.append(obstacle)
                old_obstacle_count = obstacle_count
            game_end_text = ""    
            if man_health <= 0:
                game_end_text = f"Score: {int(score)}"
            if game_end_text != "":
                draw_end(game_end_text)
                break
            handle_obstacles(obstacles, man, OBSTACLE_VEL)
            keys_pressed = pygame.key.get_pressed()
            movement(keys_pressed, man, VEL)
        with open("highscore.txt","a") as file:
            file.write(str(int(score))+"\n")
        main()
    main()
"""    if __name__ == "__main__":
        main()"""
