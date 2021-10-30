#!/usr/bin/python3

import datetime 
import pytz 
import wikipedia
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from playsound import playsound
import time
import requests, json 
import random
import sys
from src.AI import AI
from src.Board import Board
from src.InputParser import InputParser
import math


dictionary = {'hello': 'Hi! I\'m Lola, your virtual assistant',
             'help': 'Hi! I\'m Lola, your virtual assistant. \nYou can ask me whatever you need!!!',
              'friends': 'I\'m your friend!',
              'money': 'Maybe this can be useful: <link how to earn money>', #insert some stupid link
              'how are you?': 'Pretty good! I\'m proud of beeing your personal assistant!',  
              'options': 'Options: \n time \n date \n weather \n news \n wikipedia \n email \n base converter \n morse converter \n calculator \n chess \n Type exit to exit'
             }

    
def time_function():
    print(" ")
    print("What is your time zone?")
    print("(-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12)")
    print("If you don't now your time zone, you can check it \x1b]8;;https://en.wikipedia.org/wiki/Time_zone\a\033[4;37m"+"here\x1b]8;;\a")
    print("\033[0;37m"+"")
       

    time_zone = input("TIME ZONE: ")
            
    if time_zone == "-12":
        time_zone = "Etc/GMT+12"
    elif time_zone == "-11":
        time_zone = "Etc/GMT+11" 
    elif time_zone == "-10":              
        time_zone = "Etc/GMT+10"
    elif time_zone == "-9": 
        time_zone = "Etc/GMT+9"
    elif time_zone == "-8":
        time_zone = "Etc/GMT+8"
    elif time_zone == "-7":
        time_zone = "Etc/GMT+7"
    elif time_zone == "-6":
        time_zone = "Etc/GMT+6"
    elif time_zone == "-5":
        time_zone = "Etc/GMT+5"
    elif time_zone == "-4":
        time_zone = "Etc/GMT+4"
    elif time_zone == "-3":
        time_zone = "Etc/GMT+3"
    elif time_zone == "-2":
        time_zone = "Etc/GMT+2"
    elif time_zone == "-1":
        time_zone = "Etc/GMT+1"
    elif time_zone == "0":                    
        time_zone = "Etc/GMT+0"
    elif time_zone == "1" or time_zone == "+1":
        time_zone = "Etc/GMT-1"
    elif time_zone == "2" or time_zone == "+2":                    
        time_zone = "Etc/GMT-2"       
    elif time_zone == "3" or time_zone == "+3":                    
        time_zone = "Etc/GMT-3"
    elif time_zone == "4" or time_zone == "+4": 
        time_zone = "Etc/GMT-4"
    elif time_zone == "5" or time_zone == "+5":
        time_zone = "Etc/GMT-5"
    elif time_zone == "6" or time_zone == "+6":                    
        time_zone = "Etc/GMT-6"
    elif time_zone == "7" or time_zone == "+7":                    
        time_zone = "Etc/GMT-7"
    elif time_zone == "8" or time_zone == "+8": 
        time_zone = "Etc/GMT-8"
    elif time_zone == "9" or time_zone == "+9":
        time_zone = "Etc/GMT-9"            
    elif time_zone == "10" or time_zone == "+10":
        time_zone = "Etc/GMT-10"
    elif time_zone == "11" or time_zone == "+11": 
        time_zone = "Etc/GMT-11"   
    elif time_zone == "12" or time_zone == "+12":
        time_zone = "Etc/GMT-12"
    else:
        print("Not a time zone")
        all_code()
        
    
    current_time = datetime.datetime.now(pytz.timezone(time_zone))  
    print ("The current date and time in your country is :", current_time)
    
    
    
def date_function():
    x = datetime.datetime.now()

    print(x.day, "/", x.month, "/", x.year)

