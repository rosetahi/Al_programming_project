def chatbot():
    print("🎓 Welcome to Nova University Chatbot!")
    print("Type 'exit' or 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        # 1. Greeting Intent
        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello  Welcome to Nova University!")
            print("Bot: I’m here to help you with courses, admissions, fees, and location.")

        # 2. Courses Intent
        elif "course" in user_input or "program" in user_input:
            print("Bot: Nova University offers a variety of programs ")
            print("Bot: These include Information Technology, Business Administration, Education, and Nursing.")
            print("Bot: Let me know if you'd like details about a specific course!")

        # 3. Admission Intent (WITH CONTACT INFORMATION)
        elif "apply" in user_input or "admission" in user_input:
            print("Bot: Applying to Nova University is simple ")
            print("Bot: You need to fill out the online application form and upload your academic documents.")
            print("Bot: The minimum requirement is a KCSE mean grade of C+ or equivalent.")
            print("Bot: If you need help, feel free to contact us at:")
            print("Bot:  info@novauniversity.ac.ke")
            print("Bot: call +254 700 000 000")

        # 4. Fees Intent
        elif "fee" in user_input or "cost" in user_input:
            print("Bot: Tuition fees depend on the course you choose ")
            print("Bot: On average, fees are around KES 120,000 per year.")
            print("Bot: We also offer flexible payment plans and  also scholarships.")

        # 5. Location Intent
        elif "location" in user_input or "where" in user_input:
            print("Bot: Nova University is located in Nairobi, Kenya ")
            print("Bot: Our campus is easily accessible and has modern facilities.")

        # Exit Condition
        elif user_input in ["bye", "exit"]:
            print("Bot: Thank you for chatting with Nova University! ")
            print("Bot: We hope to see you soon. Goodbye ")
            break

        # Fallback Response
        else:
            print("Bot: Hmm  I didn’t quite understand that.")
            print("Bot: You can ask me about courses, admissions, fees, or location.")

# Run the chatbot
chatbot()