num_lst = [1, 4, 6, 9, 10]

biggest_num = None

for number in num_lst:
    if biggest_num is None or number > biggest_num:
        biggest_num = number

print(biggest_num)

my_name = "pradeep"

letter = list(my_name)

print(letter)