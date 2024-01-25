import random

def admission_bot(user_input, context):
    # Dictionary containing predefined questions and answers
    qna_dict = {
        "What are the admission procedures?": "The admission procedures typically involve submitting an online application, providing transcripts, and letters of recommendation.",
        "What are the admission requirements?": "Admission requirements may include academic transcripts, standardized test scores, letters of recommendation, and a personal statement.",
        "When is the admission deadline?": "The admission deadline varies by college. It's important to check the official college website for the most accurate and up-to-date information.",
        "How can I apply for admission?": "You can apply for admission by filling out the online application form available on the college website.",
        "Is there an interview for admission?": "Yes there is an interview for the admission.",
        "What is the minimum GPA for admission?": "The minimum GPA for admission depends on the college and the program. It's best to check the specific requirements for the college you are applying to.",
        "Are there any scholarships available?": "Yes there are many types of scholarships , please look up for them in the college website",
        "Can I transfer credits from another college?": "Some colleges allow credit transfers. You should contact the admissions office of the college you are interested in for information on their credit transfer policy.",
        "Where can I find information on tuition fees?": "You can find information on tuition fees on the college's official website or by contacting the admissions or finance office.",
        "What majors does the college offer?": "Colleges offer a variety of majors in Computer Science, Mechanical , Chemical , Metallurgy, Astronomy",
        "What is the acceptance rate of the college?": "The acceptance rate of the college is 65%"
    }

    
    if user_input.isdigit():
        option = int(user_input)
        questions = list(qna_dict.keys())
        if 1 <= option <= len(questions):
            selected_question = questions[option - 1]
            response = qna_dict[selected_question]
            
            if response and 'name' in context:
                response = response.replace("you", context['name'])
            return response
        else:
            return "Invalid option. Please select a valid question number."
    elif user_input.lower() == 'list':
        return "\n".join([f"{i + 1}. {question}" for i, question in enumerate(qna_dict.keys())])
    else:
       
        return "I'm sorry, I don't have information on that. Please check the college's official website or contact the admissions office for more details."

context = {}
print("Admission Q&A Bot: Hello! How can I help you with your college admission queries? Type 'list' to get the list of questions Type 'exit' to end the session.")
while True:
   
    user_input = input("Question: " )

    if user_input.lower() == 'exit':
        exit_message = "Goodbye, See you again"
        if 'name' in context:
            exit_message += f", {context['name']}"
        print("Admission Q&A Bot:", exit_message)
        break

    bot_response = admission_bot(user_input, context)

   
    if 'name' not in context and ('Hello there' in user_input or 'Hi' in user_input):
        context['name'] = input("Admission Q&A Bot: Nice to meet you! May I know your name? ")
        print("Admission Q&A Bot: Hi, {}. How can I assist you today?".format(context['name']))
    else:
     
        if not bot_response:
            print("Admission Q&A Bot: I'm sorry, I couldn't understand your query. Please try a different question or type 'list' to see available questions.")
        else:
            print("Admission Q&A Bot:", bot_response)
            print("-" * 50)