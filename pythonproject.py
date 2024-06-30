import datetime
from words import words
import string
import random
import calendar
import pygame as pg
import math

def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')   


def snakegame():
    window_size = 800
    tilesize = 50
    range_x = (tilesize, window_size - tilesize, tilesize)
    range_y = (tilesize, window_size - tilesize, tilesize)
    pos = lambda: [random.randrange(*range_x), random.randrange(*range_y)]
    snake = pg.Rect(pos() + [tilesize - 2, tilesize - 2])
    snake_center = pos()
    snake_direction = (0, 0)
    snake_length = 1
    segments = [snake.copy()]
    def generate_food():
        while True:
            food_position = pg.Rect(pos() + [tilesize - 2, tilesize - 2])
            if not snake.colliderect(food_position):
                return food_position
    food = generate_food()
    screen = pg.display.set_mode([window_size] * 2)
    clock = pg.time.Clock()
    timestep = 200
    dirs = {pg.K_w: (0, -tilesize), pg.K_s: (0, tilesize), pg.K_a: (-tilesize, 0), pg.K_d: (tilesize, 0)}
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key in dirs:
                    snake_direction = dirs[event.key]
                elif event.key == pg.K_q:  # Check if 'Q' key is pressed
                    pg.quit()
                    exit()    
        screen.fill((0, 0, 0))
        self_eat = snake.collidelist(segments[:-1]) != -1
        if snake.left < 0 or snake.right > window_size or snake.top < 0 or snake.bottom > window_size or self_eat:
            snake.center = pos()
            food.center = generate_food().center  # Regenerate food position
            snake_length = 1
            segments = [snake.copy()]
        if snake.colliderect(food):
            snake_length += 1
            food.center = generate_food().center  # Regenerate food position
        segments.insert(0, snake.copy())
        if len(segments) > snake_length:
            segments.pop()
        snake.move_ip(snake_direction)
        for segment in segments:
            pg.draw.rect(screen, (0, 255, 0), segment)
        pg.draw.rect(screen, (255, 0, 0), food)
        pg.display.flip()

        clock.tick(7)  # Lowered the tick rate for better visibility

def AlarmClock():
    alarmTime = input("Enter the alarm time you want to set: HH:MM:SS AM/PM\n")
    alarmHour = int(alarmTime[0:2])
    alarmMin = int(alarmTime[3:5])
    alarmSec = int(alarmTime[6:8])
    AlarmAM_PM = alarmTime[-2:]
    print("Setting Alarm")
    while True:
        now = datetime.datetime.now()
        CurrentHour = now.strftime("%I")  # Use %I for 12-hour format
        CurrentMinute = now.strftime("%M")
        CurrentSec = now.strftime("%S")
        CurrentPeriod = now.strftime('%p')
        if (AlarmAM_PM.upper() == CurrentPeriod.upper()) and (alarmHour == int(CurrentHour)) and (alarmSec == int(CurrentSec)) and (alarmMin == int(CurrentMinute)):
            print("WAKE UP!!")
            sound_file = "C:/Users/Prany/Downloads/clock-alarm-8761.mp3"  # Specify the path to the alarm sound file
            pg.mixer.init()  
            pg.mixer.music.load(sound_file)
            pg.mixer.music.play()
            break 
def  CurrentClock():
    time = datetime.datetime.now()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Time:", current_time)
def Clock():
    cl= int(input("\n1) Display Current time\n 2) Set an alarm\n Choose one: "))
    if cl == 1:
        CurrentClock()
    else:
        AlarmClock()    
        
def year():
    y = int(input("Enter the year: "))
    print(calendar.calendar(y))
def month():
    y = int(input("Enter the year: ")) 
    m =int(input("Enter month: "))
    print(calendar.month(y,m)) 
def Calendar():
    c= input("Year calendar or Month calendar?\n Write month/year: ")
    if c == 'month':
        month()
    else:
        year()    


def calculator():
    print("Welcome to Simple Calculator!")
    print("Enter the operation symbol for the operation you want to perform:")
    print("->'sqrt' for square root\n ->'log' for logarithm\n '^' for power")
    choice = input("Enter the operation symbol: ")
    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '+':
            print("Result:", (num1+num2))
        elif choice == '-':
            print("Result:", (num1- num2))
        elif choice == '*':
            print("Result:", (num1*num2))
        elif choice == '/':
            print("Result:", (num1/num2))
    elif choice in ['sqrt', '^']:
        num = float(input("Enter a number: "))
        if choice == 'sqrt':
            print("Result:", math.sqrt(num))
        elif choice == '^':
            p= int(input("Enter power: "))
            print("Result:", math.pow(num,p))
    elif choice == 'log':
        num = float(input("Enter a number: "))
        base = float(input("Enter the base: "))
        print("Result:", math.log(num, base))    
    else:
        print("Invalid operation symbol!")

choice = None
while choice!=0:
    print("\nWELCOME!\n THIS IS A MINI PHONE :)" )
    print("It contains the following features:\n 1) CLOCK\n 2) CALENDER\n 3) CALCULATOR\n 4) SNAKE GAME\n 5) GUESS THE WORD GAME\n 0:EXIT")
    choice= int(input("Choose One: "))
    if choice == 1:
        Clock()
    elif choice == 2:
        Calendar()
    elif choice == 3:
        calculator()
    elif choice == 4:
        print("Press 'Q' to exit!\n Enjoy your game!")
        snakegame()
    elif choice== 5:
        hangman()    
    else:
        print('invalid')            


