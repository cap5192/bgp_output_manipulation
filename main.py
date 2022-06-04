file = open("bgp.txt", 'r')
data = file.readlines()
new_data = []
read_line = []
for i in range(len(data)):
    if i >= 17:
        new_data.append(data[i])
for i in new_data:
    x = i.split()
    read_line.append(x)

for i in range(len(read_line)):
    entry = read_line[i]
    for x in range(10):
        if x == 9:
            if entry[9].isdigit() == True:
                if entry[9] > "0":
                    print(f"Neighbor {entry[0]} is up!")