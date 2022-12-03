f = open("input.txt", "r")
line_list = f.readlines();
max = []
sum = 0
for x in line_list:
    if len(x) == 1:
        max.append(sum);
        sum = 0;
    else:
        sum += int(x);

max.sort(reverse=True)
print(max[0]+max[1]+max[2])