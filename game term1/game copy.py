import random
import pygame
from pygame import Surface, display
from pygame import surface
from pygame.constants import K_BACKSPACE, MOUSEBUTTONDOWN
import pygame.freetype

#put arrow for forward 
#opengameart.org
#arrows file
#establish conflict
#reduce font weight
#clearcode pygame gamestate code 
#clearcode pygame timer code

taskandtime = {
    0 : "wake up - " + str(random.randint(6,7)) + ":" + str(random.randint(0, 3)) + str(random.randint(0, 9)) + " AM",
    1 : "breakfast - 7:" + str(random.randint(45, 59)) + " AM",
    2 : "rollcall for work - 9:" + str(random.randint(45, 50)) + " AM",
    3 : "escorting - 9:" + str(random.randint(50,59)) or "10:" + str(random.randint(0, 1) + str(random.randint(0, 5))) + " AM",
    4 : "lunch - 1:" + str(random.randint(30, 45)) + " PM",
    #"walkbyward" : "2:" + str(random.randint(15, 30)) + " PM",
    5 : "phonecalls - 2:" + str(random.randint(35, 45)) + " PM",
    #"selfhelp" : "3:" + str(random.randint(15, 30)) + " PM",
    #"relgmeet" : "4:" + ((str(random.randint(0,1)) + str(random.randint(0,5))) or ("0" + str(random.randint(6,9)))) + " PM",
    6 : "exercise - 4:00 PM",
    7 : "cleaning - 6:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,15)))) + " PM",
    8 : "dinner - 7:" + str(random.randint(16, 30)) + " PM",
    9 : "lights out - " + ("8:" + str(random.randint(30,59))) or ("9:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,30))))) + " PM"

}

#clearcode pygame gamestate code
class gamestates():
    
    def __init__(self):
        self.state = 'menu'

    def menu(self):

        ##
        #setup start screen
        ##
        scrcolor = (255, 255, 255)
        screen.fill(scrcolor)

        #render func shows text onscreen: 4 args - text to print as string, antialias(smooth text or no), RGB value  
        title = main1942.render("Remember the Time...", True, (195, 0, 0))
        screen.blit(title, (325, 230))

        #brick image bg for options presented below title
        button = pygame.transform.scale(bricks, (74,38))
        rect2 = button.get_rect()
        rect2.center = (363, 290)
        screen.blit(button, rect2)
        
        play = carbontype.render("Play", False, (255, 255, 255))
        screen.blit(play, (338, 277))

        for event in pygame.event.get():
            #if play button clicked on start window
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                #if mouse lies within 'play' box and is clicked:
                if ((326 <= x <= 400) and (271 <= y <= 309)):
                    self.state = "frame1"

        pygame.display.update()

    def frame1(self):
        screen.fill(black)
        bg = pygame.transform.scale(bricks, (313,190))
        #rect3 = bricks.get_rect(topleft = (0,0))
        screen.blit(bg, (165, 160))

        f1txt1 = carbontype.render("Once upon a time...", False, white)
        screen.blit(f1txt1, (185, 130))      
        f1txt2 = carbontype.render("there were two goons", False, white)
        screen.blit(f1txt2, (171, 355))
        f1txt3 = carbontype.render("locked in a prison.", False, white)
        screen.blit(f1txt3, (184, 380))
    
        f1txt4 = carbontype.render("Press", False, white)
        screen.blit(f1txt4, (510, 457))
        arrows = pygame.font.Font("Arrows ADF.ttf", 40)
        two = carbontype.render("2", False, white)
        screen.blit(two, (590, 450))
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_2]:
            self.state = "frame2"
        
        """    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if event.type == pygame.KEYUP:
                        self.state = "frame2" """

    def frame2(self):

        screen.fill(black)
        f2txt1 = carbontype.render("Prison life was meek.", False, white)
        screen.blit(f2txt1, (170, 250))

        f2txt2 = carbontype.render("Press", False, white)
        screen.blit(f2txt2, (510, 457))
        f2txt3 = carbontype.render("3", False, white)
        screen.blit(f2txt3, (592,470))

        pygame.display.update()
        
        if pygame.key.get_pressed()[pygame.K_3]:
            self.state = "frame3"

    def frame3(self):

        screen.fill(black)
        f3txt1 = carbontype.render("But these goons,", False, white)
        screen.blit(f3txt1, (180, 130))
        f3txt2 = carbontype.render("they still had wounds to heal.", False, white)
        screen.blit(f3txt2, (120, 170))
        f3txt4 = carbontype.render("Press", False, white)
        screen.blit(f3txt4, (510, 457))
        f3txt5 = carbontype.render("4", False, white)
        screen.blit(f3txt5, (592,470))
        pygame.display.update()
        
        f3txt3 = carbontype.render("They were still seeking retribution...", False, white)
        screen.blit(f3txt3, (96, 210))
        pygame.display.update()


        if pygame.key.get_pressed()[pygame.K_4]:
            self.state = "frame4"

    def frame4(self):

        screen.fill(black)
        f4txt1 = carbontype.render("For once, they finally found their nemesis.", False, white)
        screen.blit(f4txt1, (10, 150))
        f4txt2 = carbontype.render("And murdered him", False, white)
        screen.blit(f4txt2, (10, 190))
        f4txt3 = carbontype.render("within the prison's territories. Alas!", False, white)
        screen.blit(f4txt3, (10, 230))

        f4txt4 = carbontype.render("Yet danger crept up soon.", False, white)
        screen.blit(f4txt4, (10, 330))
        f4txt5 = carbontype.render("The police intervened.", False, white)
        screen.blit(f4txt5, (10, 370))
        f4txt6 = carbontype.render("They are now on the hunt for the murderers.", False, white)
        screen.blit(f4txt6, (10, 410))

        f4txt7 = carbontype.render("Press", False, white)
        screen.blit(f4txt7, (510, 457))
        f4txt8 = carbontype.render("5", False, white)
        screen.blit(f4txt8, (592,470))
        
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_5]:
            self.state = "frame5"

    def frame5(self):

        screen.fill(black)
        f5txt1 = carbontype.render("The police starts interrogating all inmates", False, white)
        screen.blit(f5txt1, (10, 110))
        f5txt2 = carbontype.render("about their prison routine", False, white)
        screen.blit(f5txt2, (10, 140))
        f5txt3 = carbontype.render("on the day of the crime.", False, white)
        screen.blit(f5txt3, (10, 170))
        f5txt4 = carbontype.render("Selfishly,", False, white)
        screen.blit(f5txt4, (10, 230))
        f5txt5 = carbontype.render("each goon tries not to get caught.", False, white)
        screen.blit(f5txt5, (10, 260))

        f5txt6 = carbontype.render("If their routine lines up", False, white)
        screen.blit(f5txt6, (10, 330))
        f5txt7 = carbontype.render("with the timing of the murder,", False, white)
        screen.blit(f5txt7, (10, 360))
        f5txt8 = carbontype.render("they are in trouble!", False, white)
        screen.blit(f5txt8, (10, 390))

        f5txt9 = carbontype.render("Press", False, white)
        screen.blit(f5txt9, (510, 457))
        f5txt = carbontype.render("6", False, white)
        screen.blit(f5txt, (592,470))
        
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_6]:
            self.state = "inmates"

    def inmates(self):

        global timelol
        x = pygame.transform.scale(bricks, (650,500))
        #rect2 = button.get_rect()
        #rect2.center = (363, 290)
        screen.blit(x, (0,0))

        screen.blit(prisoner, (20, 170))
        screen.blit(prisoner2, (360, 170))
        main1942 = pygame.font.Font("1942.ttf", 32, bold = True)
        txt = main1942.render("Inmate 1", False, white)
        screen.blit(txt, (60, 370))
        txt = main1942.render("Inmate 2", False, white)
        screen.blit(txt, (410, 370))
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_7]:
            self.state = "times"
            timelol = pygame.time.get_ticks()

    def times(self):
        
        screen.fill(black)
        x = 0
        for i in range(0, 10):
        
            y = carbontype.render(taskandtime.get(i), False, white)
            screen.blit(y, (195, 50 + x))
            
            x += 40
        countdown = main1942.render(str((current_time - timelol)/1000), True, white)
        screen.blit(countdown, (550,450))
        pygame.display.update()

        global stoptime
        if ((current_time - timelol)/1000) >= 2.500:
            stoptime = pygame.time.get_ticks()
            self.state = "stop"
        
    def stop(self):

        main1942 = pygame.font.Font("1942.ttf", 40, bold = True)
        carbontype = pygame.font.Font("carbontype.ttf", 30)

        screen.fill(black)
        txt = main1942.render("It's GONE!", False, white)
        screen.blit(txt, (200, 200))

        if ((current_time - stoptime)/1000) >= 2.600:
            txt2 = carbontype.render("Ready", False, white)
            screen.blit(txt2, (20,350))
        if ((current_time - stoptime)/1000) >= 3.600:
            txt3 = carbontype.render("to", False, white)
            screen.blit(txt3, (145, 350))
        if ((current_time - stoptime)/1000) >= 4.600:
            txt4 = carbontype.render("answer", False, white)
            screen.blit(txt4, (195, 350))
        if ((current_time - stoptime)/1000) >= 5.600:
            txt5 = carbontype.render("the", False, white)
            screen.blit(txt5, (335, 350))
        if ((current_time - stoptime)/1000) >= 6.600:
            txt6 = carbontype.render("questions", False, white)
            screen.blit(txt6, (410, 350))
        if ((current_time - stoptime)/1000) >= 8.000:
            txt7 = carbontype.render("?", False, white)
            screen.blit(txt7, (610, 350))
        if ((current_time - stoptime)/1000) >= 9.000:
            txt8 = carbontype.render("Y/N", False, white)
            screen.blit(txt8, (290, 430))
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_y]:
            self.state = "q1"
        elif pygame.key.get_pressed()[pygame.K_n]:
            self.state = "bye"
            
    def bye(self):
        screen.fill(black)
        txt = carbontype.render("byebye.", True, white)
        screen.blit(txt, (300, 250))
        pygame.display.update()

    def q1(self):
        screen.fill(white)
        x = pygame.transform.scale(bricks, (650,500))
        screen.blit(x, (0,0))

        color = 232, 147, 98
        active_color = False

        input = ""

        #question

        box_1 = pygame.Rect((100,300),(200,100))
        
        for game_event in pygame.event.get():
            if game_event.type == pygame.MOUSEBUTTONDOWN:

                if box_1.collidepoint(pygame.mouse.get_pos()):
                    active_color = True

            if game_event.type == pygame.KEYDOWN:
                if game_event.key == K_BACKSPACE:
                    if len(input) > 0:
                        input = input[:-1]
                else:
                    input += game_event.unicode

            box_text = carbontype.render(input, True, white)
            screen.blit(box_text, (box_1.x + 5, box_1.y + 5))
            pygame.display.flip()

        if active_color == True:
            color = 255, 60, 0

        pygame.draw.rect(screen, (color), box_1)
        #box_text = carbontype.render(input, True, white)
        #screen.blit(box_text, (box_1.x + 5, box_1.y + 5))
        pygame.display.flip()

    def state_manager(self):
        if self.state == "menu":
            self.menu()
        if self.state == "frame1":
            self.frame1()
        if self.state == "frame2":
            self.frame2()
        if self.state == "frame3":
            self.frame3()
        if self.state == "frame4":
            self.frame4()
        if self.state == "frame5":
            self.frame5()
        if self.state == "inmates":
            self.inmates()
        if self.state == "times":
            self.times()
        if self.state == "stop":
            self.stop()
        if self.state == "bye":
            self.bye()
        if self.state == "q1":
            self.q1()


