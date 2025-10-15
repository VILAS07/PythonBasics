words=['apple','orange','grape']
s=0
for i in range(len(words)):
    for j in words[i]:
        if j == 'a':
            s += 1
            print()
        elif j == 'e':
            s += 1
        elif j == 'i':
            s += 1
        elif j == 'o':
            s += 1
        elif j== 'u':
            s += 1
    print(f"{words[i]} -> {s}")