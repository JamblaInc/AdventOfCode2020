import sys, re

graph = {}

for line in open('input.txt', 'r'):
    color = re.match('(.+?) bags', line).group(1)
    contains = re.findall('(\d+) (.+?) bag', line)
    graph[color] = contains
print(graph)
def has_shiny(color):
    if color == 'shiny gold': return True
    return any(has_shiny(c) for _, c in graph[color])
print(sum(has_shiny(c) for c in graph.keys()) - 1)

def count(bag_type):
    return 1 + sum(int(n)*count(c) for n,c in graph[bag_type])
print(count('shiny gold')-1)

# from collections import Counter

# bagInput = [line.strip('\n') for line in open("input.txt", "r")]
# validBags = set()
# checked = set()
# cleanInput = []
# containDict = {}

# bagInput = [x.replace(' bags contain', ',') for x in bagInput]
# bagInput = [x.replace(' bag.', ' ') for x in bagInput]
# bagInput = [x.replace(' bags.', '') for x in bagInput]
# bagInput = [x.replace(' bags', '') for x in bagInput]
# bagInput = [x.replace(' bag', '') for x in bagInput]
# bagInput = [x.split(', ') for x in bagInput]

# for bag in bagInput:
#     bag[:] = [x.strip() for x in bag]

# for i in bagInput:
#     newDict = {}

#     for x in i:
#         if x[0].isdigit():
#             newDict[x[2:]] = x[0]

#     containDict[i[0]] = newDict

# # for i in containDict:
# #     print(i, containDict[i])

# total = 0

# def getChildren(inputBag):
#     for bag, num in containDict[inputBag].items():
#         if bag is None or num is None:
#             return 0
#         return sum(int(num) * getChildren(bag))


# print(getChildren('shiny gold'))