questions = [["What is the capital city of Pakistan?", ["Karachi", "Islamabad", "Lahore", "Peshawar"], 1], ["Which river flows through Lahore?", ["Jhelum", "Indus", "Ravi", "Chenab"], 2], ["Who is the founder of Pakistan?", ["Allama Iqbal", "Quaid-e-Azam Muhammad Ali Jinnah", "Liaquat Ali Khan", "Benazir Bhutto"], 1], ["What is the national language of Pakistan?", ["Urdu", "Sindhi", "Pashto", "Punjabi"], 0], ["Which city is known as the 'City of Gardens' in Pakistan?", ["Karachi", "Islamabad", "Lahore", "Multan"], 2], ["What is the largest city in Pakistan by population?", ["Karachi", "Faisalabad", "Islamabad", "Lahore"], 0], ["Which mountain range is located in the northern areas of Pakistan?", ["Karakoram", "Himalayas", "Pamir", "Hindu Kush"], 1], ["What is the national animal of Pakistan?", ["Markhor", "Tiger", "Lion", "Leopard"], 0], ["Which Pakistani cricketer has the highest number of centuries in international cricket?", ["Shoaib Malik", "Inzamam-ul-Haq", "Sachin Tendulkar", "Mohammad Yousuf"], 2], ["What is the national flower of Pakistan?", ["Sunflower", "Tulip", "Jasmine", "Rose"], 2]]

prices = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

print("Welcome to KBC!")
print("---------------- Rules ----------------")
print("1. You will be asked 10 questions. Each question has a price. You will win the price if you answer the question correctly.")
print("2. You will be given 4 options. You have to enter the correct option number to answer the question.")
print("3. You will be given 2 chances to skip a question. You can skip a question by entering '-1'.")
print("4. Your game will end if you answer a question incorrectly.")
print("5. You can quit the game at any time by entering '0'.")
print("6. In both cases i.e. quiting the game or answering a question incorrectly, you will win your current price value.")

print("\nLet's start the game!\n")

price = 0
skip = 2
for i in range(len(questions)):
    print(f"Question {i+1}: (for Rs. {prices[i]})")
    print(questions[i][0])

    for j in range(len(questions[i][1])):
        print(f"{j+1}. {questions[i][1][j]}")

    answer = int(input("Enter your answer: "))
    if answer == -1:
        skip = skip - 1
        if skip < 0:
            print("--------------------------")
            print("You have used all your chances to skip a question!")
            print("You Win a price of Rs.", price)
            print("Game Over!")
            print("--------------------------")
            break
        else:
            print("You have", skip, "chances left to skip a question!")
            continue
    else:
        print("--------------------------")
        if answer == 0:
            print("You quit the game!")
            print("You Win a price of Rs.", price)
            print("Game Over!")
            break
        elif answer - 1 == questions[i][2]:
            price = price + prices[i]
            print("Correct answer!")
            print("You won Rs.", prices[i])
            print("Your current price is Rs.", price)
        else:
            print("Incorrect answer!")
            print("You Win a price of Rs.", price)
            print("Game Over!")
            break
        print("--------------------------")
        print("Ready for the next question?")
else:
    print("Congratulations! You won the game!")
    print("You Win a price of Rs.", price)
    print("Game Over!")
