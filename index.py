#This program requires mysql for the database integration to work correctly
#The author used XAMPP and phpMyAdmin during the creation of this project
import pymysql
import time
from quiz_questions import *
#Imports necessary functions from the quiz_questions module

connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")
#The database must be set up before this program can be used
#If it is named differently than 'euros_quiz', then the code above must be changed accordingly

cursor = connection.cursor()

scores = """CREATE TABLE IF NOT EXISTS scores(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
name CHAR(3) NOT NULL,
accuracy FLOAT NOT NULL,
time FLOAT NOT NULL)"""
#Creates a scores table for the quiz database
#The IF NOT EXISTS parameter acts as a first-time setup operator

cursor.execute(scores)

def start_quiz():
    #Starts the quiz with a new set of questions
    score = 0
    #The user's score is tracked throughout
    start = time.time()
    #The user is also timed on how fast they complete the quiz

    generate_questions()
    #Generates three fresh randomly generated questions for the user to answer

    add_question = "SELECT * FROM questions WHERE ID='1';"
    cursor.execute(add_question)
    connection.commit()
    question_set_one = cursor.fetchone()

    add_question = "SELECT * FROM questions WHERE ID='2';"
    cursor.execute(add_question)
    connection.commit()
    question_set_two = cursor.fetchone()

    add_question = "SELECT * FROM questions WHERE ID='3';"
    cursor.execute(add_question)
    connection.commit()
    question_set_three = cursor.fetchone()

    answer_one = input(question_set_one[1])
    if(question_set_one[2] in answer_one.lower()):
    #To get a question right, the user must include the answer of the question somewhere in their input
    #It does not have to match exactly and case does not matter
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer...")
    time.sleep(1)
    #The program uses artifical time lengthening to simulate a traditional quiz format
    #It also gives the user breathing space for them to read each line of text
    
    print("Next question...")
    time.sleep(1)
    answer_two = input(question_set_two[1])
    if(question_set_two[2] in answer_two.lower()):
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer...")
    time.sleep(1)
    
    print("Final question...")
    time.sleep(1)
    answer_three = input(question_set_three[1])
    if(question_set_three[2] in answer_three.lower()):
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer...")
    time.sleep(1)
    
    accuracy = 100*(score/3)
    #Accuracy is calculated as a percentage of correct questions answered vs total questions asked
    end = time.time()
    time_taken = round((end - start), 2)
    #All time values are limited to two decimal places, meaning that it is unlikely but possible for two users to get the same time
    print("Your final score is " + str(score) + ". You completed the quiz in " + str(time_taken) + " seconds.")
    time.sleep(1)
    
    print("Adding score to database...")
    add_score = "INSERT INTO scores(name, accuracy, time) VALUES('" + name.upper() + "', '" + str(accuracy) + "', '" + str(time_taken) + "');"
    #The user's score is added to the database at the end of the quiz
    cursor.execute(add_score)
    connection.commit()
    time.sleep(1)
    
    print("Retrieving highscores...")
    select = "SELECT * FROM scores ORDER BY accuracy DESC, time;"
    #Time and score are the two parameters for determining the user's final rank
    cursor.execute(select)
    connection.commit()
    highscores = cursor.fetchall()
    time.sleep(1)

    entry = 0
    rank = 0
    temp = 0
    #Local variables are used to find the user's entry number and rank
    user_accuracy = ""
    user_time = ""
    print("HIGHSCORES")
    print("-----------------------------")
    print("ID  NAME  ACCURACY TIME")
    print("-----------------------------")
    for row in highscores:         
        print(row)
        print("")
        if(entry < row[0]):
            entry = row[0]
            rank = rank + temp + 1
            user_accuracy = str(row[2])
            user_time = str(row[3])
        else:
            temp += 1
    print("You were entry number " + str(entry) + ". Your entry ranked in at number " + str(rank) + ". You had an accuracy of " + user_accuracy + "% and a time of " + user_time + " seconds.")
    if(rank == 1):
        print("Congratulations! Your entry is now the new highscore!!!")

    drop_questions_table()
    #The questions table in the quiz database is dropped after a user finishes a quiz
    #This means that the user answers a different set of questions each time

    time.sleep(1)
    replay = input("Would you like to retry the quiz?")
    if('yes' in replay):
        time.sleep(1)
        start_quiz()
    else:
        time.sleep(1)
        print("Thanks for playing!")
    
print("Hello! Welcome to the Euro2020 group stage quiz!")
#This is the first message the user will see


def input_name():
#A simple function that forces the user to have a name in length of 3 characters
    time.sleep(1)
    name = input("Please enter your name. Max 3 characters: ")
    if(len(name) != 3):
        time.sleep(1)
        print("ERROR! Name is of an inappropriate length.")
        return input_name()
    else:
        return name

name = str(input_name())

time.sleep(1)

print("Hello " + name + "!")
time.sleep(1)

print("The quiz is about to begin.")
time.sleep(1)

start_quiz()
#The quiz portion of the program activates

connection.close()
#The connection with the database is closed once the quiz finishes