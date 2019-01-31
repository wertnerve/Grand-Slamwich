import pygame
import time
from PIL import Image
from finalProject import intro

pygame.init()
pygame.font.init()
myFont=pygame.font.SysFont("Courier",30)

#color templates
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#enemy stats and player HP
enemyHP=100
attack=30
defense=30
playerHP=150

#enemy life counter
timesFought=0

#window size
size=[800,800]
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Grand Slammwich')

pygame.draw.rect(screen,red,[75,10,50,20])

#specific game clock
clock = pygame.time.Clock()
f1= pygame.image.load('C:/Python34/finalProject/finalProjectFrames/f4p.png')
textBox = pygame.image.load('C:/Python34/finalProject/finalProjectFrames/textbox.png')
enemy= pygame.image.load('C:/Python34/finalProject/enemy.png')

#setup textbox and background

screen.blit(f1,(0,0))
screen.blit(textBox,(100,000))

#setup font for printouts

textOut=myFont.render("         Eureka!",True,white)
screen.blit(textOut,(130,30))
textOut=myFont.render("    Welcome to my game!",True,white)
screen.blit(textOut,(130,60))
textOut=myFont.render("   Press SPACE to begin ",True,white)
screen.blit(textOut,(130,90))

keys=pygame.key.get_pressed()
#getters for stats
def getAttack(): return attack
def getDefense(): return defense
def getEnemyHP(): return enemyHP
def getHP(): return playerHP

#wait for player to press space before continuing
def stall():
    stalling=True
    while stalling:
        event=pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stalling=False
                
#wait for player to enter number option and return it               
def inputStall():
    stalling=True
    
    while stalling:
     for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                stalling=False
                return 1
            if event.key == pygame.K_2:
                stalling=False
                return 2
            if event.key == pygame.K_3:
                stalling=False
                return 3
            if event.key == pygame.K_4:
                stalling=False
                return 4

            
#longer sentences get smoller font      
def textGenSmol(text):
    myFont=pygame.font.SysFont("Courier",20)
    return myFont.render(text,True,white)

#more efficent call using myFont to avoid emtivulous typing
def textGen(text):
    return myFont.render(text,True,white)

def textGenRed(text):
    return myFont.render(text,True,red)
    
#quicker way to update display  
def printOut() :
    pygame.display.update()
    
#quicker way to print to different parts of the screen using x axis as reference
    
def print30(text):
    screen.blit(text,(130,30))
    printOut()


def print60(text):
    screen.blit(text,(130,60))
    printOut()


def print90(text):
    screen.blit(text,(130,90))
    printOut()


def print120(text):
    screen.blit(text,(130,120))
    printOut()

#reset screen
def resetText():
    screen.blit(textBox,(100,000))
    
def resetAll():
    screen.blit(f1,(0,0))
    screen.blit(textBox,(100,000))
#fight prompt
def tussle():
    
    resetAll()
    enemyGen(3)
    textOut=textGen("AH! A TUSSLE IT IS THEN?")
    print30(textOut)
    textOut=textGen("GIRD YOUR LOINS FAM!")
    print60(textOut)
    stall()
    tussleOptions()
