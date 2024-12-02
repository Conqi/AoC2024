safe_counter1 = 0
safe_counter2 = 0

for input in open("input"):
    line = [int(x) for x in input.split()]
    i = 0
    dampener_use = False
    mode = ""

    if line[0] > line[1]:
        mode = "descending"
    elif line[1] > line[0]:
        mode = "ascending"
    else: mode = "failed"

    if mode == "descending":
        for number in line[:-1]:
            i += 1
            if not 0 < number - line[i] < 4:
                new_line = line.copy()
                new_line.pop(i-1)
                j = 0
                for number in new_line[:-1]:
                    j += 1
                    if not 0 < number - new_line[j] < 4:
                        new_new_line = line.copy()
                        new_new_line.pop(i)
                        k = 0
                        for number in new_new_line[:-1]:
                            k += 1
                            if not 0 < number - new_new_line[k] < 4:
                                mode = "failed"
                                break
                        if mode != "failed":
                            break
                if mode != "failed":
                    break
            j = 0

    if mode == "ascending":
        for number in line[:-1]:
            i += 1
            if not 0 < line[i] - number < 4:
                new_line = line.copy()
                new_line.pop(i-1)
                j = 0
                for number in new_line[:-1]:
                    j += 1
                    if not 0 < new_line[j] - number < 4:
                        new_new_line = line.copy()
                        new_new_line.pop(i)
                        k = 0
                        for number in new_new_line[:-1]:
                            k += 1
                            if not 0 < new_new_line[k] - number < 4:
                                mode = "failed"
                                break
                        if mode != "failed":
                            break
                if mode != "failed":
                    break
            j = 0
    
    if mode != "failed":
        safe_counter2 += 1
        if j == 0:
            safe_counter1 += 1

print(safe_counter1, safe_counter2)

