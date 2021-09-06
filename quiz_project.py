""" 
This program is a trivia quiz program. The user selects a topic, 
and then is challenged to answer quiz questions on that topic. 
If the user gets a question correct, they see a 'Correct!' message. 
If their answer is incorrect, they see a message with the correct answer. 
After the user has answered all the questions, they will see the number 
of questions they answered correctly.  
If they answered all questions correctly, they will see another message 
letting them know they answered all the questions correctly.
"""






def main():
 # dictionary to hold topics and their questions and answers
    question_bank = {
        'space':{
            'Which planet is closest to the sun?':'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system?':'Venus',
            'How many moons does Mars have?':'2',
            'What was the first human-made object to leave the solar system?':'Voyager 1'
        },
        'art':{
            'Who painted the Mona Lisa?':'Vincent Van Gogh',
            'What precious stone is used to make the artist\'s pigment ultramarine?':'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?':'Chicago'
        }
    }
    """
    function for user interface; the function asks the user for the topic
    """
    def topic_entry():
        print('Enter topic from the following: ')
        print(question_bank.keys())
        topic = input('Enter choice: ')
        return topic.lower()

    topic=topic_entry()

    #validate topic is in the dictionary
    while topic not in question_bank.keys():
        print('please enter a valid input')
        topic=topic_entry()

    #access the desired topic 
    question_for_topic = question_bank[topic]

    #get the total score after asking the questions
    total_score=ask_questions(question_for_topic)

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(question_for_topic)}.')

    if total_score == 3:
        print('You got all the answers correct!')

"""
the ask functions; it asks the user a series of questions related to the desired topic
then check the answeres for correctness. the total score is calculated and returned
"""
def ask_questions(questions):
    # todo needs to be split into more functions. 
    total_score = 0
    for q in questions:
        print(q)
        answer = input('your answer is:')#get the answer

        #validate the answer and check for correctness
        if answer.lower() ==  questions[q].lower():
            print('Correct!')
            total_score +=1
        else:
            print(f'Sorry, the answer is {questions[q]}')

    return total_score #return score

main()

# if topic == 'art':

#     print('Who painted the Mona Lisa?')
#     answer = input('Enter your answer: ')
#     if answer == 'Vincent Van Gartogh':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the answer is Leonardo Da Vinci.')
    
#     print('What precious stone is used to make the artist\'s pigment ultramarine?')
#     answer = input('Enter your answer: ')
#     if answer == 'Lapiz lazuli':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Lapiz lazuli.')

#     print('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
#     answer = input('Enter your answer: ')
#     if answer == 'Chicago':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Chicago.')

#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')

#     if total_score == 3:
#         print('You got all the answers correct!')


# elif topic == 'space':
    
#     print('Which planet is closest to the sun?')
#     answer = input('Enter your answer: ')
#     if answer == 'Mercury':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Mercury.')

#     print('Which planet spins in the opposite direction to all the others in the solar system?')
#     answer = input('Enter your answer: ')
#     if answer == 'Venus':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Venus.')

#     print('How many moons does Mars have?')
#     answer = input('Enter your answer: ')
#     if answer == '2':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is 2.')

#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')

#     if total_score == 3:
#         print('You got all the answers correct!')

# else:
#     print('That is not a valid topic. Restart the program to try again.')

