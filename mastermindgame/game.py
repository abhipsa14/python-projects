## Generate a 4 color random code
## Make the user to guess the code
## compare the guess
## tie the game together
import random
COLORS=['R','G','B','Y','O','P']
TRIES=10
CODE_LENGTH=4
def generate_code():
    code=[]

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code

def guess_code():
    while True:
        guess = input(f"Enter your guess ({CODE_LENGTH} colors from {', '.join(COLORS)}): ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"Please enter exactly {CODE_LENGTH} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color {color}. Please use only {', '.join(COLORS)}.")
                break
        else:
            break
    return guess

def check_guess(guess,code):
    color_counts={}
    correct_pos=0
    incorrect_pos=0
    for color in code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+=1
    
    for guess_color, real_color in zip(guess,code):
        if guess_color==real_color:
            correct_pos+=1
            color_counts[guess_color]-=1
        
    for guess_color, real_color in zip(guess,code):
        if guess_color in color_counts and color_counts[guess_color]>0:
            incorrect_pos+=1
            color_counts[guess_color]-=1
    return correct_pos, incorrect_pos


def play_game():
    code = generate_code()
    print("Welcome to the Mastermind Game!")
    print(f"You have {TRIES} tries to guess the code.")
    
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_guess(guess, code)
        if correct_pos == CODE_LENGTH:

            print(f"Congratulations! You've guessed the code in {attempt} attempts!")
            break
        print(f"Correct Position:{correct_pos}|Incorrect Position:{incorrect_pos}")
        
       
        
        print(f"Attempt {attempt + 1}: {correct_pos} colors in the correct position, {incorrect_pos} colors in the wrong position.")
    
    print(f"Sorry, you've used all your tries. The code was: {' '.join(code)}")

if __name__ == "__main__":
    play_game()
    # This allows the game to be run directly or imported without executing
    # the game logic immediately.