def news_function():
    print("\x1b]8;;https://www.bbc.com/news\a\033[4;37m"+"<BBC News>\x1b]8;;\a")
    print("\x1b]8;;https://www.theguardian.com/international\a\033[4;37m"+"<The Guardian>\x1b]8;;\a")
    print("\x1b]8;;https://www.nytimes.com/\a\033[4;37m"+"<New York Times>\x1b]8;;\a")
    
    print("\033[0;37m"+"")
    
def wikipedia_function():
    word = input("Type your search here: ")

    print("")
    print("What of those searches do you need?: ")

    print("")

    print(wikipedia.search(word))

    print("")

    word2 = input("Copy here your search: ")

    print("")

    print("Summary: \n" + wikipedia.summary(word2, sentences = 3))

    print("")

    link = wikipedia.page(word2).url

    link2 = "\x1b]8;;" + link + "\a\033[4;37m"+"<LINK>\x1b]8;;\a"

    print("Link for more information: " , link2)
    
    print("\033[0;37m"+"")
    
    
def email_function():
    msg = MIMEMultipart()

    print("")
    print("***Send an email***")

    msg['From'] = input("Your email: ")
    password = getpass.getpass("Password (not going to appear): ")
    #password = input("Contrasenya: ")
    msg['To'] = input("Email of the destinatary: ")
    msg['Subject'] = input("Subject: ")

    message = input('Message: ')

    newMessage = "Encypted message: " +  message

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print('***Message sent***')


def base_converter_function():
    print("In what base are you going to enter the number?")
    print("Binary(1), Octadecimal(2), Decimal(3), Hexadecimal(4)")
    
    base = input("Base num: ")
    
    num = input("What number do you want to convert?: ")
    
    if base == "1":
        print(num, "in octal =", oct(int(num)))
        print(num, "in decimal =", int(num, 2))        
        print(num, "in hexa =", hex(int(num)))
        print("")
        

    if base == "2":
            
        b = int(num, 8)
        b = bin(b)
        
        d = int(num, 8)
        
        h = int(num, 8)
        h = hex(int(num))        
        

        print(num, "in binary =", b)
        print(num, "in decimal =", d)        
        print(num, "in hexa =", h)
        print("")
        
    if base == "3":
        b = bin(int(num))
        
        o = oct(int(num))
            
        h = hex(int(num))        
        

        print(num, "in binary =", b)
        print(num, "in octal =", o)        
        print(num, "in hexa =", h)
        print("")
        
    if base == "4":
        
        b = bin(int(num))
        
        o = oct(int(num))
            
        d = int(num, 16)        
        

        print(num, "in binary =", b)
        print(num, "in octal =", o)        
        print(num, "in decimal =", d)
        print("")
        
def morse_function():

    dictionary = {
        " " : " ",
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",

        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"
    }


    text = input("What text do you want to convert to morse?: ")

    #print ( "Original text: " + text )

    morse = ""

    for c in text:
        morse += dictionary[ c.upper() ] + " "

    print (text, "in morse: ", morse )

    
def calculator_function():
    output = 0
    num1 = ""
    operation = ""
    num2 = ""

    print("What operation would you like to calculate(+, -, *, /, ^, √)?")
    operation = input("Operation: ")
    
    
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":

        num1 = input("What is your First Number?: ")
        num2 = input("Your Second Number?: ")

        floatnum1 = float(num1)
        floatnum2 = float(num2)

        if operation == "+":
            output=floatnum1+floatnum2
        if operation == "-":
            output=floatnum1-floatnum2
        if operation == "*":
            output=floatnum1*floatnum2
        if operation == "/":
            output=floatnum1/floatnum2


        if operation == "+" or operation == "-" or operation == "/" or operation == "*":
            #print("Your Answer: "+str(output))
            print(num1, operation, num2, " = ", str(output))
        else:
            print("Your operation is invalid, please try again")
            
    elif operation == "exponent":
        num = input("What number would you like to raise?: ")
        num = float(num)

            
        def exp_function():
            exp = input("Exponent to raise the number?: ")

            if "," in exp:
                print("The exponent must be whole number")
                exp = ""
                exp_function()
                
            elif "." in exp:
                print("The exponent must be whole number")
                exp = ""
                exp_function()
            else:
                exp = float(exp)
                
                result = num ** exp
                print(num, " ** ", exp, " = ", result)
                    
        exp_function()
        
    elif operation == "root":
        
        def root_type():
            root = input("Would you like to calculate a square root (2) or a cube root (3)?: ")
        
            if root == "2":
                num = input("What number would you like to root?: ")
                print("Square root of ", num, " = ", math.sqrt(int(num)))
            
        
            elif root == "3":
                num = input("What nuber would you like to cube root?: ")
                num = float(num)

                print("Cube root of ", num, " = ", num ** (1/3))
            
            
            else:
                print("Choose between 2 (square root) or 3 (cube root)")
                root_type()
        root_type()
        
            
