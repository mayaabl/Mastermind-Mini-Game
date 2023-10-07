import random

colors= ["R", "G", "B", "Y", "W", "O"]
tries=10
code_length=3

#a function for generating a code

def generate_code():
    code=[]
    
    for i in range(code_length):
        color= random.choice(colors)
        code.append(color)
        
    return code

code= generate_code()

#a function for guessing the code

def guess_code():
    
    while True:
        
        guess= input("Guess: ").upper().split(" ")
        
        if len(guess)!= code_length:
            print(f"you must guess {code_length} colors.")
            continue
        
        for color in guess:
            if color not in colors:
                print(f" Wrong color: {color}. Try Again.")
                break
            
        else:
            break
        
    return guess

# a function to check how many correct guesses are there
def check_code(guess, real_code):
    color_counts = {} #nb of colors in the real code
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+=1
        
    for guess_color, real_color in zip(guess, real_code): #zip for easier comparison
        if guess_color ==real_color:
            correct_pos+=1
            color_counts[guess_color]-=1
            
            
    for guess_color, real_color in zip(guess, real_code): #zip for easier comparison
        if guess_color in color_counts and color_counts[guess_color]>0:
            incorrect_pos+=1
            color_counts[guess_color]-=1
            
    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to Mastermind, you have {tries} to guess the code...")
    print("The valid colors are", colors )
    code=generate_code()
    for attempt in range(1, tries+1):
        guess= guess_code()
        correct_pos, incorrect_pos= check_code(guess, code)
        
        if correct_pos==code_length:
            print(f"You guessed the code in {attempt} tries!")
            break
            
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("You ran out of tries, the code was:", code)
        
        
if __name__ =="__main__": #directly running the python file
    game()
        