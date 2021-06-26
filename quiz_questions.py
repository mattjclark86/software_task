import pymysql
import random

def question_one():
    question = "What country does Harry Kane play for?"
    answer = "england"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_two():
    question = "Which country scored the most goals during the Euro2020 group stage?"
    answer = "netherlands"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_three():
    question = "Which country had the best goal difference during the Euro2020 group stage?"
    answer = "italy"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_four():
    question = "Which country does Tomáš Souček play for?"
    answer = "czech republic"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_five():
    question = "Which player scored the most goals in the Euro2020 group stage?"
    answer = "ronaldo"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_six():
    question = "Which player ended the group stage with the most Fantasy Football points?"
    answer = "ronaldo"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_seven():
    question = "Which team does Aymeric Laporte play for?"
    answer = "spain"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_eight():
    question = "Which player scored the final goal of the Euro2020 group stage?"
    answer = "goretzka"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def question_nine():
    question = "Which team scored and conceded the most goals combined in the Euro2020 group stage?"
    answer = "portugal"

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    insert = "INSERT INTO questions(question, answer) VALUES('" + question + "', '" + answer + "');"

    cursor.execute(insert)
    connection.commit()

    connection.close()

def generate_questions():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    questions = """CREATE TABLE IF NOT EXISTS questions(
    ID INT(20) PRIMARY KEY AUTO_INCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL)"""

    cursor.execute(questions)

    connection.close()

    questions_array = random.sample(range(1, 9), 3)

    for x in questions_array:
        if(x == 1):
            question_one()
        elif(x == 2):
            question_two()
        elif(x == 3):
            question_three()
        elif(x == 4):
            question_four()
        elif(x == 5):
            question_five()
        elif(x == 6):
            question_six()
        elif(x == 7):
            question_seven()
        elif(x == 8):
            question_eight()
        elif(x == 9):
            question_nine()

def drop_questions_table():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

    cursor = connection.cursor()

    drop = "DROP TABLE questions;"

    cursor.execute(drop)

    connection.close()