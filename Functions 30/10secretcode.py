
import random
def secret_code(word):
    s= ['@','#','$','%','&','!','?','*']
    code = ""
    for i in word:
        code += random.choice(s)
    return code

print(secret_code("HELLO"))
