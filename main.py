file = open("bgp.txt", "r")
data = file.readlines()[17:]
formatted_data = []
neighbors = []
for i in range(len(data)):
    formatted_data.append(data[i].split())
for i in range(len(formatted_data)):
    each_line = formatted_data[i]
    # ['10.100.1.0', '4', '200', '26', '22', '199', '0', '0', '00:14:23', '23']
    for x in range(len(each_line)):
        if x == 9:
            if each_line[9].isdigit() == True:
                if int(each_line[9]) > 0:
                    neighbors.append(each_line[0])

print("Up neighbors are:")
for i in neighbors:
    print(i)