#options and results of fights for player
def tussleOptions():
    recoil=0
    resetText()
    textOut=textGen("CHOOSE AN ACTION!")
    print30(textOut)
    textOut=textGen("1) Rabbit punch")
    print60(textOut)
    textOut=textGen("2) A hardy shank")
    print90(textOut)
    textOut=textGen("3) Improv Zui Quan")
    print120(textOut)
    num=inputStall()
    #most powerful, has recoil damage
    if num == 1:
        resetText()
        textOut=textGenSmol("You go ham on the back of the enemy's neck ")
        print30(textOut)
        textOut=textGenSmol("with a wizard looking knifehand!")
        print60(textOut)
        textOut=textGenSmol("Damn bro, good form! Your metacarpal is taking ")
        print90(textOut)
        textOut=textGenSmol("recoil tho!")
        print120(textOut)
        stall()
        resetAll()
        enemyGen(4)
        #damage scales with defense
        damage=70-defense
        textOut=textGenRed("ENEMY TAKES "+str(damage)+" DAMAGE!")
        print30(textOut)
        stall()
        recoil=40-defense
        textOut=textGenRed("PLAYER TAKES " +str(recoil)+ " DAMAGE!")
        print60(textOut)
        stall()
    #weakest attack    
    if num == 2:
        resetText()
        textOut=textGenSmol("Oh boy! Out comes the handy dandy box cutter!")
        print30(textOut)
        textOut=textGenSmol("It finds slight purchase in the enemy's ")
        print60(textOut)
        textOut=textGenSmol("titatium frame!")
        print90(textOut)
        stall()
        resetAll()
        enemyGen(4)
        damage=40-defense
        textOut=textGenRed("ENEMY TAKES "+str(damage)+" DAMAGE!")
        print30(textOut)
        stall()
    #yup
    if num == 3:
        resetText()
        textOut=textGenSmol("You channel your inner chinese frat boy")
        print30(textOut)
        textOut=textGenSmol("and unleash a drunken barrage!")
        print60(textOut)
        stall()
        resetAll()
        enemyGen(4)
        damage=60-defense
        textOut=textGenRed("ENEMY TAKES "+str(damage)+" DAMAGE!")
        print30(textOut)
        stall()

                           
    #access enemyHP and update it so it displays correctly later    
    global enemyHP
    enemyHP-=damage

    
    if enemyHP<0:victory()
    
    #calculate ptoential recoil in same method as enemy damage calculation                       
    else: enemyAttack(recoil)
    
#standard enemy attack, resets screen and damage is proprtional to current attack
def enemyAttack(recoil):
    resetAll()
    enemyGen(3)
    textOut=textGen("The enemy hits that YEET!")
    print30(textOut)
    stall()
    global playerHP
    battleText="PLAYER TAKES "+str(attack)+" DAMAGE!" 
    textOut=textGenRed(battleText)
    print60(textOut)
    playerHP-=attack
    playerHP-=recoil
    if playerHP<0: failure()
    
#conversation prompt                           
def converse():
    resetText()
 
    textOut=myFont.render("What's poppin bro?",True,white)
    screen.blit(textOut,(130,30))
    textOut=myFont.render("How's the weather?",True,white)
    screen.blit(textOut,(130,50))
    pygame.display.update()
    printed=True
    stall()
    converseOptions()
    
#options and consequences    
def converseOptions():
    resetText()
    textOut=myFont.render("HOW DO WE RESPOND?",True,white)
    screen.blit(textOut,(130,30))
    textOut=myFont.render("1: Dreary",True,white)
    screen.blit(textOut,(130,60))
    textOut=myFont.render("2: Dreamy",True,white)
    screen.blit(textOut,(130,90))
    textOut=myFont.render("3: Delaware doesnt exist",True,white)
    screen.blit(textOut,(130,120))
    printOut()
    num=inputStall()
    if num==1:
        resetAll()
        enemyGen(3)
        textOut=myFont.render("'Poppycock!",True,white)
        screen.blit(textOut,(130,30))
        textOut=myFont.render("You liar! It's humid at worst!'",True,white)
        screen.blit(textOut,(130,60))
        printOut()
        stall()
        textOut=myFont.render("ENEMY'S ATTACK ROSE!",True,red)
        attack+=10
        screen.blit(textOut,(130,90))
        printOut()
        
    if num==2:
        resetText()
        textOut=textGenSmol("'...It is a lovely day for kites isnt it?'")
        print30(textOut)
        stall()
        textOut=textGenSmol("The enemy begins to reminisce!")
        print60(textOut)
        textOut=textGenSmol("They are enraptured in nostalgic memories ")
        print90(textOut)
        textOut=textGenSmol("of times gone by!")
        print120(textOut)
        stall()
        resetText()
        textOut=textGenRed("ENEMY'S ATTACK FELL!")
        global attack
        attack=attack-10
        print30(textOut)
        
    if num==3:
        resetText()
        textOut=textGenSmol("'What the fresh hell are you on about?'")
        print30(textOut)
        stall()
        textOut=textGenSmol("The enemy is peturbed by your answer!")
        print60(textOut)
        stall()
        global defense
        defense=defense-10
        
        textOut=textGenRed("ENEMY'S DEFENSE FELL")
        
        print90(textOut)
        
        
    
    
