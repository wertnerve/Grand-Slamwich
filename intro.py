import pygame

pygame.font.init()
myFont=pygame.font.SysFont("Courier",30)
#color templates
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

size=[800,800]
screen=pygame.display.set_mode(size)

textBox = pygame.image.load('C:/Python34/finalProject/finalProjectFrames/textbox.png')
screen.blit(textBox,(100,000))

def introScript():
    screen.blit(textBox,(100,000))                  
    textOut=myFont.render("Eureka!",True,white)
    screen.blit(textOut,(130,30))
