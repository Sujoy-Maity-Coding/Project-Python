import random
import math
import pygame
from pygame import mixer
# Initialize pygame all function
pygame.init()

# Create a screen
screen=pygame.display.set_mode((400,500))

# Title and icon
pygame.display.set_caption("Sujoy Maity Game")
img1=r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\gameIcon.png"       # right click on the picture and then click property option and then copy path
icon=pygame.image.load(img1)
pygame.display.set_icon(icon)

# Adding score
score=0
style=pygame.font.SysFont(None,20)
def textScreen(text,x,y):
    t=style.render(text,True,(255,255,255))
    screen.blit(t,(x,y))

# Teaxt fr game over
overText=pygame.font.SysFont(None,50)
def overScreen(text,x,y):
    t=overText.render(text,True,(255,255,255))
    screen.blit(t,(x,y))

# Adding background music
mixer.music.load(r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\background.mp3")
mixer.music.play(-1)        # Here -1 means play loop

# Adding player
img2=r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\player.png"
playerImg=pygame.image.load(img2)
playerX=180
playerY=410
playerX_change=0
def player(x,y):
    # Here blit means draw
    screen.blit(playerImg,(x,y))

# Adding multiple Enemy
img3=r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\enemy.png"
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
numEnemy=5
for i in range(numEnemy):
    enemyImg.append(pygame.image.load(img3))
    enemyX.append(random.randint(0,368))        # 400-32px=368
    enemyY.append(random.randint(30,300))
    enemyX_change.append(0.05)
    enemyY_change.append(35)
def enemy(x,y,i):
    # Here blit means draw
    screen.blit(enemyImg[i],(x,y))

# Adding Bullet
img5=r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\bullet.png"
bulletImg=pygame.image.load(img5)
bulletX=0
bulletY=410
bulletX_change=0
bulletY_change=0.1
bulletState="ready"     # ready-> You cannot see the bullet on the screen
def fireBullet(x,y):
    global bulletState      # To access bullet state variable
    bulletState="fire"      # fire -> Fire the bullet
    screen.blit(bulletImg,(x,y))

# Collision
def ifCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))     # Formula of distance between two points
    if distance<27:     # Here 27 is just a number
        return True
    else:
        return False

# Add background image
img4=r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\bg.png"
bgImg=pygame.image.load(img4)

# Game Loop
running=True
while running:
    # To change the background color   [RGB-> Red,Green,Blue]
    screen.fill((0,0,0))
    screen.blit(bgImg,(0,0))

    # To access all event
    for event in pygame.event.get():
        # To close the screen
        if event.type==pygame.QUIT:
            running=False
        # Check Which keystroke is press left or right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.1
            if event.key==pygame.K_RIGHT:
                playerX_change=0.1
            if event.key==pygame.K_SPACE:
                # Adding bullet shound when it ready for fire
                bs=mixer.Sound(r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\bullet.mp3")
                bs.play()
                # When bullet is ready state then it fire if we click space button
                if bulletState is "ready":
                    bulletX=playerX
                    fireBullet(bulletX,bulletY )
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    
    # For movement player
    playerX+=playerX_change
    # Set Boundary for player
    if playerX<=0:
        playerX=0
    elif playerX>=368:      # Here we set 368 beacause screen width(400) - player size(32px) = 368
        playerX=368
    
    for i in range(numEnemy):
        # Game Over
        if enemyY[i]>380:
            for j in range(numEnemy):
                enemyY[j]=2000       # Means when any one enemy reach out the above 380 then all enemy left from the screen
            overScreen("GAME OVER",80,230)
            break

        # For movement enemy
        enemyX[i]+=enemyX_change[i]
        # Set Boundary for enemy
        if enemyX[i]<=0:
            enemyX_change[i]=0.05
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=368:      # Here we set 368 beacause screen width(400) - enemy size(32px) = 368
            enemyX_change[i]=-0.05
            enemyY[i]+=enemyY_change[i]

        # Collision
        collision=ifCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            # Adding enemy shound when it ready for fire
            es=mixer.Sound(r"C:\Users\91700\OneDrive\Desktop\Python Project\2- Space game\enemy.mp3")
            es.play()
            bulletY=410
            bulletState="ready"
            score+=1
            enemyX[i]=random.randint(0,368)        # 400-32px=368
            enemyY[i]=random.randint(30,300)
    
        enemy(enemyX[i],enemyY[i],i)

    # For firing multiple bullet
    if bulletY<=0:
        bulletY=410
        bulletState="ready"
    if bulletState is "fire":
        fireBullet(bulletX,bulletY)
        bulletY-=bulletY_change

    textScreen(f"Score: {score}",0,0)

    player(playerX,playerY)
    pygame.display.update()