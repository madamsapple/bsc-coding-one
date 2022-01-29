import random
import pygame
from pygame import display
import pygame.freetype

taskandtime = {
    "wake up" : str(random.randint(6,7)) + ":" + str(random.randint(0, 3)) + str(random.randint(0, 9)) + " AM",
    "breakfast" : "7:" + str(random.randint(45, 59)) + " AM",
    "rollcall" : "9:" + str(random.randint(45, 50)) + " AM",
    "escorting" : "9:" + str(random.randint(50,59)) or "10:" + str(random.randint(0, 1) + str(random.randint(0, 5))) + " AM",
    "lunch" : "1:" + str(random.randint(30, 45)) + " PM",
    "walkbyward" : "2:" + str(random.randint(15, 30)) + " PM",
    "phonecalls" : "2:" + str(random.randint(35, 45)) + " PM",
    "selfhelp" : "3:" + str(random.randint(15, 30)) + " PM",
    "relgmeet" : "4:" + ((str(random.randint(0,1)) + str(random.randint(0,5))) or ("0" + str(random.randint(6,9)))) + " PM",
    "exercise" : "5:00 PM",
    "cleaning" : "7:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,15)))) + " PM",
    "supper" : "7:" + str(random.randint(16, 30)) + " PM",
    "lightsout" : ("8:" + str(random.randint(30,59))) or ("9:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,30))))) + " PM"

}

pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Remember the Time...")
window = True

while window:
    #looping through all events happening in the game
    for event in pygame.event.get():

        #if event is a quit event (triggered by clicking the x button)
        if event.type == pygame.QUIT:

            #game stops running
            window = False

    

    #gamefont is an object which stores the font and text size
    gamefont = pygame.font.Font("LIQUIDISMPART2.ttf", 30)

    #render func shows text onscreen: 4 args - display surface, location on surface, text to print as string, (l,b,h) of text  
    text = gamefont.render("Remember the Time...", False, (255, 0, 0))
    
    screen.blit(text, (325, 250))

    pygame.display.update()

