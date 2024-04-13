import pygame
import random
from pygame.locals import *

def runGame2():
    global gameLoop
    
    def randColor():
        r = random.randrange(200,256)
        g = random.randrange(100,150)
        b = random.randrange(150,200)
        return (r,g,b)

    pygame.init()

    width = 800
    height = 600

    color = (0,200,170)
    platColor = randColor()

    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    score = 0

    ############################################################################################################
    #GAME INTRO FUNCTION

    def gameIntro():
     
        #BALL
        x = width/2
        y = 250
        xVel = 0
        yVel = 0
        ballRad = 50
        g = 1.5

        #PLATFORM
        xCord  = 200
        yCord  = 580
        pRight = True
        pVel   = 5
        xCord  += 1

        boardFont = pygame.font.Font(pygame.font.get_default_font(),40)
        overFont = pygame.font.Font(pygame.font.get_default_font(),100)
        listFont = pygame.font.Font(pygame.font.get_default_font(),30)
        controlFont = pygame.font.Font(pygame.font.get_default_font(),20)
    
        running = True
        gameFrozen = True
        while gameFrozen:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            
                screen.fill((65,65,65))

    #-----------------------------------------------------------------------------------------------------------
            
                text_surface = listFont.render("You Control The Ball", True, ("white"))
                screen.blit(text_surface, (25,230))
            
                text_surface = controlFont.render("Left: 'A' or LEFT key", True, ("white"))
                screen.blit(text_surface, (68,270))
            
                text_surface = controlFont.render("Right: 'D' or RIGHT key", True, ("white"))
                screen.blit(text_surface, (55,300))
           
                text_surface = boardFont.render("Press 'S' or DOWN key to start", True, ("white"))
                screen.blit(text_surface, (100,500))
            
                text_surface = overFont.render("KEEP IT UP!", True, (platColor))
                screen.blit(text_surface, (100,75))
            
    #-----------------------------------------------------------------------------------------------------------
          
                keys = pygame.key.get_pressed()
        
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    return
        
                if keys[pygame.K_q]:
                    running = False
            
                pygame.draw.circle(screen, color, (x,y), ballRad)  
                pygame.draw.rect(screen, platColor, pygame.Rect(xCord,yCord,150,20))

                pygame.display.flip()
                clock.tick(60)

            global gameLoop
            gameLoop = False
            return
    
    ############################################################################################################
    #MAIN GAME FUNCTION

    def gameMain():
        global score
        score = 0
        global platColor
    #-----------------------------------------------------------------------------------------------------------
    #DIMENSIONS

        #BALL
        x = width/2
        y = 250
        xVel = 0
        yVel = 0
        ballRad = 50
        g = 1.5

        #PLATFORM
        xCord  = 200
        yCord  = 580
        pRight = True
        pVel   = 5
        xCord  += 1
    
        scoreFont = pygame.font.Font(pygame.font.get_default_font(),40)
    #-----------------------------------------------------------------------------------------------------------

        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                 
            screen.fill((65,65,65))
    
            keys = pygame.key.get_pressed()
        
            text_surface = scoreFont.render("Score: "+str(score), True, ("white"))
            screen.blit(text_surface, (10,10))

    #-----------------------------------------------------------------------------------------------------------
    #BALL PHYSICS

            movingHorizontally = False
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                movingHorizontally = True
            
                if xVel > -5:
                    xVel -= 1
    
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                movingHorizontally = True
        
                if xVel < 5:
                    xVel += 1
    
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                y += 4
    
            if keys[pygame.K_q]:
                running = False
    
            if movingHorizontally == False:
                xVel *= 0.95
    
            x += xVel
            yVel += g
            y += yVel
    
            #left border check
            if x < ballRad:
                x = ballRad
            #right border check
            if x >= (width-ballRad):
                x = width-ballRad
    
            #height limit check
            if y <= 250:
                y = 250
                yVel = 0
    
    #-----------------------------------------------------------------------------------------------------------
    #PLATFORM PHYSICS
    
            pVel *= 1.0001
    
            if pRight == True:
                xCord += pVel
            else:
                xCord -= pVel
    
            if xCord > (width-150):
                pRight = False
    
            if xCord < 0:
                pRight = True
    
    #-----------------------------------------------------------------------------------------------------------
    #COLLISION DETECTION + SCORE
        
            ball = {"xBottom":x, "yBottom":y+50}
            platform = {"xLeft":xCord, "yTop":yCord, "xRight":xCord+150}
            #When the coordinates of the bottom of the ball land between the coordinates of the
            #platform  (xCord,yCord < (height - ballRad) < xCord+150,yCord)
   
            #platform check
            if ball["yBottom"] > platform["yTop"] and platform["xLeft"] <= ball["xBottom"] <= platform["xRight"]:
                platColor = randColor()
                score += 1
                yVel *= -1
                y = (platform["yTop"]-ballRad) - (y-(platform["yTop"]-ballRad))
        
            if ball["yBottom"] > height+300:
                return score

    #-----------------------------------------------------------------------------------------------------------
    #DRAW
            pygame.draw.circle(screen, color, (x,y), ballRad)  
            if 'platColor' not in globals():
                platColor = randColor()
            pygame.draw.rect(screen, platColor, pygame.Rect(xCord,yCord,150,20))
    #-----------------------------------------------------------------------------------------------------------
            pygame.display.flip()
            clock.tick(60)

    ############################################################################################################
    #GAME OVER FUNCTION

    def gameOver():
        global score

        scoreFont = pygame.font.Font(pygame.font.get_default_font(),40)
 
    #-----------------------------------------------------------------------------------------------------------
    #FILE FIND/CREATION
 
        try:
            scoreFile = open("leaderboard.txt", "r").read()

        except FileNotFoundError:
            print("File Not Found, Creating New")
    
            scoreFile = open("leaderboard.txt", "w")
            scoreFile.write("0,0,0,0,0")
            scoreFile.close()
            scoreFile = open("leaderboard.txt", "r").read()

        highScores = scoreFile.strip().split(",")
    
    #------------------------------------------------------------------------------------------------------------
    #SORT HIGH SCORES WITH NEW SCORE

        def sort(highScores, newScore):
    
            for i in range(len(highScores)):
                    if newScore > int(highScores[i]):
                    
                        highScores.insert(i,str(newScore))
                        break          

            if len(highScores)>5:
                del highScores[5]
        
        sort(highScores,score)

    #------------------------------------------------------------------------------------------------------------
    #REWRITE FILE

        highScoresStr = ",".join(highScores)
    
        scoreFile = open("leaderboard.txt", "w")
        scoreFile.write(highScoresStr)
        scoreFile.close()

    #------------------------------------------------------------------------------------------------------------
    
        #BALL
        x = width/2
        y = 250
        xVel = 0
        yVel = 0
        ballRad = 50
        g = 1.5


        #PLATFORM
        xCord  = 200
        yCord  = 580
        pRight = True
        pVel   = 5
        xCord  += 1

        gameFrozen = True
        overFont = pygame.font.Font(pygame.font.get_default_font(),100)
        boardFont = pygame.font.Font(pygame.font.get_default_font(),40)
        listFont = pygame.font.Font(pygame.font.get_default_font(),30)

        running = True
        while gameFrozen:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    
                screen.fill((65,65,65))

    #-----------------------------------------------------------------------------------------------------------

                text_surface = scoreFont.render("Score: "+str(score), True, ("white"))
                screen.blit(text_surface, (10,10))
           
                text_surface = boardFont.render("Press 'S' or DOWN key to restart", True, ("white"))
                screen.blit(text_surface, (85,500))
           
                text_surface = overFont.render("GAME OVER", True, (platColor))
                screen.blit(text_surface, (85,75))
            
                text_surface = boardFont.render("High Scores", True, ("white"))
                screen.blit(text_surface, (525,200))
            
                text_surface = listFont.render("1: "+str(highScores[0]), True, (0,220,190))
                screen.blit(text_surface, (600,255))
            
                text_surface = listFont.render("2: "+str(highScores[1]), True, (0,180,150))
                screen.blit(text_surface, (600,290))
            
                text_surface = listFont.render("3: "+str(highScores[2]), True, (0,140,110))
                screen.blit(text_surface, (600,325))
            
                text_surface = listFont.render("4: "+str(highScores[3]), True, (0,120,90))
                screen.blit(text_surface, (600,360))
            
                text_surface = listFont.render("5: "+str(highScores[4]), True, (0,100,70))
                screen.blit(text_surface, (600,395))
            
    #-----------------------------------------------------------------------------------------------------------
            
                keys = pygame.key.get_pressed()
        
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    return
        
                if keys[pygame.K_q]:
                    running = False
            
                pygame.draw.circle(screen, color, (x,y), ballRad)  
                pygame.draw.rect(screen, platColor, pygame.Rect(xCord,yCord,150,20))

                pygame.display.flip()
                clock.tick(60)
                
            global gameLoop
            gameLoop = False
            gameFrozen = False


    ############################################################################################################
    #PLAY

    gameLoop = True

    while gameLoop:
    
        gameIntro()
        gameMain()
        gameOver()

    pygame.quit()