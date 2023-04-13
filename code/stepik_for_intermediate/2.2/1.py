count_iteration = int(input())

first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0

for i in range(1, count_iteration + 1):
    coordinates = input().split(" ")
    coord_x, coord_y = int(coordinates[0]), int(coordinates[1])


    if coord_x > 0 and coord_y > 0:
        first_quarter += 1
    elif coord_x < 0 and coord_y > 0:
        second_quarter += 1
    elif coord_x < 0 and coord_y < 0:
        third_quarter += 1
    elif coord_x > 0 and coord_y < 0:
        fourth_quarter += 1

print(f"Первая четверть: {first_quarter}")
print(f"Вторая четверть: {second_quarter}")
print(f"Третья четверть: {third_quarter}")
print(f"Четвертая четверть: {fourth_quarter}")