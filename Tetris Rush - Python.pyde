import random

NUM_ROWS = 20
NUM_COLS = 10
RESOLUTION = 4000
BOARD_WIDTH = RESOLUTION/NUM_ROWS
BOARD_HEIGHT = RESOLUTION/NUM_COLS
BLOCK_DIMENSION = 20

COLOUR_LIST = ["red", "blue", "green", "yellow", "purple", "white", "black"]
COLOUR_DICT = {"red": [255,51,52], "blue": [12,150,228], "green": [30,183,66], "yellow": [246,187,0], "purple": [76,0,153], "white": [255,255,255], "black": [0,0,0]}

class Block:
    def __init__(self, row, column):
        self.row = row*BLOCK_DIMENSION
        self.column = column*BLOCK_DIMENSION
        self.block_colour = COLOUR_LIST[random.randint(0,len(COLOUR_LIST)-1)]
        
    def display(self):
        
        strokeWeight(1)
        fill(COLOUR_DICT[str(self.block_colour)][0],COLOUR_DICT[str(self.block_colour)][1],COLOUR_DICT[str(self.block_colour)][2])
        rect(self.column,self.row,BLOCK_DIMENSION,BLOCK_DIMENSION)
              
class Game(list):
    
    def __init__(self):
        for r in range(NUM_ROWS):
            board_row = []
            for c in range(NUM_COLS):
                board_row.append(" ")
            self.append(board_row)
        self.key_handler = {RIGHT:False, LEFT:False}
        self.row = 0
        self.score = 0
        self.speed = 0
                
    def display(self):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                line(col*BLOCK_DIMENSION, row, col*BLOCK_DIMENSION, BOARD_HEIGHT)
                line(col, row*BLOCK_DIMENSION, BOARD_WIDTH, row*BLOCK_DIMENSION)

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if self[row][col] != " ":
                    self[row][col].display()
                else:
                    fill(210)
                    rect(col*BLOCK_DIMENSION, row*BLOCK_DIMENSION, BLOCK_DIMENSION,BLOCK_DIMENSION)
        
        # Printing the score
        
        fill(0)            
        textSize(15)
        text("Score : {}".format(self.score), 120, 20)
        
    def reset(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self[r][c] = " "
        self.key_handler = {RIGHT:False, LEFT:False}
        self.row = 0
        self.score = 0
        self.speed = 0
        
        self.game_run()

    # Initializing an instance of the block class in a random column
            
    def game_run(self):
        self.curr_col = random.randint(0,NUM_COLS-1)
        self.row = 0
        if self[0][self.curr_col] == " ": self[0][self.curr_col] = Block(0,self.curr_col)
        self.speed += 0.25
        
    # Dropping each block
    
    def drop_block(self):
    
        if not self.game_over():
            if self.row < 19 and self[self.row+1][self.curr_col] == " ":
                self[self.row+1][self.curr_col] = self[self.row][self.curr_col]
                self[self.row][self.curr_col] = " "
                self.row += 1
                self[self.row][self.curr_col].row = self.row*BLOCK_DIMENSION
            else:
                self.check_colour_match()
                game.game_run()
                
            self.display()
        else:
            textSize(20)
            text("Game Over!!!", 30, 180)
            text("Score : {}".format(self.score), 30, 200)
              
    # Moving the block right
    
    def move_block_right(self):
        
        if self.curr_col < NUM_COLS-1 and self[self.row][self.curr_col+1] == " ":
            self[self.row][self.curr_col+1] = self[self.row][self.curr_col]
            self[self.row][self.curr_col] = " "
            self.curr_col += 1
            self[self.row][self.curr_col].column = self.curr_col*BLOCK_DIMENSION
        else:
            pass
            
    # Moving the block left
        
    def move_block_left(self):
    
        if self.curr_col > 0 and self[self.row][self.curr_col-1] == " ":
            self[self.row][self.curr_col-1] = self[self.row][self.curr_col]
            self[self.row][self.curr_col] = " "
            self.curr_col -= 1
            self[self.row][self.curr_col].column = self.curr_col*BLOCK_DIMENSION 
        else:
            pass
    
    # Checking matching blocks
    
    def check_colour_match(self):
        
        if self.row < NUM_ROWS-3:
            if self[self.row][self.curr_col].block_colour == self[self.row+1][self.curr_col].block_colour == self[self.row+2][self.curr_col].block_colour == self[self.row+3][self.curr_col].block_colour:
                self[self.row][self.curr_col] = " "
                self[self.row+1][self.curr_col] = " "
                self[self.row+2][self.curr_col] = " "
                self[self.row+3][self.curr_col] = " "
                
                self.speed = 0
                self.score += 1

        # Checking for game over condition
        
    def game_over(self):
        if " " not in self[0]:
            #background(210)
            return True
        else:
            return False
     
game = Game()
game.game_run()

def setup():
    size(BOARD_WIDTH,BOARD_HEIGHT)
    background(210)
    stroke(180)
    fill(150)
    strokeWeight(0.3)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            line(col*BLOCK_DIMENSION, row, col*BLOCK_DIMENSION, BOARD_HEIGHT)
            line(col, row*BLOCK_DIMENSION, BOARD_WIDTH, row*BLOCK_DIMENSION)

def draw():
    #slow down the game by not calling the display() method every frame
    if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1:
        background(210)
        
        game.drop_block()
    
def keyPressed():
    if keyCode == RIGHT:
        game.move_block_right()
    elif keyCode == LEFT:
        game.move_block_left()
        
def mouseClicked():
    flag = game.game_over()
    if flag == True:
        game.reset()
        
