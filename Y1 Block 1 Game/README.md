SUMMARY
This is an executable version of the game. Just run "Remthetime.exe" under the folder "exe.macosx-10.9-universal2-3.10" to start playing!
 
General Instructions: This is a 2-player game (no computer opponent). Make sure you have a working keyboard and mouse/touchpad. Turn up your volume just enough - there’s music in the game!

This game is called “Remember the Time”. Two players act as two inmates in a prison. They recently committed a murder in secret within the prison. But the police found out, and are now conducting trial sessions to find out the perpetrators. Each inmate/murderer tries not to get caught and just save themself.

In order to cover up the exact timing of the murder and the events taking place around it, a fake schedule is devised. A series of false timestamps detailing what you did and at what time will be shown. They will differ from the actual times you did those tasks, for example:

When were you escorted for work?
When did you clean the communal showers?
When did you do phone calls?
Etc.

Both players must remember these timestamps to cover up the murder’s timing, dodge any accusations, and save oneself. Questions will be presented to both players, asking what time they did certain tasks. All answers will be recorded. In the end, if either player messes up the time, they will be sentenced to death!


DEVELOPMENT

I wrote in my notes, around 10th Nov, how I wanted my game to be mystery-themed or giving a sense of thrill when someone plays it. I cannot vouch for how much of those ambitions actually exhibited in the present game, and if they did to what extent, but I hope it offers some level of engagement. I decided to keep it simple in idea and not aim for something too demanding.

I chose to code my game in pygame since I liked that it offered a greater amount of creative freedom - in graphics, mechanics, and various other aspects. Moreover, making a terminal-based game or using the Turtle module felt slightly less challenging with how many new concepts I could learn or getting to practice untouched topics. In retrospect, Pygame’s object-oriented approach certainly helped me become more familiar with this entirely new way of coding, which was otherwise hard to grasp having done procedural all along.

Initially, I simply created a dictionary in my program storing the timestamps of the inmates’ tasks. To avoid hardcoding, I used the random function to generate new answers every run of the game. Then came learning pygame and understanding its basics for the first time. I wanted to make sure I got a hang of the fundamentals such as displaying a screen, text, drawing objects, images, etc. before I began designing things. I watched this incredibly long introduction to pygame by ClearCode and started setting things up.

It was mostly a learn-as-you-go approach that I adopted throughout my time coding - if I wanted to have a white background on my menu, I looked up how display screens work and how you can color them; if I wanted to change the display if someone clicked on a text box, I got to know about mouse click detections, and so on. There were a lot of pre-made solutions defining a whole part of the game in code, and it was pretty tempting to look them up, but I tried avoiding that and building elements from scratch. This also meant having a lot of trial and error while playing around with your code, like seeing what happens when you manipulate some value or change the organization of the code.

I was insistent on having a storyline for my game so my first process was simply writing the scripts and displaying them before the actual gameplay.

Notable challenges were switching through game states, identifying players’ answers to the question in the interface and then registering them in your internal code for further use, and figuring out/working with event loops in general.

Game States: I still have to understand how events work with key presses and mouse clicks and how to handle them. When I was using the right arrow key to move forward in the game, it would just skip all the states and arrive at the last one. As a result, I had to use different keys for switching, to avoid skips all the while the key was pressed where you would end up moving through all the game states. On a side note, my initial design of game states was based on manipulating variables between true and false, triggering the display of the frames I wanted. But it was pretty bad design and it wasn’t an object- oriented approach either. I then took help from ClearCode’s video tutorial on how different states can be set up using different methods in one class: this became my basis for creating/moving through new game states. It was much more dynamic.

Registering answers: I spent a lot of time figuring out how to save the players’ answers. Should I create a text box where they can type in? Or one where they simply click on the boxes of the answers provided? And then how do I differentiate between the first and the second player’s answers? I looked up various guides on how text boxes are implemented, but it gave rise to endless complications in my code. The event handling of typing letters was not functional since multiple event loops affected each other while running. I sadly gave up and then decided to see button-click functions, if any. Once again, I referred to ClearCode and they had a tutorial on how to set up a button click.

I used their code but had to experiment and mold their Button class a lot to fit it in with my game’s scenario. This entailed omitting certain code and methods, changing statements here and there, and placing it in the game’s specific functionality.

Graphically, the game is sort of old fashioned and rudimentary in style. I thought it blended with the game’s rough themes of prison cells, murders, and gothic text, etc. Consequently, I used a typewriter font (like it is used in official documents in governments, law). Pixel art is very popular in retro games and looks very exciting to the eye, but I knew this game was adopting a different approach in that sense.

Hopefully you’ll like the game - have fun!


CREDITS

Code for implementing game states in pygame: https://www.youtube.com/watch?v=j9yMFG3D7fg

Using a timer in pygame: https://www.youtube.com/watch?v=YOCt8nsQqEo

Creating a button in pygame: https://www.youtube.com/watch?v=8SzTzvrWaAA

Background music: https://www.youtube.com/watch?v=s0266OK1Haw
