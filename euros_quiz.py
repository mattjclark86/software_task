#This program requires mysql for the database integration to work correctly
#The author used XAMPP and phpMyAdmin during the creation of this project
import pymysql
import time

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

def question_set_one():
    #Function for the first set of questions
    #Currently the only set of questions available
    score = 0
    #The user's score is tracked throughout
    start = time.time()
    #The user is also timed on how fast they complete the quiz
    answer_one = input("What team does Harry Kane play for?")
    if('england' in answer_one.lower()):
    #The questions are currently quite harsh, it has to be the exact name of the country
        print("Correct answer!")
        score += 1
    else:
        print("WRONG!!")
    time.sleep(1)
    #The program uses artifical time lengthening to simulate a traditional quiz format
    #It also gives the user breathing space for them to read each line of text
    
    print("Next question...")
    time.sleep(1)
    answer_two = input("Which team scored the most goals during the Euro2020 group stage?")
    if('netherlands' in answer_two.lower()):
        print("Correct answer!")
        score += 1
    else:
        print("WRONG!!")
    time.sleep(1)
    
    print("Final question...")
    time.sleep(1)
    answer_three = input("Which team had the best goal difference during the Euro2020 group stage?")
    if('italy' in answer_three.lower()):
        print("Correct answer!")
        score += 1
    else:
        print("WRONG!!")
    time.sleep(1)
    
    accuracy = 100*(score/3)
    end = time.time()
    time_taken = round((end - start), 2)
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
    
    print("SCORE TABLE")
    for row in highscores:         
        print(row)
    
print("Hello User!")
time.sleep(1)
#This is the first message the user will see

name = input("Please enter your name. Max 3 characters.")
#Note: names do not have to be 3 characters, only up to a maximum of 3 characters, 0 characters is also possible
if(len(name) > 3):
    print("ERROR! Name too long. Shutting down.")
    sys.exit()
time.sleep(1)

print("The quiz is about to begin.")
time.sleep(1)

question_set_one()
connection.close()
