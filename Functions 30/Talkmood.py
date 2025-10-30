import random


def talk_based_on_mood(m):
    mood = ["happy", "sad", "lazy", "angry", "motivated"]
    hap = ["Keep smiling! You’re confusing a lot of people 😁",
        "Happiness looks good on you ✨",
        "Smiles are free therapy — use them often 😊",
        "If you’re happy and you know it, code it! 🧑‍💻"]

    sa = [
        "Even the darkest night will end, and the sun will rise 🌅",
        "Crying doesn’t mean you’re weak — it means you’ve been strong too long 💧",
        "Cheer up! Sad spelled backward is DAS, and that’s not a word 😜",
        "It’s okay to not be okay sometimes 💙"
    ]

    la = [
        "You’re not lazy, you’re just on energy-saving mode 😴",
        "Procrastination level: Expert 🏆",
        "Don’t worry, the couch believes in you 🛋️",
        "You’ll do it tomorrow… probably 😅"
    ]

    an = [
        "Take a deep breath… or go punch a pillow first 😤",
        "Anger is like fire — warm if controlled, destructive if ignored 🔥",
        "Don’t let anger control you; you’re the main character 😎",
        "Count to 10. If still angry, count to 1000 😬"
    ]

    mo = [
        "Push yourself! Because no one else is going to do it for you 💪",
        "Discipline beats motivation — start small, stay consistent 🚀",
        "Don’t wish for it. Work for it 🔥",
        "Dream big, but code bigger 👨‍💻"
    ]

    if  m=='happy':
        return random.choice(hap)
    elif m=='sad':
        return random.choice(sa)
    elif m == 'lazy':
        return random.choice(la)
    elif m=='angry':
        return random.choice(an)
    elif m=='motivated':
        return random.choice(mo)
    else:
        return None


m=input('enter your mood : ').lower()
print(talk_based_on_mood(m))


