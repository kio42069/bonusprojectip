import pygame
import random
import button
import os


WIDTH, HEIGHT = 1290, 650
CARD_WIDTH, CARD_HEIGHT = 150,150
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Elements Unleashed')

def make_deck():
    deck = []
    for _ in range(5):
        card = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Elementsunleashed',random.choice(['snow.png','fire.png','water.png']))),(CARD_WIDTH,CARD_HEIGHT))
        deck.append(card)
    return deck

def add_card(deck):
    empty = deck.index(0)
    card = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Elementsunleashed',random.choice(['snow.png','fire.png','water.png']))),(CARD_WIDTH,CARD_HEIGHT))
    deck[empty] = card

def create_buttons():
    button_img = pygame.image.load(r"C:\Users\Dell\Desktop\bonusprojectip\Assets_Elementsunleashed\button_transparent.png").convert_alpha()
    buttons = dict()
    for i in range(5):
        buttons.append(button.Button(150+200*i,485, button_img,1))
    return buttons

run = True
card_deck = make_deck()
card_chosen = pygame.image.load(r"C:\Users\Dell\Desktop\bonusprojectip\Assets_Elementsunleashed\button_transparent.png").convert_alpha()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(1290,650))
    WIN.blit(bg,(0,0))
    for i in range(5):
        WIN.blit(card_deck[i],(150+200*i,485))
    buttons = create_buttons()
    
    for i in range(5):
        if buttons[i].draw(WIN):
            card_chosen = card_deck[i]
            card_deck[i] = pygame.image.load(r"C:\Users\Dell\Desktop\bonusprojectip\Assets_Elementsunleashed\button_transparent.png").convert_alpha()
            card_chosen = pygame.transform.scale(card_chosen,(200,200))
            WIN.blit(card_chosen,(250,100))
            pygame.display.update()
            pygame.time.delay(500)
            cpu_card = 
    WIN.blit(card_chosen,(250,100))
    pygame.display.update()