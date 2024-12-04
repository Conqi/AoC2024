import time
start_time = time.perf_counter()

grid = []
xmas_counter = 0
masmas_counter = 0

for input in open("Day04/input.txt"):
    grid+=list(input.rstrip())

line_length = len(input)
grid_length = len(grid)

for i in range(grid_length):
    if grid[i] == "X":
        #check right
        if i%line_length < line_length-3 and grid[i+1] == "M" and grid[i+2] == "A" and grid[i+3] == "S":
            xmas_counter += 1
        #left check
        if i%line_length > 2 and grid[i-1] == "M" and grid[i-2] == "A" and grid[i-3] == "S":
            xmas_counter += 1
        #up check
        if i>=line_length*3 and grid[i-line_length] == "M" and grid[i-2*line_length] == "A" and grid[i-3*line_length] == "S":
            xmas_counter += 1
        #down_check
        if i<=grid_length-line_length*3 and grid[i+line_length] == "M" and grid[i+2*line_length] == "A" and grid[i+3*line_length] == "S":
            xmas_counter += 1
        #right down check
        if i%line_length < line_length-3 and i<=grid_length-line_length*3 and grid[i+line_length+1] == "M" and grid[i+2*line_length+2] == "A" and grid[i+3*line_length+3] == "S":
            xmas_counter += 1
        #right up check
        if i%line_length < line_length-3 and i>=line_length*3 and grid[i-line_length+1] == "M" and grid[i-2*line_length+2] == "A" and grid[i-3*line_length+3] == "S":
            xmas_counter += 1
        #left down check
        if i%line_length > 2 and i<=grid_length-line_length*3 and grid[i+line_length-1] == "M" and grid[i+2*line_length-2] == "A" and grid[i+3*line_length-3] == "S":
            xmas_counter += 1
        #left up check
        if i%line_length > 2 and i>=line_length*3 and grid[i-line_length-1] == "M" and grid[i-2*line_length-2] == "A" and grid[i-3*line_length-3] == "S":
            xmas_counter += 1
    if grid[i] == "A" and 0 < i%line_length < line_length-1 and line_length <= i <= grid_length-line_length:
        #M S
        # A
        #M S
        if grid[i-line_length-1] == "M" and grid[i-line_length+1] == "S" and grid[i+line_length-1] == "M" and grid[i+line_length+1] == "S":
            masmas_counter +=1
        #M M
        # A
        #S S
        elif grid[i-line_length-1] == "M" and grid[i-line_length+1] == "M" and grid[i+line_length-1] == "S" and grid[i+line_length+1] == "S":
            masmas_counter +=1
        #S M
        # A
        #S M
        elif grid[i-line_length-1] == "S" and grid[i-line_length+1] == "M" and grid[i+line_length-1] == "S" and grid[i+line_length+1] == "M":
            masmas_counter +=1
        #S S
        # A
        #M M
        elif grid[i-line_length-1] == "S" and grid[i-line_length+1] == "S" and grid[i+line_length-1] == "M" and grid[i+line_length+1] == "M":
            masmas_counter +=1

print(xmas_counter)
print(masmas_counter)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Finished in {elapsed_time:.6f}")