def weather_function():

    api_key = "c18d256c5a06e4a98fef5438d3d5be62"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("What's your city?: ") 

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    response = requests.get(complete_url) 

    x = response.json() 

    y = x["main"] 

    celsius = (y["temp"]-272.15)

    celsius = round(celsius, 2)

    if x["cod"] != "404": 


        current_temperature = y["temp"]


        current_pressure = y["pressure"] 

        current_humidiy = y["humidity"] 


        z = x["weather"] 


        weather_description = z[0]["description"] 

        print("")
        print("Weather INFO for your current location:")
        print("     Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n     Temperature (in celsius unit) = " +
                        str(celsius) +
            "\n     Atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n     Humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n     Description = " +
                        str(weather_description)) 

    else: 
        print(" City Not Found ") 

        
def chess_function():
    
    WHITE = True
    BLACK = False


    def askForPlayerSide():
        playerChoiceInput = input(
            "What side would you like to play as [wB]? ").lower()
        if 'w' in playerChoiceInput:
            print("You will play as white")
            return WHITE
        else:
            print("You will play as black")
            return BLACK


    def askForDepthOfAI():
        depthInput = 2
        try:
            depthInput = int(input("How deep should the AI look for moves?\n"
                                   "Warning : values above 3 will be very slow."
                                   " [2]? "))
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Invalid input, defaulting to 2")
        return depthInput


    def printCommandOptions():
        undoOption = 'u : undo last move'
        printLegalMovesOption = 'l : show all legal moves'
        randomMoveOption = 'r : make a random move'
        quitOption = 'quit : resign'
        moveOption = 'a3, Nc3, Qxa2, etc : make the move'
        options = [undoOption, printLegalMovesOption, randomMoveOption,
                   quitOption, moveOption, '', ]
        print('\n'.join(options))


    def printAllLegalMoves(board, parser):
        for move in parser.getLegalMovesWithNotation(board.currentSide, short=True):
            print(move.notation)


    def getRandomMove(board, parser):
        legalMoves = board.getAllMovesLegal(board.currentSide)
        randomMove = random.choice(legalMoves)
        randomMove.notation = parser.notationForMove(randomMove)
        return randomMove


    def makeMove(move, board):
        print("Making move : " + move.notation)
        board.makeMove(move)


    def printPointAdvantage(board):
        print("Currently, the point difference is : " +
              str(board.getPointAdvantageOfSide(board.currentSide)))


    def undoLastTwoMoves(board):
        if len(board.history) >= 2:
            board.undoLastMove()
            board.undoLastMove()


    def startGame(board, playerSide, ai):
        parser = InputParser(board, playerSide)
        while True:
            print()
            print(board)
            print()
            if board.isCheckmate():
                if board.currentSide == playerSide:
                    print("Checkmate, you lost")
                else:
                    print("Checkmate! You won!")
                return

            if board.isStalemate():
                if board.currentSide == playerSide:
                    print("Stalemate")
                else:
                    print("Stalemate")
                return

            if board.currentSide == playerSide:
                # printPointAdvantage(board)
                move = None
                command = input("It's your move."
                                " Type '?' for options. ? ")
                if command.lower() == 'u':
                    undoLastTwoMoves(board)
                    continue
                elif command.lower() == '?':
                    printCommandOptions()
                    continue
                elif command.lower() == 'l':
                    printAllLegalMoves(board, parser)
                    continue
                elif command.lower() == 'r':
                    move = getRandomMove(board, parser)
                elif command.lower() == 'exit' or command.lower() == 'quit':
                    return
                try:
                    move = parser.parse(command)
                except ValueError as error:
                    print("%s" % error)
                    continue
                makeMove(move, board)

            else:
                print("AI thinking...")
                move = ai.getBestMove()
                move.notation = parser.notationForMove(move)
                makeMove(move, board)

    def twoPlayerGame(board):
        parserWhite = InputParser(board, WHITE)
        parserBlack = InputParser(board, BLACK)
        while True:
            print()
            print(board)
            print()
            if board.isCheckmate():
                print("Checkmate")
                return

            if board.isStalemate():
                print("Stalemate")
                return

            # printPointAdvantage(board)
            if board.currentSide == WHITE:
                parser = parserWhite
            else:
                parser = parserBlack
            move = None
            command = input("It's your move, {}.".format(board.currentSideRep()) + \
                            " Type '?' for options. ? ")
            if command.lower() == 'u':
                undoLastTwoMoves(board)
                continue
            elif command.lower() == '?':
                printCommandOptions()
                continue
            elif command.lower() == 'l':
                printAllLegalMoves(board, parser)
                continue
            elif command.lower() == 'r':
                move = getRandomMove(board, parser)
            elif command.lower() == 'exit' or command.lower() == 'quit':
                return
            try:
                move = parser.parse(command)
            except ValueError as error:
                print("%s" % error)
                continue
            makeMove(move, board)


    board = Board()

    def main():
        try:
            if len(sys.argv) >= 2 and sys.argv[1] == "--two":
                twoPlayerGame(board)
            else:
                playerSide = askForPlayerSide()
                print()
                aiDepth = askForDepthOfAI()
                opponentAI = AI(board, not playerSide, aiDepth)
                startGame(board, playerSide, opponentAI)
        except KeyboardInterrupt:
            sys.exit()

    if __name__ == "__main__":
        main()