#initializes all modules
pygame.init()
clock = pygame.time.Clock()

#fonts loading
main1942 = pygame.font.Font("1942.ttf", 27, bold = True)
carbontype = pygame.font.Font("carbontype.ttf", 20)
arrows = pygame.font.Font("Arrows ADF.ttf", 20)

#colors
white = (255, 255, 255)
black = (0,0,0)

#images loading
bricks = pygame.image.load('brick.jpg')
prisoner = pygame.image.load('prisoner.png')
prisoner2 = pygame.image.load('prisoner2.jpg')

gamestate = gamestates()

#sets the initial/opening window
width = 650
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Remember the Time...")

window = True
while window:

    #looping through all events happening in the game
    for event in pygame.event.get():

        #if event is a quit event (triggered by clicking the x button)
        if event.type == pygame.QUIT:
            #game stops running
            window = False

    current_time = pygame.time.get_ticks()


    gamestate.state_manager()
    #clock.tick(60)        
     

"""

    #dict storing gamestates
        dict = { 1: "Menu", 2: "frame1", 3: "frame2", 4: "frame3" }

        #GAME STATES
        Menu = True
        Frame1 = False
        Frame2 = False
        Frame3 = False
        Frame4 = False
        Frame5 = False
        Frame6 = False

    if Frame1:

        if event.type == pygame.USEREVENT:
            counter += 1

        screen.fill(black)

        bg = pygame.transform.scale(bricks, (313,190))
        #rect3 = bricks.get_rect(topleft = (0,0))
        screen.blit(bg, (165, 160))

        f1txt1 = carbontype.render("Once upon a time...", False, white)
        screen.blit(f1txt1, (185, 130))

        #delayed printing of text using "counter" timer
        if counter >= 23:
            f1txt2 = carbontype.render("there were two goons", False, white)
            screen.blit(f1txt2, (171, 355))

        #counter needs to be (>=) not just (==) or text will only flash for that second/moment
        if counter >= 34.5:
            f1txt3 = carbontype.render("locked in a prison.", False, white)
            screen.blit(f1txt3, (184, 380))
        
        if counter >= 35.5:
            f1txt4 = carbontype.render("Press", False, white)
            screen.blit(f1txt4, (510, 457))
            arrows = pygame.font.Font("Arrows ADF.ttf", 40)
            rightkey = arrows.render("k", False, white)
            screen.blit(rightkey, (590, 450))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Frame1 = False
                    Frame2 = True
                    x = counter


    if Frame2:
        if event.type == pygame.USEREVENT:
            counter += 1

        setup = True
        keypress = False

        if setup:
            screen.fill(black)
            f2txt1 = carbontype.render("Prison life was meek.", False, white)
            screen.blit(f2txt1, (170, 250))
            print(counter)
            if counter == x + 15:
                keypress = True

        
        #figured out feature to move between frames during storyline!!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Frame1 = True
                Frame2 = False

        if keypress:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Frame2 = False
                    Frame3 = True
              

    if Frame3:

        screen.fill(black)

        f3txt1 = carbontype.render("But these goons,", False, white)
        screen.blit(f3txt1, (180, 250))

        f3txt2 = carbontype.render("they still had wounds to heal.", False, white)
        screen.blit(f3txt2, (150, 290))
"""