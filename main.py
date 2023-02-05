tasks = 8
first_student = {2, 3, 6, 7}
second_student = {1, 6, 7, 8}
new_student = first_student | second_student
to_be_done= []
for i in range(1, tasks):
    if i not in new_student:
        to_be_done.append(i)
print(len(list(to_be_done)))
