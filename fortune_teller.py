import random
import time
import datetime as dt
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)

print("\nI am the Fortune Teller, ask me yes or no questions")

time.sleep(1)

print("So, let's begin...")

time.sleep(1)

def tell_fortune():
    global question
    question = input("\nWhat is your question? ")
    
    if "help" in question or "Help" in question:
        print("\nWhen you are aking questions, you must include:")
        print("    a question mark at the end")
        print("    at least 6 characters")
        print("    spaces between each word")
        print("    capital letters")
        print("\nIf you want to continue asking questions when the question is asked, type \"yes\"")
        print("\nI hope that this helped you!")
        time.sleep(2)
        tell_fortune()
        
    if " time" in question or " date" in question:
        print("\nToday's date and time are " + str(dt.datetime.now()) + " I know, I am really precise!")
        time.sleep(1)
        print("You are asking me obvious questions, please ask me questions about your future!")
        time.sleep(1)
        print("So...")
        time.sleep(1)
        tell_fortune()
        
    if " you " in question:
        print("Why are you asking questions about me?")
        print("I am here to predict your future, not mine!")
        tell_fortune()
        
    if len(question) < 5 or not " " in question:
        print("\nPlease ask an actual question! Who do you think I am, a computer?")
        print("(If you are having trouble asking questions, type \"help\" in the next question)")
        print("So...")
        tell_fortune()
        
    if "?" not in question:
        print("\nYou forgot the question mark! What do they teach in schools these days?")
        print("Please answer the questions correctly...")
        tell_fortune()
        
    print("Predicting the future...")
    time.sleep(1)
    answer()

def answer():
    
    answers = ["Yes","No", "Definitely", "Maybe", "Please ask again later", "Most likely", "Cannot predict now", "Outlook good", "It is certain", "My reply is no", "You may rely on it", "Signs point to yes", "Very Doubtful", "Don't count on it", "Reply hazy, try again"]
    answers_for_yes = ["Yes", "Definitely", "Most likely"]
    answers_for_no = ["No", "Very doubtful", "My reply is no"]
    
    global random_number
    random_number = 0
    if " I " in question:
        if "Am " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", you are")
            else:
                print(random.choice(answers_for_no) + ", you aren't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", you will")
            else:
                print(random.choice(answers_for_no) + ", you won't")
                
    elif " he " in question:
        if "Is " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", he is")
            else:
                print(random.choice(answers_for_no) + ", he isn't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", he will")
            else:
                print(random.choice(answers_for_no) + ", he won't")
                
    elif " she " in question:
        if "Is " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", she is")
            else:
                print(random.choice(answers_for_no) + ", she isn't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", she will")
            else:
                print(random.choice(answers_for_no) + ", she won't")

    elif " it " in question:
        if "Is " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", it is")
            else:
                print(random.choice(answers_for_no) + ", it isn't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", it will")
            else:
                print(random.choice(answers_for_no) + ", it won't")
            
    elif " we " in question:
        if "Are " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", we are")
            else:
                print(random.choice(answers_for_no) + ", we aren't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", we will")
            else:
                print(random.choice(answers_for_no) + ", we won't")
            
    elif " they " in question:
        if "Are " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", they are")
            else:
                print(random.choice(answers_for_no) + ", they aren't")
        if "Will " in question:
            random_number = random.randint(0,2)
            if random_number == 0:
                print(random.choice(answers_for_yes) + ", they will")
            else:
                print(random.choice(answers_for_no) + ", they won't")

    else:
        print(random.choice(answers))
    time.sleep(1)
    other_questions()

def other_questions():
    
    global other_question_answer
    other_question_answer = input("\nDo you have any other questions? ")

    time.sleep(1)

    if " " in other_question_answer and len(other_question_answer) > 5 and "?" in other_question_answer:
        print("\nThis is a yes or no question... But I can answer your question!")
        print("I would say...\n")
        global question
        question = other_question_answer
        time.sleep(1)
        answer()

    elif " " in other_question_answer and len(other_question_answer) > 5:
        print("\nThis is a yes or no question... It is to see if you want to continue talking to me, the Fortune Teller!")
        other_question_answer = input("So, I guess you want to continue to talk to me? ")
        if "y" in other_question_answer or "Y" in other_question_answer:
            tell_fortune()
            
    elif "?" in other_question_answer or "help" in other_question_answer:
        print("\nIf you want to continue asking questions when this question is asked, type \"yes\"")
        time.sleep(1)
        print("So...")
        other_questions()

    if "y" in other_question_answer or "Y" in other_question_answer:
        tell_fortune()
    elif "n" in other_question_answer or "N" in other_question_answer:
        print("\nHave a good day! I kind of like predicting the future...")
        time.sleep(3)
        exit()
        
    else:
        print("\nI am lost...")
        print("So...")
        launch_other_questions()
        
def launch_other_questions():
    other_questions()
    
tell_fortune()
