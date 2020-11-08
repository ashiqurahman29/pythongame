import pygame, sys , random  #importing library to develop game. Sys used to close the game application.
#

def position_restart(): # this function allows the ball to reset once it goes behind the player or rival.
    global ball_speed_x, ball_speed_y # defined variable outside the function for ball speed , known as global variable.
    game_ball.center = (box_ui_width/2, box_ui_height/2) # This code helps the ball stay in the middle.
    ball_speed_x *= random.choice((1,-1)) # controlling the speed of the ball.
    ball_speed_y *= random.choice((1,-1)) # controlling the speed of the ball.
    
""" This code moves the opponent without human input """
def ai_code(): # This function allows player to play with the opponent without any human input
    # if the ball is moving towards the rival, it can track the ball position and change its position according to the event.
    if rival.top < game_ball.y: 
        rival.top += rival_speed # course of the rival paddle speed increases.
    if rival.bottom >game_ball.y: 
        rival.bottom -= rival_speed # course of the rival paddle speed decreases.
    #this section of the code ensures the rival paddle stays within the game at a steady speed by not going too high/low.
    if rival.top <= 0: #stops it going too high .
        rival.top = 0 #once reaches the edge the character cannot go anymore up when going near top of the edge.
    if rival.bottom>=box_ui_height: # this code ensures the rival paddle cannot go outside of the screen.
        rival.bottom = box_ui_height #stops the rival paddle going outside of the edge. 
"""This code ensures the character moves and does not go outside the box """
def moving_character(): # this function ensures the player does not move outside the window.
    character.y += character_move #controlling the character.
    if character.top <= 0: # stops it from moving very high.
        character.top = 0 # stops it from moving very high and speed goes to zero even if the character presses the up key.
    if character.bottom >= box_ui_height: # blocks character going outside the game box and ensures it does not go too slow.
        character.bottom = box_ui_height# blocks character going outside the game box and ensures it does not go too slow.

