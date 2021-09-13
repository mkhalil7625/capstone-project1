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

# avoid creating functions inside other functions, unless the nested function is 
# inherently tied to the containing function and doesn't make sense without it. It's fairly rare to create nested functions.
def topic_entry(topics):
    """
    Docstring goes after the def line. 
    User interface function to display list of topics and ask user for their choice, return the topic chosen
    """

  print('Enter topic from the following: ')
    print(topics)   # This prints dict_keys(['art', 'space']) - can you display the choices in a more user-friendly way? 
    topic = input('Enter choice: ')

    # validate topic is in the dictionary
    while topic not in topics:
        print('please enter a valid input')
        topic = input('Enter choice: ')
        
    return topic.lower()  

   
def main():
 # dictionary to hold topics and their questions and answers
    question_bank = {
        'space': {
            'Which planet is closest to the sun?': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
            'How many moons does Mars have?': '2',
            'What was the first human-made object to leave the solar system?': 'Voyager 1'
        },
        'art': {
            'Who painted the Mona Lisa?': 'Vincent Van Gogh',
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'
        }
    }

    topic = topic_entry(question_bank.keys())   # pass the list of topics to the function, handle validation in the function

    # access the desired topic 
    question_for_topic = question_bank[topic]

    # get the total score after asking the questions
    total_score = ask_questions(question_for_topic)

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(question_for_topic)}.')

    if total_score == 3:   # what if there are 2 or 3 or 100 questions? Will this work? Can you use len(questions_for_topic) in this condition? 
        print('You got all the answers correct!')


def ask_questions(questions):
 
    """
    the ask functions; it asks the user a series of questions related to the desired topic
    then check the answeres for correctness. the total score is calculated and returned
    """
    
   # todo needs to be split into more functions. (I think this is fine - if the quiz got more complex you'll probably need to break this down.)
    total_score = 0
    for q in questions:
        print(q)
        answer = input('your answer is:') # get the answer

        #validate the answer and check for correctness
        if answer.lower() ==  questions[q].lower():
            print('Correct!')
            total_score +=1
        else:
            print(f'Sorry, the answer is {questions[q]}')

    return total_score #return score  This comment isn't needed. Comments should focus on explaining the complex parts of code. 

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

