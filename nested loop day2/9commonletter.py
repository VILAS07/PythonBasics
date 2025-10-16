names = ["Anu", "Ben", "Neha", "Leo"]

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        # Find common letters (case-insensitive)
        common = set(names[i].lower()) & set(names[j].lower())

        if common:
            print(f"{names[i]} & {names[j]} → common letter: {', '.join(sorted(common))}")