"""This code creates the animation of ball moving in the game  """
def ball_animation(): # Function to create ball animation 
    global ball_speed_x, ball_speed_y, character_score, rival_score # calling global variables.
    game_ball.x += ball_speed_x # aids us in tracking the ball and controlling the ball.
    game_ball.y += ball_speed_y # aids us in tracking the ball and controlling the ball.
    # This section of the code is an advance way to track what our ball is doing in the game and control its action.
    if game_ball.top <= 0 or game_ball.bottom >= box_ui_height: 
        ball_speed_y *= -1 # change speed when ball touches a surface such as the Screen height.
    #tracking ball left movement 
    if game_ball.left <= 0: #ball goes behind rival it will score. 
        character_score += 1 # Adds points for the character.
        position_restart()# Puts the ball back to the start the position.
    
    if game_ball.right >= box_ui_width: # This code ensures if the ball goes past the character width the ball will reset.
        position_restart() # This code puts the ball position back to middle once the ball goes outside of the game.
        rival_score += 1 # This adds the score to the rivel player as the ball was missed by the player.
    """This is the ball collison to check if the ball hit the charcater"""
    if game_ball.colliderect(character) and ball_speed_x > 0: # This section checks ball collision characeter (you)
        if abs(game_ball.right - character.left) < 10: # This code tells what the progrm to do if the ball hits the characeter 
            ball_speed_x *= -1 # the value of ball speed is changed. 
        elif abs(game_ball.bottom - character.top) < 10 and ball_speed_y > 0:#This code tells what the progrm to do if the ball hits the characeter 
            ball_speed_y *= -1 #changes the vaule of the ball speed due to interacting with the character 
        elif abs(game_ball.top - character.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1 #changes the vaule of the ball speed due to interacting with the character 


    """This is an if statment to check ball collison with the paddle and bounces the ball back. """
    if game_ball.colliderect(rival) and ball_speed_x < 0: #This section checks ball collision of rival 
        #Here it will check when the ball hits the rival paddle and bounces back. 
        if abs(game_ball.left - rival.right) < 10: #This code tells what the progrm to do if the ball hits the rival 
            ball_speed_x *= -1 # 
        elif abs(game_ball.bottom - rival.top) < 10 and ball_speed_y > 0: #ball bounce
            ball_speed_y *= -1 #
        elif abs(game_ball.top - rival.bottom) < 10 and ball_speed_y < 0: #ball bounce
            ball_speed_y *= -1#



pygame.init() #activates module in python.
clock = pygame.time.Clock() #this code tracks the time in my game.
""" Screen Size for the game."""
box_ui_width = 1280# This is the  size of Screen width.
box_ui_height = 960# This is the size of Screen height.
"""Box Screen and Game Rave """
box_screen = pygame.display.set_mode((box_ui_width,box_ui_height)) # This code adds the width and height we set above to create the game box.
pygame.display.set_caption('Game Rave')# This will display our game name in th form.

"""Shapes and Variables"""
game_ball = pygame.Rect(box_ui_width/2 - 14,box_ui_height/2 - 15,30,30) # This code creates the size and shape of the ball in the game 
character = pygame.Rect(box_ui_width - 20,box_ui_height/2 - 70,10,140) # This code creates the size and shape of the character in the game.
rival = pygame.Rect(10, box_ui_height/2 - 70, 10, 140 ) # This code creates the size and shape of the rival player in the game 
#Global Variables that we can later use in our code.
ball_speed_x = 7 *random.choice((1,-1)) # setting the ball X-axis speed to a random places within our game application 
ball_speed_y = 7 *random.choice((1,-1))# settng the ball y-axis speed to a random places within our game application 
rival_speed = 7 # setting opponent speed at 7
character_move = 0 # character movement set as 0 to control its location. 


"""Background colour and paint"""
ui_background = pygame.Color('grey12') # This sets the background color of our game 
paint = (255,00,00) # this is the Red color that is set for the ball , character , rival and score.
"""Variables"""
character_score = 0 # Setting character score as 0 to start with.
rival_score = 0 # Setting the rival score as 0 to start with.
font_1 = pygame.font.Font("freesansbold.ttf",32) # Creating the score label font.
font_paint= (255,00,00) # Setting up the font as red.
"""Score render function to aid in building the score system"""
def score_render(): # This function is used to create the score board in the game.
    scorelbl = font_1.render(f"{character_score}",False,font_paint) # Creates the score board.
    box_screen.blit(scorelbl,(660,470)) # location of character score which is in the middle of the line.

    scorelbl2 = font_1.render(f"{rival_score}",False,font_paint) # this is the same code for the character , just replaced it with rival.
    box_screen.blit(scorelbl2,(600,470)) # this puts the score on the left and a space between the character score
    




# This is the main game loop that handles all our animmation , characters , movement and etc.
while True: # this loop checks if the user pressed any keyboard and what to do when they press it.
    for event in pygame.event.get(): # Checks user key input
        if event.type == pygame.QUIT: # If the quit or exist button is pressed it wil quiet the game 
            pygame.quit() # stops everything associated with pygame 
            sys.exit() # closes the entire program.
        if event.type == pygame.KEYDOWN: # 
            if event.key == pygame.K_DOWN: # If the key down button is pressed the character will move
                character_move +=7 # changes the location and movement of the character paddle.
            if event.key == pygame.K_UP: # If the key up is pressed , the character will move.
                character_move -=7 # changes the location and movement of the character paddle.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN: #Key down 
                character_move -=7 #s changes the location and movement of the character paddle 
            if event.key == pygame.K_UP:# Key up
                character_move +=7#changes the location and movement of the character paddle.

    # Calling all these function below in the main loop
    moving_character()# character paddle moving up/down
    ai_code()# bot 
    ball_animation() #ball animation 
    
    """This section of the code below are where the game draws our in-game character """
    box_screen.fill(ui_background)# This allows you to set the background to the colour grey.
    pygame.draw.rect(box_screen,paint, character)#This draws the character player in our game box and paints it in red.
    pygame.draw.rect(box_screen,paint, rival)# this draws the opponent player in the game with the color red.
    pygame.draw.ellipse(box_screen, paint, game_ball) # draws the ball and paints in red.
    pygame.draw.aaline(box_screen, paint, (box_ui_width/2,0), (box_ui_width/2,box_ui_height))# creates a straight line in middle of our gam
    
    score_render()# Calling the function to render game score within the midde of the game. 

    
    


    pygame.display.flip() # foward everything in loop to be drawned in the user screen.
    clock.tick(60)# Controls the loop to run 60 second. 