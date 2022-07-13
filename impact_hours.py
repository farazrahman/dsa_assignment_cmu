from pathlib import Path


# 1. first of all create a function that takes each individual file as input
# 2. Then iterates over these files to find the life guard that has minimum impact on the pool duty in terms of hours
# 3. Outputs the hour of the minimum impact lifeguard as the hour that still needs to be covered for

def get_files(filepath):
    with open(filepath, 'r') as reader:
        data = [x.rstrip('\n').split(" ") for x in reader.readlines()]
        list = [[int(i) for i in sublist] for sublist in data]
        list.pop(0)
        list = sorted(list)
        # print(list)
        return list


# def impact_factor(filepath):
#     list = get_files(filepath)
#     for sublist in iter(list):
#
#         print(next(sublist[0]))

# def impact_factor(filepath):
#     list = get_files(filepath)
#     for curr, next in zip(list, list[1:]):
#         # print(curr, next)
#         if next[0] < curr[1]:
#             impact = (curr[1]-curr[0])-(curr[1]-next[0])
#             print(curr, impact)

def impact_factor(filepath):
    list = get_files(filepath)
    for i in range(len(list)):
        if i == 0:
            curr = list[i]
            next = list[i+1]
            impact = (curr[1]- curr[0])-(curr[1]-next[0])
            print(curr, impact)

        elif i == len(list)-1:
            prev = list[i - 1]
            curr = list[i]
            impact = (curr[1] - curr[0]) - (prev[1] - curr[0])
            print(curr, impact)

        else:
            prev = list[i-1]
            curr = list[i]
            next = list[i+1]
            impact = (curr[1]- curr[0])-(prev[1]-curr[0])-(curr[1]-next[0])
            print(curr, impact)




if __name__ == '__main__':
    # get_files('CMU MSSM Summer Programming Assignments/1.in')
    impact_factor('CMU MSSM Summer Programming Assignments/1.in')
