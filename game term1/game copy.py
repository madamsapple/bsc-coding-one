import random
import pygame,sys
from pygame import Surface, display
from pygame import surface
#from pygame.constants import K_BACKSPACE, MOUSEBUTTONDOWN
import pygame.freetype
#from button import Button

#put arrow for forward 
#opengameart.org
#arrows file
#establish conflict
#reduce font weight
#clearcode pygame gamestate code 
#clearcode pygame timer code
#relative path

#answer dict
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

answers = [ ["", ""], ["", ""], ["", ""] ]


class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = chrome

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = chrome
		#text
		self.text_surf = gui_font.render(text,True,black)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = vermillion
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					#print('click')
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = lime        

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


        txt = carbontype.render("Press    to play", False, black)
        screen.blit(txt, (328, 267))
        arrows = pygame.font.Font("Arrows ADF.ttf", 45)
        rightkey = arrows.render(" k", False, black)
        screen.blit(rightkey, (408, 259))
        
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.state = "frame1"

        """
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
        """ 
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
        screen.blit(f1txt4, (500, 457))
        two = carbontype.render("2", False, white)
        screen.blit(two, (588, 457))
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (610, 450))
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_2]:
            self.state = "frame2"

    def frame2(self):

        screen.fill(black)
        f2txt1 = carbontype.render("Prison life was meek.", False, white)
        screen.blit(f2txt1, (170, 250))

        f2txt2 = carbontype.render("Press", False, white)
        screen.blit(f2txt2, (500, 457))
        f2txt3 = carbontype.render("3", False, white)
        screen.blit(f2txt3, (586,458.5))
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (610, 450))

        pygame.display.update()
        
        if pygame.key.get_pressed()[pygame.K_3]:
            self.state = "frame3"

    def frame3(self):

        screen.fill(black)
        f3txt1 = carbontype.render("But these goons,", False, white)
        screen.blit(f3txt1, (210, 130))
        f3txt2 = carbontype.render("they still had wounds to heal.", False, white)
        screen.blit(f3txt2, (120, 170))
        f3txt4 = carbontype.render("Press", False, white)
        screen.blit(f3txt4, (500, 457))
        f3txt5 = carbontype.render("4", False, white)
        screen.blit(f3txt5, (586,458.5))
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (610, 450))
        pygame.display.update()
        
        f3txt3 = carbontype.render("They were still seeking retribution...", False, white)
        screen.blit(f3txt3, (65, 210))
        pygame.display.update()


        if pygame.key.get_pressed()[pygame.K_4]:
            self.state = "frame4"

    def frame4(self):

        screen.fill(black)
        f4txt1 = carbontype.render("For once, they finally found their nemesis.", False, white)
        screen.blit(f4txt1, (10, 130))
        f4txt2 = carbontype.render("And murdered him", False, white)
        screen.blit(f4txt2, (10, 170))
        f4txt3 = carbontype.render("within the prison's territories. Alas!", False, white)
        screen.blit(f4txt3, (10, 210))

        f4txt4 = carbontype.render("Yet danger crept up soon.", False, white)
        screen.blit(f4txt4, (10, 300))
        f4txt5 = carbontype.render("The police intervened.", False, white)
        screen.blit(f4txt5, (10, 340))
        f4txt6 = carbontype.render("They are now on the hunt for the murderers.", False, white)
        screen.blit(f4txt6, (10, 380))

        f4txt7 = carbontype.render("Press", False, white)
        screen.blit(f4txt7, (500, 457))
        f4txt8 = carbontype.render("5", False, white)
        screen.blit(f4txt8, (586,459))
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (610, 450))
        
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
        screen.blit(f5txt9, (500, 457))
        f5txt = carbontype.render("6", False, white)
        screen.blit(f5txt, (586,459))
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (610, 450))
        
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_6]:
            self.state = "inmates"

    def inmates(self):

        #timer always declared at the moment of a key press!!
        global timelol
        x = pygame.transform.scale(bricks, (650,500))
        #rect2 = button.get_rect()
        #rect2.center = (363, 290)
        screen.blit(x, (0,0))

        screen.blit(prisoner1, (60, 110))
        screen.blit(prisoner2, (370, 110))

        main1942 = pygame.font.Font("1942.ttf", 32)
        title = main1942.render("Now YOU will be the inmates.", False, white)
        screen.blit(title, (40, 60))
        txt1 = main1942.render("Inmate 1", False, white)
        screen.blit(txt1, (70, 280))
        txt2 = main1942.render("Inmate 2", False, white)
        screen.blit(txt2, (410, 280))

        txt3 = carbontype.render("A fake schedule of your prison routine will", False, white)
        screen.blit(txt3, (10, 330))
        txt3 = carbontype.render("be shown. It covers up the timing of the", False, white)
        screen.blit(txt3, (10, 360))
        txt3 = carbontype.render("murder. Memorize the timestamps to avoid", False, white)
        screen.blit(txt3, (10, 390))

        txt3 = carbontype.render("getting caught! Ready?", False, white)
        screen.blit(txt3, (10, 420))
        txt3 = carbontype.render("You have 11 seconds.", False, white)
        screen.blit(txt3, (10, 455))

        f5txt9 = carbontype.render("(GO!) Press", False, white)
        screen.blit(f5txt9, (432, 455))
        
        rightkey = arrows.render("k", False, white)
        screen.blit(rightkey, (600, 445))

        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
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
        screen.blit(countdown, (20,455))

        txt = carbontype.render("seconds passed", False, white)
        screen.blit(txt, (140, 460))
        pygame.display.update()

        global stoptime
        if ((current_time - timelol)/1000) >= 11.500:
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
        screen.blit(txt, (275, 250))
        pygame.display.update()

    def q1(self):
        
        carbontype = pygame.font.Font("carbontype.ttf", 23)
        x = pygame.transform.scale(bricks, (650,500))
        screen.blit(x, (0,0))
        scr2 = pygame.draw.rect(screen, white, (0,250,width,530))
        
        #question
        q1 = carbontype.render("When did you wake up?", False, white)
        screen.blit(q1, (150, 70))

        answer = taskandtime[0]
        answer = answer[10:] 
        option_b = str(random.randint(6,7)) + ":" + str(random.randint(0, 3)) + str(random.randint(0, 9)) + " AM"
        option_c = "7" + ":" + str(random.randint(0, 3)) + str(random.randint(0, 9)) + " AM"
        option_d = "6" + ":" + str(random.randint(0, 5)) + str(random.randint(0, 9)) + " AM"
        
        carbontype = pygame.font.Font("carbontype.ttf", 17)
        warning = carbontype.render("Click once on the button for your answer.", False, black)
        screen.blit(warning, (15, 460))

        carbontype = pygame.font.Font("carbontype.ttf", 23)

        #simple display of all options
        pygame.draw.rect(screen, orange, (160,123,130,45))
        a = carbontype.render(answer, False, white)
        screen.blit(a, (170, 133))
        letter_a = carbontype.render("a.", False, white)
        screen.blit(letter_a, (130,133))
        
        pygame.draw.rect(screen, orange, (360,123,130,45))
        b = carbontype.render(option_b, False, white)
        screen.blit(b, (370, 133))
        letter_b = carbontype.render("b.", False, white)
        screen.blit(letter_b, (330,133))

        pygame.draw.rect(screen, orange, (160,193,130,45))
        c = carbontype.render(option_c, False, white)
        screen.blit(c, (170, 203))
        letter_c = carbontype.render("c.", False, white)
        screen.blit(letter_c, (130,203))

        pygame.draw.rect(screen, orange, (360,193,130,45))
        d = carbontype.render(option_d, False, white)
        screen.blit(d, (370, 203))
        letter_d = carbontype.render("d.", False, white)
        screen.blit(letter_d, (330,203))

        inmate_1 = carbontype.render("Inmate 1: ", False, black)
        screen.blit(inmate_1, (90, 280))
        inmate_2 = carbontype.render("Inmate 2: ", False, black)
        screen.blit(inmate_2, (420, 280))

        #button class: Button(text, width, height, pos, elevation)
        player1_a = Button("a",75,40,(80,325),3)
        player1_b = Button("b",75,40,(170,325),3)
        player1_c = Button("c",75,40,(80,385),3)
        player1_d = Button("d",75,40,(170,385),3)

        player2_a = Button("a",75,40,(410,325),3)
        player2_b = Button("b",75,40,(500,325),3)
        player2_c = Button("c",75,40,(410,385),3)
        player2_d = Button("d",75,40,(500,385),3)

        
        x = True
        while x:
            for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                #   x = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    x = False
                    self.state = "q2"
                
	    
            player1_a.draw()
            player1_b.draw()
            player1_c.draw()
            player1_d.draw()

            player2_a.draw()
            player2_b.draw()
            player2_c.draw()
            player2_d.draw()

            if player1_a.pressed:
                #answer to the first question by the first player
                answers[0][0] = True
            if player1_b.pressed:
                #answer to the first question by the first player
                answers[0][0] = False
            if player1_c.pressed:
                #answer to the first question by the first player
                answers[0][0] = False
            if player1_d.pressed:
                #answer to the first question by the first player
                answers[0][0] = False

            if player2_a.pressed:
                #answer to the first question by the first player
                answers[0][1] = True
            if player2_b.pressed:
                #answer to the first question by the first player
                answers[0][1] = False
            if player2_c.pressed:
                #answer to the first question by the first player
                answers[0][1] = False
            if player2_d.pressed:
                #answer to the first question by the first player
                answers[0][1] = False
            
            if answers[0][0] != "" and answers[0][1] != "":
                carbontype = pygame.font.Font("carbontype.ttf", 19)
                locked = carbontype.render("Answers", False, red)
                screen.blit(locked, (280, 340))
                locked2 = carbontype.render("are locked.", False, red)
                screen.blit(locked2, (255, 365))

                carbontype = pygame.font.Font("carbontype.ttf", 17)
                next = carbontype.render("Press", False, black)
                screen.blit(next, (550, 460))
                arrows = pygame.font.Font("Arrows ADF.ttf", 40)
                rightkey = arrows.render("k", False, black)
                screen.blit(rightkey, (615, 452))

            
            pygame.display.update()

        
        """
        #box_1 = pygame.Rect((100,300),(200,100))

        #answer a
        #box_a = pygame.draw.rect(screen, orange, (130,213,130,45))
        #screen.blit(option_a, (140, 223))

        #answer b
        #(x,y,width,height)
        #box_b = pygame.draw.rect(screen, orange, (330,213,130,45))
        #screen.blit(option_b, (340, 223))

        #box_c = pygame.draw.rect(screen, orange, (130,283,130,45))
        #screen.blit(option_c, (140, 293))

        #box_d = pygame.draw.rect(screen, orange, (330,283,130,45))
        #screen.blit(option_d, (340, 293))
        input_1 = pygame.draw.rect(screen, black, (170,403,130,45))
        user_answer = user_text[1:]
        text_surface = carbontype.render(user_answer, False, orange)
        screen.blit(text_surface, (190, 410))

        if pygame.key.get_pressed()[pygame.K_a]:
            pygame.draw.rect(screen, red, (130,213,130,45), 3)           
        elif pygame.key.get_pressed()[pygame.K_b]:
            pygame.draw.rect(screen, red, (330,213,130,45), 3)
        elif pygame.key.get_pressed()[pygame.K_c]:
            pygame.draw.rect(screen, red, (130,313,130,45), 3)
        elif pygame.key.get_pressed()[pygame.K_d]:
            pygame.draw.rect(screen, red, (330,313,130,45), 3)

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
        """

    def q2(self):

        x = pygame.transform.scale(bricks, (650,500))
        screen.blit(x, (0,0))
        #"rollcall for work - 9:" + str(random.randint(45, 50)) + " AM"
        carbontype = pygame.font.Font("carbontype.ttf", 23)
        
        scr2 = pygame.draw.rect(screen, white, (0,250,width,530))
        
        #question
        q1 = carbontype.render("At what time did you go to work?", False, white)
        screen.blit(q1, (80, 70))

        answer = taskandtime[2]
        answer = answer[20:]
        
        option_a = "9:" + str(random.randint(20, 30)) + " AM"
        option_b = str(random.randint(8, 9)) + ":" + str(random.randint(31, 49)) + " AM"
        option_d = "8:" + str(random.randint(10, 19)) + " AM"
        
        #simple display of all options
        pygame.draw.rect(screen, orange, (160,123,130,45))
        a = carbontype.render(option_a, False, white)
        screen.blit(a, (170, 133))
        letter_a = carbontype.render("a.", False, white)
        screen.blit(letter_a, (130,133))
        
        pygame.draw.rect(screen, orange, (360,123,130,45))
        b = carbontype.render(option_b, False, white)
        screen.blit(b, (370, 133))
        letter_b = carbontype.render("b.", False, white)
        screen.blit(letter_b, (330,133))

        pygame.draw.rect(screen, orange, (160,193,130,45))
        c = carbontype.render(answer, False, white)
        screen.blit(c, (170, 203))
        letter_c = carbontype.render("c.", False, white)
        screen.blit(letter_c, (130,203))

        pygame.draw.rect(screen, orange, (360,193,130,45))
        d = carbontype.render(option_d, False, white)
        screen.blit(d, (370, 203))
        letter_d = carbontype.render("d.", False, white)
        screen.blit(letter_d, (330,203))

        inmate_1 = carbontype.render("Inmate 1: ", False, black)
        screen.blit(inmate_1, (90, 280))
        inmate_2 = carbontype.render("Inmate 2: ", False, black)
        screen.blit(inmate_2, (420, 280))

        #button class: Button(text, width, height, pos, elevation)
        player1_a = Button("a",75,40,(80,325),3)
        player1_b = Button("b",75,40,(170,325),3)
        player1_c = Button("c",75,40,(80,385),3)
        player1_d = Button("d",75,40,(170,385),3)

        player2_a = Button("a",75,40,(410,325),3)
        player2_b = Button("b",75,40,(500,325),3)
        player2_c = Button("c",75,40,(410,385),3)
        player2_d = Button("d",75,40,(500,385),3)

        x = True
        while x:
            for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                #   x = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed()[pygame.K_UP]:
                    x = False
                    self.state = "q3"
	    
            player1_a.draw()
            player1_b.draw()
            player1_c.draw()
            player1_d.draw()

            player2_a.draw()
            player2_b.draw()
            player2_c.draw()
            player2_d.draw()

            if player1_a.pressed:
                #answer to the first question by the first player
                answers[1][0] = False
            if player1_b.pressed:
                #answer to the first question by the first player
                answers[1][0] = False
            if player1_c.pressed:
                #answer to the first question by the first player
                answers[1][0] = True
            if player1_d.pressed:
                #answer to the first question by the first player
                answers[1][0] = False

            if player2_a.pressed:
                #answer to the first question by the first player
                answers[1][1] = False
            if player2_b.pressed:
                #answer to the first question by the first player
                answers[1][1] = False
            if player2_c.pressed:
                #answer to the first question by the first player
                answers[1][1] = True
            if player2_d.pressed:
                #answer to the first question by the first player
                answers[1][1] = False
            
            if answers[1][0] != "" and answers[1][1] != "":
                carbontype = pygame.font.Font("carbontype.ttf", 19)
                locked = carbontype.render("Answers", False, red)
                screen.blit(locked, (280, 340))
                locked2 = carbontype.render("are locked.", False, red)
                screen.blit(locked2, (255, 365))

                carbontype = pygame.font.Font("carbontype.ttf", 17)
                next = carbontype.render("Press", False, black)
                screen.blit(next, (550, 460))
                arrows = pygame.font.Font("Arrows ADF.ttf", 40)
                rightkey = arrows.render("q", False, black)
                screen.blit(rightkey, (615, 449))
            
            pygame.display.update()

    def q3(self):

        x = pygame.transform.scale(bricks, (650,500))
        screen.blit(x, (0,0))
        
        carbontype = pygame.font.Font("carbontype.ttf", 23)
        
        scr2 = pygame.draw.rect(screen, white, (0,250,width,530))
        
        #question
        q1 = carbontype.render("When did you attend phonecalls?", False, white)
        screen.blit(q1, (80, 70))

        answer = taskandtime[5]
        answer = answer[13:]
        option_b = "2:" + str(random.randint(45, 50)) + " PM"
        option_c = "2:" + str(random.randint(13, 29)) + " PM"
        option_a = "2:" + str(random.randint(30, 34)) + " PM"
        
        #simple display of all options
        pygame.draw.rect(screen, orange, (160,123,130,45))
        a = carbontype.render(option_a, False, white)
        screen.blit(a, (170, 133))
        letter_a = carbontype.render("a.", False, white)
        screen.blit(letter_a, (130,133))
        
        pygame.draw.rect(screen, orange, (360,123,130,45))
        b = carbontype.render(option_b, False, white)
        screen.blit(b, (370, 133))
        letter_b = carbontype.render("b.", False, white)
        screen.blit(letter_b, (330,133))

        pygame.draw.rect(screen, orange, (160,193,130,45))
        c = carbontype.render(option_c, False, white)
        screen.blit(c, (170, 203))
        letter_c = carbontype.render("c.", False, white)
        screen.blit(letter_c, (130,203))

        pygame.draw.rect(screen, orange, (360,193,130,45))
        d = carbontype.render(answer, False, white)
        screen.blit(d, (370, 203))
        letter_d = carbontype.render("d.", False, white)
        screen.blit(letter_d, (330,203))

        inmate_1 = carbontype.render("Inmate 1: ", False, black)
        screen.blit(inmate_1, (90, 280))
        inmate_2 = carbontype.render("Inmate 2: ", False, black)
        screen.blit(inmate_2, (420, 280))

        #button class: Button(text, width, height, pos, elevation)
        player1_a = Button("a",75,40,(80,325),3)
        player1_b = Button("b",75,40,(170,325),3)
        player1_c = Button("c",75,40,(80,385),3)
        player1_d = Button("d",75,40,(170,385),3)

        player2_a = Button("a",75,40,(410,325),3)
        player2_b = Button("b",75,40,(500,325),3)
        player2_c = Button("c",75,40,(410,385),3)
        player2_d = Button("d",75,40,(500,385),3)

        
        x = True
        while x:
            for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                #   x = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    x = False
                    self.state = "decision"
                    global mer
                    mer = pygame.time.get_ticks()
                
	    
            player1_a.draw()
            player1_b.draw()
            player1_c.draw()
            player1_d.draw()

            player2_a.draw()
            player2_b.draw()
            player2_c.draw()
            player2_d.draw()

            if player1_a.pressed:
                #answer to the first question by the first player
                answers[2][0] = False
            if player1_b.pressed:
                #answer to the first question by the first player
                answers[2][0] = False
            if player1_c.pressed:
                #answer to the first question by the first player
                answers[2][0] = False
            if player1_d.pressed:
                #answer to the first question by the first player
                answers[2][0] = True

            if player2_a.pressed:
                #answer to the first question by the first player
                answers[2][1] = False
            if player2_b.pressed:
                #answer to the first question by the first player
                answers[2][1] = False
            if player2_c.pressed:
                #answer to the first question by the first player
                answers[2][1] = False
            if player2_d.pressed:
                #answer to the first question by the first player
                answers[2][1] = True
            
            if answers[2][0] != "" and answers[2][1] != "":
                carbontype = pygame.font.Font("carbontype.ttf", 19)
                locked = carbontype.render("Answers", False, red)
                screen.blit(locked, (280, 340))
                locked2 = carbontype.render("are locked.", False, red)
                screen.blit(locked2, (255, 365))

                carbontype = pygame.font.Font("carbontype.ttf", 17)
                next = carbontype.render("Press", False, black)
                screen.blit(next, (550, 460))
                arrows = pygame.font.Font("Arrows ADF.ttf", 40)
                rightkey = arrows.render("k", False, black)
                screen.blit(rightkey, (615, 452))
            
            pygame.display.update()

    def decision(self):
        screen.fill(black)

        """
        print("current_ time: " + str(current_time))
        #mer is declared in the prev frame, during the event of switching with keys!
        print("mer time: " + str(mer))
        """

        if ((current_time - mer)/1000) >= 1.000:
            txt1 = carbontype.render("Hello.", False, white)
            screen.blit(txt1, (20, 80))

        if ((current_time - mer)/1000) >= 2.500:
            txt2 = carbontype.render("The interrogations are being surveyed", False, white)
            screen.blit(txt2, (20, 130))
                
        for i in range(1, 6, 1):
            if ((current_time - mer)/1000) >= (2.500 + i):
                txt = carbontype.render(".", False, white)
                screen.blit(txt, (560 + (10*i), 128))

        if ((current_time - mer)/1000) >= 7.000:
            txt3 = carbontype.render("Did any inmate lie?", False, white)
            screen.blit(txt3, (20, 240))

        if ((current_time - mer)/1000) >= 9.000:
            txt4 = carbontype.render("Well,", False, white)
            screen.blit(txt4, (20, 270))
        
        if ((current_time - mer)/1000) >= 10.500:
            txt5 = carbontype.render("the verdict is here.", False, white)
            screen.blit(txt5, (190, 330))
            
        if ((current_time - mer)/1000) >= 12.000:
            self.state = "endgame"
            #byebye! 'twas lovely making this game

        pygame.display.update()

        player1_score = 0
        player2_score = 0
        global tie
        tie = False
        global no_winner
        no_winner = False
        global winner
        winner = 0
        global loser
        loser = 0
        
        #calculating scores of both players
        for x in range(0,3):
            if answers[x][0] == True:
                player1_score += 1
        
        for x in range(0,3):
            if answers[x][1] == True:
                player2_score += 1

        #deciding win/loss/tie
        if ((player1_score == 3) and (player2_score == 3)):
            tie = True
        elif ((player1_score == 3) or (player2_score == 3)):
            if player1_score == 3:
                winner = "Inmate 1"
                loser = "Inmate 2"
            else:
                winner = "Inmate 2"
                loser = "Inmate 1"
        else:
            no_winner = True

        """
        print("answers: ", answers)
        print("no_winner: " + str(no_winner))
        print("tie: " + str(tie))
        print("winner: " + str(winner))
        print("loser: " + str(loser))
        """

    def endgame(self):

        """ """
        #if one player wins
        if winner != 0:

            main1942 = pygame.font.Font("1942.ttf", 41, bold = True)
            #x = pygame.transform.scale(bricks, (650,500))
            #screen.blit(x, (0,0))
            screen.fill(black)
        
            txt = main1942.render("You are", False, red)
            screen.blit(txt, (220, 135))
            txt3 = main1942.render(loser, False, vermillion)
            screen.blit(txt3, (220, 255))
            pygame.display.update()

            txt2 = main1942.render("sentenced to death:", False, red)
            screen.blit(txt2, (70, 190))

            txt4 = main1942.render(("{} wins.".format(winner)), False, red)
            screen.blit(txt4, (150, 400))

        #if both players win
        elif tie == True:
            main1942 = pygame.font.Font("1942.ttf", 39, bold = True)
            #x = pygame.transform.scale(bricks, (650,500))
            #screen.blit(x, (0,0))
            screen.fill(black)
            
            txt2 = main1942.render("You both win!", False, red)
            screen.blit(txt2, (170, 250))
            
            pygame.display.update()
            txt = main1942.render("No one got caught.", False, red)
            screen.blit(txt, (115, 190))

        #if both lose
        elif no_winner == True:
            main1942 = pygame.font.Font("1942.ttf", 39, bold = True)
            #x = pygame.transform.scale(bricks, (650,500))
            #screen.blit(x, (0,0))
            screen.fill(black)
            
            txt = main1942.render("You are BOTH suspected of", False, red)
            screen.blit(txt, (15, 170))
            txt3 = main1942.render("murder", False, red)
            screen.blit(txt3, (245, 215))
            
            pygame.display.update()
            txt2 = main1942.render("No one wins.", False, red)
            screen.blit(txt2, (180, 285))
        
        pygame.display.update()

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
        if self.state == "q2":
            self.q2()
        if self.state == "q3":
            self.q3()
        if self.state == "decision":
            self.decision()
        if self.state == "endgame":
            self.endgame()

                           
lime = (253,230,126)
vermillion = (230,53,37)
chrome = 209, 150, 0
black = (0,0,0)


#initializes all modules
pygame.init()
clock = pygame.time.Clock()

gui_font = pygame.font.Font("carbontype.ttf", 23)
#fonts loading
main1942 = pygame.font.Font("1942.ttf", 27, bold = True)
carbontype = pygame.font.Font("carbontype.ttf", 20)
arrows = pygame.font.Font("Arrows ADF.ttf", 40)

#colors
white = (255, 255, 255)
black = (0,0,0)
yellow = ((255,255,0))
red = ((255,0,0))
orange = ((255,100,10))

#images loading
bricks = pygame.image.load('brick.jpg')
unscaled1 = pygame.image.load('inmate1.png')
prisoner1 = pygame.transform.scale(unscaled1, (212,181.71))

unscaled2 = pygame.image.load("inmate2.png")
prisoner2 = pygame.transform.scale(unscaled2, (212,181.71))

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
            #pygame.quit()
            #sys.exit()  

    current_time = pygame.time.get_ticks()

    gamestate.state_manager()
    clock.tick(60)