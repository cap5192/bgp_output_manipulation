file = open("bgp.txt", 'r')
data = file.readlines()
new_data = []

for i in range(len(data)):
    if i > 16:
        new_data.append(data[i].split())
for i in range(len(new_data)):
    # ['10.100.1.0' '4''200']
    each_neighbor = new_data[i]
    for x in range(len(each_neighbor)):
        if x == 9:
            state = each_neighbor[x]
            if state.isdigit() == True:
                if state > "0":
                    print("done")


# read_line = []
# for i in range(len(data)):
#     if i >= 17:
#         new_data.append(data[i])
# for i in new_data:
#     x = i.split()
#     read_line.append(x)
#
# for i in range(len(read_line)):
#     entry = read_line[i]
#     for x in range(10):
#         if x == 9:
#             if entry[9].isdigit() == True:
#                 if entry[9] > "0":
#                     print(f"Neighbor {entry[0]} is up!")

