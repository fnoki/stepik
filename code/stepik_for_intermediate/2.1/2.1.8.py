count_people = int(input())
step_kill = int(input())

list_of_people = list(range(1, count_people + 1))
s = 0
for i in range(1, count_people + 1):
    s = (s + step_kill) % i
print(s + 1)