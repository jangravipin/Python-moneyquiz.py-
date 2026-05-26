questions = [
    ["Who is Virat Kohli?", "Footballer", "Actor", "Model", "Cricketer", 4],
    ["What is the capital of Germany?", "Rome", "London", "Berlin", "Paris", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the largest mammal?", "Elephant", "Shark", "Blue Whale", "Giraffe", 3],
    ["Who wrote Romeo and Juliet?", "Charles Dickens", "Jane Austen", "Homer", "William Shakespeare", 4],
    ["What is the square root of 64?", "8", "6", "12", "16", 1],
    ["Which country known as the Land of the Rising Sun?", "China", "Japan", "South Korea", "Indonesia", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the fastest land animal?", "Cheetah", "Tiger", "Horse", "Elephant", 1],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the smallest country is the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 1]
]

prizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 150000]

i = 0
for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

# Check whether the answer is correct or not

    answer = int(input("Enter your answer : "))
    if(question[5] == answer):
        print("Correct Answer!")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break

    print(f"You won {prizes[i]}")
    i += 1