# import copy

# row = [[] for i in range(15)]
# # row[0] = [3]
# # row[1] = [7,4]
# # row[2] = [2,4,6]
# # row[3] = [8,5,9,3]
# row[0] = [75]
# row[1] = [95,64]
# row[2] = [17,47,82]
# row[3] = [18,35,87,10]
# row[4] = [20,04,82,47,65]
# row[5] = [19,01,23,75,03,34]
# row[6] = [88,02,77,73,07,63,67]
# row[7] = [99,65,04,28,06,16,70,92]
# row[8] = [41,41,26,56,83,40,80,70,33]
# row[9] = [41,48,72,33,47,32,37,16,94,29]
# row[10] = [53,71,44,65,25,43,91,52,97,51,14]
# row[11] = [70,11,33,28,77,73,17,78,39,68,17,57]
# row[12] = [91,71,52,38,17,14,91,43,58,50,27,29,48]
# row[13] = [63,66,04,68,89,53,67,30,73,16,69,87,40,31]
# row[14] = [04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]

# # uniform cost search!
# class branch:
#     def __init__(self, cost=0, x=0,depth=0):
#         self.currCost = cost
#         self.x = x
#         self.depth = depth
#     def __cmp__(self,other):
#         if type(other) is branch:
#             return other.currCost - self.currCost
#         return 0

#     def __str__(self):
#         return str([self.currCost,self.x,self.depth])

#     def __repr__(self):
#         return str([self.currCost,self.x,self.depth])

# nodes = [branch()]
# nodes[0].currCost = row[0][0]
# while nodes[0].depth < len(row)-1:
#     nodes = sorted(nodes, key=lambda x: -x.currCost)
#     print(nodes)
#     a = copy.deepcopy(nodes[0])
#     a.depth = a.depth+1
#     a.currCost = a.currCost+row[a.depth][a.x+1]
#     a.x = a.x+1


#     nodes[0].depth = nodes[0].depth+1
#     nodes[0].currCost = nodes[0].currCost+row[nodes[0].depth][nodes[0].x]
#     print(nodes[0].currCost)

#     nodes.append(a)

# nodes = sorted(nodes, key=lambda x: -x.currCost)
# print(nodes)
# print(nodes[0].currCost)
data="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle = []
for line in data.split("\n"):
    if not line: continue
    triangle.append([int(w) for w in line.strip().split(' ')])
while len(triangle) > 1:
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i+1])
    del triangle[-1]
print triangle[0][0]
