import pygame
 
pygame.init()
screen = pygame.display.set_mode((720, 480))
w, h = pygame.display.get_surface().get_size()
done = False
 
x = 0
y = 0

girdCols = 4
gridRows = 4

snakeWidth = 30
snakeHeight = 30

isRight = False
isLeft = False
isUp = False
isDown = False

while not done:
        pygame.time.delay(10) 
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        
        if pressed [pygame.K_RIGHT]: 
            if(x + snakeWidth >= w):
                x = x
            else:
                x += 1
            isRight = True
            isLeft = False
            isUp = False
            isDown = False
        if pressed[pygame.K_LEFT]: 
            if(x <= 0):
                x = x
            else:
                x -= 1
            isRight = False
            isLeft = True
            isUp = False
            isDown = False
        if pressed[pygame.K_UP]: 
            if(y <= 0):
                y = y
            else:
                y -= 1
            isRight = False
            isLeft = False
            isUp = True
            isDown = False
        if pressed[pygame.K_DOWN]:
            if(y + snakeHeight >= h):
                y = y
            else:
                y += 1
            isRight = False
            isLeft = False
            isUp = False
            isDown = True

        # while(isRight == True):
        #     print("Right")
        #     x += 1
        # while(isLeft == True):
        #     x -= 1
        # while(isDown == True):
        #     y += 1
        # while(isUp == True):
        #     y -= 1

        screen.fill((0, 0, 0)) 
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, snakeWidth, snakeHeight))

        pygame.display.update() 