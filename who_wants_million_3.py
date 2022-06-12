from operator import index
from os import read
import random, ast
from re import A
from turtle import Turtle


asked_questions=[]
corrects=[]
wrongs=[]
money=(
'100', '200', '300', '500', '1 000', '2 000', '4 000', '8 000',
'16 000', '32 000', '64 000', '125 000', '250 000', '500 000', '1 000 000'
)
help_list=[]

#open and read questions file
def read_file():
    global f
    f=open ("general_questions.txt","r")
    str_questions=f.read()
    global questions_list
    questions_list=ast.literal_eval(str_questions)

#extract questions and answers from questions list
def extract_questions():
    #randomly choose whole question dictionary from file
    randquestdict=questions_list[random.randint(0,len(questions_list)-1)]
    #take only question part(without answers) and make it a string
    question_list=list(randquestdict.keys())
    global question
    question=question_list[0]
    #take only answers and make it a string
    global answers_list
    answers_list=list(randquestdict.values())[0]
    global correct_answ
    correct_answ=answers_list[0]
    

#make randomized list with only wrong answers and append correct answer.
def randomized_wrongs():
    global rand_wrongs
    rand_wrongs=[]
    for i in range(3):
        while True:
            randansw=answers_list[random.randint(1,3)]
            if randansw in rand_wrongs:
                continue
            else:
                rand_wrongs.append(randansw)
                break
    rand_wrongs.append(correct_answ)

#randomize previous list with wrong and correct answers.
def randomized_all():
    global rand_all
    rand_all=[]
    for x in range(4):
        while True:
            randchoice=rand_wrongs[random.randint(0,3)]
            if randchoice in rand_all:
                continue
            else:
                break
        rand_all.append(randchoice)

# print question and answers
def print_questions():
    print (str(quiznum+1)+". "+question) 
    print ("A. "+rand_all[0])
    print ("B. "+rand_all[1])
    print ("C. "+rand_all[2])
    print ("D. "+rand_all[3])

#let user type answer, check if its' correct and print relevant message
def user_input():
    while True:
        if len(help_list)!=3:
            answ=input("Get help (H), Or enter your answer (A, B, C or D): ")
        else:
            answ=input("Enter your answer (A, B, C or D): ")    

        if answ=="H":
            if len(help_list)!=3:
                helps()
            else:
                print('No more helps available')   
                
        else:    
            if correct_answ==rand_all[0] and answ=="A" or correct_answ==rand_all[1] and answ=="B" or correct_answ==rand_all[2] and answ=="C" or correct_answ==rand_all[3] and answ=="D":
                answer=True
                corrects.append(answer)
                if len(corrects)==5:
                    print("You won guaranteed $1000\n")
                elif len(corrects)==10:
                    print("You won guaranteed $32000\n")
                elif len(corrects)==15:
                    print("Congratulations!".upper()+" You are now a millionaire\n")
                else:
                    print ("You won $"+str(money[len(corrects)-1]) + "\n")    
                break

            elif answ=="A" and correct_answ!=rand_all[0] or answ=="B" and correct_answ!=rand_all[1] or answ=="C" and correct_answ!=rand_all[2] or answ=="D" and correct_answ!=rand_all[3]:
                answer=False
                wrongs.append(answer) 
                print ("Wrong! Correct answer is ".upper()+ correct_answ.upper()+".\n")
                break
            else:
                continue

    asked_questions.append(question)
 
#print help options 
def helps():
    global get_help
    while True:
        get_help=input("\nGet help ('F'- Friend, 'P'- People, 'FF' - 50/50): ")
        
        if get_help=='F':
            if 'F' not in help_list:
                print ("\nHello my friend. I think the correct answer is "+ correct_answ)
                help_list.append(get_help)
                break
            else: 
                print("\nYou already used this help")
                continue  
       
        elif get_help=='P':
            if 'P' not in help_list:
                print("\nPeople think that correct answer is "+correct_answ)
                help_list.append(get_help)
                break
            else:
                print("\nYou already used this help")
                continue

        elif get_help=='FF':
            if 'FF' not in help_list:
                help_list.append(get_help)
                ff=[correct_answ, rand_wrongs[random.randint(0,2)]]
                ff_full=[]

                if correct_answ==rand_all[0]:
                    ff_full.append ("A. "+rand_all[0])
                elif correct_answ==rand_all[1]:
                    ff_full.append ("B. "+rand_all[1])
                elif correct_answ==rand_all[2]:
                    ff_full.append ("C. "+rand_all[2])
                elif correct_answ==rand_all[3]:
                    ff_full.append ("D. "+rand_all[3])   

                if ff[1]==rand_all[0]:
                    ff_full.append ("A. "+rand_all[0])
                elif ff[1]==rand_all[1]:
                    ff_full.append ("B. "+rand_all[1])
                elif ff[1]==rand_all[2]:
                    ff_full.append ("C. "+rand_all[2])   
                elif ff[1]==rand_all[3]: 
                    ff_full.append ("D. "+rand_all[3])

                ff_full.sort()
                print("\nChoose your answer:")
                print(ff_full[0])
                print(ff_full[1])
                break

            else:
                print("\nYou already used this help")
                continue

        else:
            print("Type only 'F', 'P' or 'FF'")
            continue       

#run game   
def game():
    read_file()
    global quiznum
    for quiznum in range(15):
        if len(wrongs)<1:
            while True:
                extract_questions()
                if question in asked_questions:
                    continue
                else:
                    randomized_wrongs()
                    randomized_all()
                    print_questions()
                    user_input()
                    break
        else: 
            if 5<=len(corrects)<10:
                print("You lost the game but won guaranteed $1000\n")
            elif 10<=len(corrects)<15:
                print("You lost the game but won guaranteed $32000\n")
            else:
                print("You lost the game")
            break
           
    f.close()

    #reset results and asked questions lists
    corrects.clear()
    wrongs.clear()
    asked_questions.clear()
    help_list.clear()
        
#main game loop
def game_loop():
    game()
    while True:
        inp=input("Do you want to play again (P) or quit (Q)?: ")
        if inp=="P":
            game()
            continue
        elif inp=="Q":
            print("\nquitting\n".upper())
            break
        else:
            print ("Type only 'P' or 'Q'")
            continue        

game_loop()