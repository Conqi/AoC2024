import time
start_time = time.perf_counter()

result1 = 0
result2 = 0
active = True
character = []

def check_second_number(j):
    if character[j+1].isdecimal() and character[j+2].isdecimal() and character[j+3].isdecimal() and character[j+4] == ")":
        return(int(character[j+1]+character[j+2]+character[j+3]))
    elif character[j+1].isdecimal() and character[j+2].isdecimal() and character[j+3] == ")":
        return(int(character[j+1]+character[j+2]))
    elif character[j+1].isdecimal() and character[j+2] == ")":
        return(int(character[j+1]))
    else: return(0)

for input in open("Day03/input.txt"):
    character+=list(input.rstrip())

for i in range(len(character)):
    if character[i] == "d" and character[i+1] == "o" and character[i+2] == "(" and character[i+3] == ")":
        active = True
        i+=4
    elif character[i] == "d" and character[i+1] == "o" and character[i+2] == "n" and character[i+3] == "'" and character[i+4] == "t" and character[i+5] == "(" and character[i+6] == ")":
        active = False
        i+=6
    elif character[i] == "m" and character[i+1] == "u" and character[i+2] == "l" and character[i+3] == "(" and character[i+4].isdecimal():
            if character[i+5] == ",":
                number1 = int(character[i+4])
                number2 = check_second_number(i+5)
                result1 += number1*number2
                if active == True: result2 += number1*number2
                i+=9
            elif character[i+5].isdecimal() and character[i+6] == ",":
                number1 = int(character[i+4]+character[i+5])
                number2 = check_second_number(i+6)
                result1 += number1*number2
                if active == True: result2 += number1*number2
                i+=8
            elif character[i+5].isdecimal() and character[i+6].isdecimal() and character[i+7] == ",":
                number1 = int(character[i+4]+character[i+5]+character[i+6])
                number2 = check_second_number(i+7)
                result1 += number1*number2
                if active == True: result2 += number1*number2
                i+=7                
            else: i+=4

print(result1)
print(result2)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Finised in {elapsed_time:.6f}")
