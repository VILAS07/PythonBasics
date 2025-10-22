quiz = [
    {
        "question": "What is the capital of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. John Keats"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Arctic Ocean", "C. Indian Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1947", "B. 1950", "C. 1945", "D. 1935"],
        "answer": "A"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
        "answer": "C"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. Isaac Newton"],
        "answer": "B"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "options": ["A. Asia", "B. Africa", "C. Australia", "D. South America"],
        "answer": "B"
    },
    {
        "question": "How many players are there in a cricket team (on-field)?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 9"],
        "answer": "B"
    },
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["A. Horse", "B. Elephant", "C. Camel", "D. Donkey"],
        "answer": "C"
    },
    {
        "question": "Who is the current Prime Minister of India (as of 2025)?",
        "options": ["A. Rahul Gandhi", "B. Narendra Modi", "C. Arvind Kejriwal", "D. Amit Shah"],
        "answer": "B"
    },
    {
        "question": "Which festival is known as the 'Festival of Lights' in India?",
        "options": ["A. Holi", "B. Diwali", "C. Dussehra", "D. Eid"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Which country hosted the FIFA World Cup 2022?",
        "options": ["A. Qatar", "B. Russia", "C. Brazil", "D. Germany"],
        "answer": "A"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 90°C", "B. 95°C", "C. 100°C", "D. 110°C"],
        "answer": "C"
    }
]
import  random
q=random.sample(quiz,5)
s=0
for i in q:
    print(i["question"])
    ans=input(i['options'])
    if ans.upper()==i['answer']:
        print('correct')
        s+=1
    else:
        print('incorrect')
print(f"Your Score Is {s}/5")


