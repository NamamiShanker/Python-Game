import pygame
import random
import math
score = 0
# initialise the pygame
pygame.init()

# Creates the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load('alien.png'))

# background
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (800, 600))

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 368
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 300)
enemyX_change = 2

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = -10
bulletState = 'ready'

# Drawing on screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))

# function for detection of collision between Enemy and Bullet
def collisionEnemyBullet(x1, y1, x2, y2):
    if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 27:
        return True
    else:
        return False

# function for detection of collision between Enemy and Player
def collisionEnemyPlayer(x1, y1, x2, y2):
    if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 50:
        return True
    else:
        return False


# Game code
running = True
while running:
    pygame.time.delay(10)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT and playerX > 0:
                playerX_change = -5
            if event.key == pygame.K_RIGHT and playerX < 736:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bulletState == 'ready':
                bulletState = 'action'
                bulletX = playerX

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update Player
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    player(playerX, playerY)

    # Update enemy
    if 736 > enemyX > 0:
        enemyX += enemyX_change
    else:
        enemyY += 40
        enemyX_change = -enemyX_change
        enemyX += enemyX_change
    enemy(enemyX, enemyY)

    # Update Bullet
    if bulletState == 'action':
        if bulletY < 0:
            bulletState = 'ready'
            bulletY = 480
        bulletY += bulletY_change
        bullet(bulletX, bulletY)

    # Check collision

    if collisionEnemyBullet(bulletX, bulletY, enemyX, enemyY):
        score+=1
        bulletState = 'ready'
        bulletY = 480
        enemyX = random.randint(0, 736)
        enemyY = random.randint(0, 300)
        if enemyX_change < 0:
            enemyX_change -= 0.2
        else:
            enemyX_change += 0.2
        print(score)
    if collisionEnemyPlayer(enemyX, enemyY, playerX, playerY):
        running = False

    pygame.display.update()
