import pygame
from random import *
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rebels Strike Back")
icon = pygame.image.load('rebels.png')
bg = pygame.image.load('starwarsbg.png')
pygame.display.set_icon(icon)
mixer.music.load('background.wav')
mixer.music.play(-1)

explosion = mixer.Sound('explosion.wav')

overgame = False
isintro = True
playerImg = pygame.image.load('xwing.png')
playerX = 372
playerY = 500
playerdX = 0
lost = False

laser_sound = mixer.Sound('laser.wav')
laserImg = pygame.image.load('laser.png')
laseractive = False
recharged = True
laserX = laserY = 5000
laserOrY = playerY - 10
laser2Img = pygame.image.load('greenlaser.png')
laser2X = laser2Y = 50
laser2active = False
recharged2 = True
laserdY = 6
laser2dY = 4

enemyImg = []
enemyX = []
enemyY = []
enemydX = []
enemydY = 0.3
enemy_count = 4
for i in range(enemy_count):
    enemyImg.append(pygame.image.load('tiefighter.png'))
    enemyX.append(randint(50, 700))
    enemyY.append(randint(-50, -10))
    enemydX.append(randrange(-2,4, 4))

score_val = 0
font = pygame.font.Font('Starjedi.ttf', 24)

textX = 15
textY = 2

overfont = pygame.font.Font('Starjedi.ttf', 48)
overfonthol = pygame.font.Font('Starjhol.ttf', 48)
def scoring():
    score = font.render("Score: {}".format(score_val), True, (200, 200, 200))
    screen.blit(score, (textX, textY))
def gameover():
    over = overfonthol.render("empire wins", True, (244, 67, 54))
    screen.blit(over, (240, 200))
    again = font.render("Press Enter to play again", True, (200, 200, 200))
    screen.blit(again, (210, 300))
def intro():
    title = overfonthol.render("Rebels Strike Back", True, (255, 202, 40))
    screen.blit(title, (130, 200))
    play = font.render("Press Enter to play", True, (200, 200, 200))
    screen.blit(play, (255, 300))

def player(x, y):
    screen.blit(playerImg, (int(x), int(y)))
def laser(x, y):
    screen.blit(laserImg, (int(x), int(y)))
def enemylaser(x ,y):
    screen.blit(laser2Img, (int(x), int(y)))
def enemy(x, y):
    screen.blit(enemyImg[i], (int(x), int(y)))
def collide(x1, x2, y1, y2):
    distance = math.hypot(x1-x2, y1-y2)
    if distance < 40:
        return True
    return False
def recharge():
    global enemyY, enemyX, score_val
    if collision and laserY != laserOrY:
        explosion.play()
        enemyX[i] = randint(50, 700)
        enemyY[i] = randint(-50, -10)
        score_val += 1

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerdX = -5
            if event.key == pygame.K_RIGHT:
                playerdX = 5
            if event.key == pygame.K_RETURN:
                lost = False
                overgame = False
                isintro = False
                score_val = 0
                for i in range(enemy_count):
                    enemyX[i] = randint(50, 700)
                    enemyY[i] = randint(-50, 0)
                playerX = 372
                playerY = 500
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerdX = 0
            if event.key == pygame.K_SPACE:
                if recharged:
                    laser_sound.play()
                    laseractive = True
                    recharged = False
                    laserY = laserOrY
                    laserX = randrange(playerX-10, playerX + 65, 55)
    if isintro:
        intro()
    if not isintro:
        playerX += playerdX
        if playerX > 700 or playerX < 50:
            playerX -= playerdX

        for i in range(enemy_count):

            if enemyX[i] > 700 or enemyX[i] < 50:
                enemydX[i] = enemydX[i] * -1
            enemyX[i] += enemydX[i]
            enemyY[i] += enemydY

            collision = collide(enemyX[i], laserX, enemyY[i], laserY)
            if laserY < 0 or collision:
                laseractive = False
                recharged = True

                recharge()
                laserY = laserOrY
            enemy(enemyX[i], enemyY[i])

            if enemyX[i] in range(playerX-50,playerX+50) and recharged2:
                laser_sound.play()
                laser2active = True
                recharged2 = False
                laser2Y = enemyY[i] + 50
                laser2X = randrange(enemyX[i]-10, enemyX[i] + 65, 55)
            if enemyY[i] > 600:
                enemyY[i] = randint(-50, -10)

            playercoll = collide(playerX, laser2X, playerY, laser2Y)
            playerenemycoll = False
            for k in range(enemy_count):
                playerenemycoll = collide(playerX, enemyX[k], playerY, enemyY[k])
                if playerenemycoll:
                    break
            if playercoll or playerenemycoll:
                explosion.play()
                lost = True
            if lost:
                laser2Y = 1700
                playerY = 1500
                playerX = 1500
                overgame = True

        if laser2active:
            laser2Y += laser2dY
            enemylaser(laser2X, laser2Y)
        if laser2Y > 600:
            recharged2 = True
        if laseractive:
            laserY -= laserdY
            laser(laserX, laserY)

        player(playerX, playerY)
    if overgame:
        gameover()
    scoring()
    pygame.display.update()