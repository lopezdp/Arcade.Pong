# Implementation of classic arcade game Pong
#Must be played in CodeSkulptor. See Link below
#http://www.codeskulptor.org/#user23_vprgYUXQ2x_16.py
import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):    
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [0,0]
    
    #Play around with these inverse functions to make sure they are correct 
    #respawn & go LEFT/RIGHT
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2,4)
        ball_vel[1] = (random.randrange(1,3)) * -1
        return direction    
    else:
        ball_vel[0] = (random.randrange(2,4)) * -1
        ball_vel[1] = (random.randrange(1,3)) * -1
        return direction  
   
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers    
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    
    # update only the [1] position
    paddle1_pos = [[WIDTH - HALF_PAD_WIDTH, (HEIGHT/2) - HALF_PAD_HEIGHT], #(x,y) top
                   [WIDTH - HALF_PAD_WIDTH, (HEIGHT/2) + HALF_PAD_HEIGHT]] #(x,y) bottom
    
    paddle2_pos = [[0 + HALF_PAD_WIDTH, (HEIGHT/2) - HALF_PAD_HEIGHT], #(x,y) top
                   [0 + HALF_PAD_WIDTH, (HEIGHT/2) + HALF_PAD_HEIGHT]] #(x,y) bottom
    
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
     
    spawn_ball(random.choice([LEFT,RIGHT])) 
        
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel   
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")  
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
 # if ball hits either left/right gutter then the ball will respawn
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        paddle1 = paddle1_pos[0][1]
        paddle2 = paddle2_pos[0][1]
        if (paddle1 + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle1 - HALF_PAD_HEIGHT): #it hits the paddle, bounce
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(random.choice([LEFT,RIGHT]))
            
    if ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        paddle1 = paddle1_pos[0][1]
        paddle2 = paddle2_pos[0][1]
        
        if (paddle2 + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle2 - HALF_PAD_HEIGHT): #it hits the paddle, bounce
            ball_vel[0] = -ball_vel[0]
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball(random.choice([LEFT,RIGHT]))
       
    # this is what will make ball bounce off top/bottom    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]*1.1  
                        
    # draw ball
    c.draw_circle([ball_pos[0],ball_pos[1]], BALL_RADIUS, 10, 'Green', 'Orange')
        
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0][1] > HEIGHT - PAD_HEIGHT:
        paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1][1] = HEIGHT 
        paddle1_pos[0][1] = paddle1_pos[0][1] + (paddle1_vel[1] * -1)
        paddle1_pos[1][1] = paddle1_pos[1][1] + (paddle1_vel[1] * -1)
        
    elif paddle1_pos[0][1] < 0:
        paddle1_pos[0][1] = 0
        paddle1_pos[1][1] = PAD_HEIGHT 
        paddle1_pos[0][1] = paddle1_pos[0][1] + (paddle1_vel[1] * -1)
        paddle1_pos[1][1] = paddle1_pos[1][1] + (paddle1_vel[1] * -1)        
                
    else:
        paddle1_pos[0][1] += paddle1_vel[1]
        paddle1_pos[1][1] += paddle1_vel[1]   
        
    if paddle2_pos[0][1] > HEIGHT - PAD_HEIGHT:
        paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1][1] = HEIGHT 
        paddle2_pos[0][1] = paddle2_pos[0][1] + (paddle2_vel[1] * -1)
        paddle2_pos[1][1] = paddle2_pos[1][1] + (paddle2_vel[1] * -1)
        
    elif paddle2_pos[0][1] < 0:
        paddle2_pos[0][1] = 0
        paddle2_pos[1][1] = PAD_HEIGHT 
        paddle2_pos[0][1] = paddle2_pos[0][1] + (paddle2_vel[1] * -1)
        paddle2_pos[1][1] = paddle2_pos[1][1] + (paddle2_vel[1] * -1)        
                
    else:
        paddle2_pos[0][1] += paddle2_vel[1]
        paddle2_pos[1][1] += paddle2_vel[1]  
        
    # draw paddles
    c.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, 'Red')
    c.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, 'Yellow')
    
    # draw scores
    c.draw_text(str(score1), [150, 100], 30, "Red")
    c.draw_text(str(score2), [450, 100], 30, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel[1] -= acc
        
    if key == simplegui.KEY_MAP['s']:
        paddle2_vel[1] += acc
        
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel[1] -= acc
        
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel[1] += acc        
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel[1] = acc
        
    if key == simplegui.KEY_MAP['s']:
        paddle2_vel[1] = acc
        
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel[1] = acc
        
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel[1] = acc        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