print("***VIRTUAL ASSISTANT*** (type help for help and options to see options)")


def all_code():
    i = 0
    while i < 1:
        text = input("What do you need?: ")
        text = text.lower()
            
        if "hello" in text:
            print(dictionary["hello"])
            print("_________________________")

        elif "help" in text:
            print(dictionary["help"])
            print("_________________________")
            
        elif "options" in text:
            print(dictionary["options"])
            print("_________________________")

            
        elif "date" in text:
            date_function()
            print("_________________________")

        elif "time" in text:
            time_function()
            print("_________________________")

        elif "news" in text:
            news_function()
            print("_________________________")


        elif text == 'exit':
            i = i+1
            
        elif "wikipedia" in text:
            wikipedia_function()
            print("_________________________")
            
        elif "email" in text:
            email_function()
            print("_________________________")
            
        elif "base converter" in text:
            base_converter_function()
            print("_________________________")
            
        elif "morse converter" in text:
            morse_function()
            print("_________________________")
            
        elif "calculator" in text:
            calculator_function()
            print("_________________________")

            
        elif "weather" in text:
            weather_function()
            print("_________________________")
            
        elif "chess" in text:
            chess_function()
            print("_________________________")
            
        elif "money" in text:
            print(dictionary["money"])
            print("_________________________")
            
        elif "friends" in text:
            print(dictionary["friends"])
            print("_________________________")
                
        elif "how are you" in text:
            print(dictionary["how are you?"])
            print("_________________________")
            
        else:
            print("Command not found")
            print("_________________________")



all_code()