def flee():
   enemy= pygame.image.load('C:/Python34/finalProject/bye.png')
   resetAll()
   screen.blit(enemy,(300,325))
   textOut=myFont.render("I SAID FIGHT NOT FLIGHT FAM!",True,white)
   screen.blit(textOut,(130,30))
  

def actions():
    resetText()
    textOut=myFont.render("Choose your option kid!",True,white)
    screen.blit(textOut,(130,30))
    textOut=myFont.render("1: Kerfuffle",True,white)
    screen.blit(textOut,(130,60))
    textOut=myFont.render("2: Converse",True,white)
    screen.blit(textOut,(130,90))
    textOut=myFont.render("3: Skedaddle",True,white)
    screen.blit(textOut,(130,120))
    textOut=myFont.render("4: Inquire Within",True,white)
    screen.blit(textOut,(130,150))
    printOut()
    generated=True

#print current stats of enemy
def statusReport():
    resetText()
                           
    enemyHPPrint="Current enemy HP: "+str(getEnemyHP())
    textOut=textGen(enemyHPPrint)
    print30(textOut)
                           
    attackPrint="Current enemy attack: "+str(getAttack())
    textOut=textGen(attackPrint)
    print60(textOut)
                           
    defensePrint="Current enemy defense: "+str(getDefense())
    textOut=textGen(defensePrint)
    print90(textOut)
                           
    hpPrint="Player current HP: "+str(getHP())
    textOut=textGen(hpPrint)
    print120(textOut)
                        

#different sprites for enemy, activated depending on route   
def enemyGen(num):
    #default
    if num==1:
     enemy= pygame.image.load('C:/Python34/finalProject/enemy.png')
    #flee
    if num==2:
     enemy= pygame.image.load('C:/Python34/finalProject/bye.png')
    #engage
    if num==3:
     enemy= pygame.image.load('C:/Python34/finalProject/engage.png')
    #wounded
    if num==4:
     enemy= pygame.image.load('C:/Python34/finalProject/oof.png')
    #defeated
    if num==5:
     enemy= pygame.image.load('C:/Python34/finalProject/kurt.png')
    screen.blit(enemy,(300,325))
    printOut()
    
def victory():
    resetAll()
    enemyGen(5)
    textOut=textGenSmol("Oh snap, you broke off the armor!")
    print30(textOut)
    stall()
    textOut=textGenSmol("The enemy is exposed! How embarrasing!")
    print60(textOut)
    stall()
    resetAll()
    textOut=textGen("The enemy has skedaddled!")
    print30(textOut)
    stall()
    resetText()
    myFont=pygame.font.SysFont("Comic Sans",70)
    textOut=myFont.render("   A WINNER IS YOU!",True,green)
    screen.blit(textOut,(130,60))
    printOut()
    stall()
    time.sleep(1.1)
    pygame.quit()
    

def failure():
    resetAll()
    myFont=pygame.font.SysFont("Comic Sans",50)
    textOut=myFont.render("GAME OVER!",True,green)
    print30(textOut)
    stall()
    time.sleep(1.1)
    pygame.quit()
    
        
#print(keys)
#essentially acts as game engine, checks all the time for updates and the like
#also prevents unitnentonal repeats or overlaps with prinouts
crashed = False
#when set to true, will attack after conversing
#set to true when user chooses option 1
instigated=False
     
while not crashed:
   printed=False
   introComplete=False
   generated=False
   conversing1=False
   
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #start the game when user presses space
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                  if introComplete is not True: introComplete=True
                 
                             
        #generate enemy
        if introComplete:
           resetAll()
           screen.blit(enemy,(300,325))
           generated=True
          
           
        if generated and introComplete:
           
           actions()
           printOut()
        #input user action
           num=inputStall()
           print(num)
           if num == 0:
            print(num)
           elif num==4: statusReport()
           elif num==3:
                flee()
                crashed=True
           elif num==2:
              converse()
              if instigated:
                  stall()
                  enemyAttack(0)
           elif num==1:
               instigated=True
               tussle()
               
                  
        print(event)
       
    
         
         
   pygame.display.update()
   clock.tick(60)
if crashed:
   time.sleep(1.1)
   pygame.quit()

quit()
