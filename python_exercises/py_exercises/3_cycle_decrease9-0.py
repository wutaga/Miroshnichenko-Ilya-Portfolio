# Напишите код, выводящий следующее:
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0
for column in range(10):
    for row in range(column):
        print(" ", end=" ")
    for row in range(10-column):
        print(row, end=" ")
    print()