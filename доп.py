
# string_J = int(input('Введите оценки ученика Johnny через пробел:'))
# string_B = input('Введите оценки ученика Bilbo через пробел:')
# string_S = input('Введите оценки ученика Steve через пробел:')
# string_K = input('Введите оценки ученика Khendrik через пробел:')
# string_A = input('Введите оценки ученика Aaron через пробел:')

grades_j = [5, 3, 3, 5, 4]
len_j = "53354"
j = (sum(grades_j)/len(len_j))
grades_b = [2, 2, 2, 3]
len_b = "2223"
b = (sum(grades_b)/len(len_b))
grades_s = [4, 5, 5, 2]
len_s = "4552"
s = (sum(grades_s)/len(len_s))
grades_k = [4, 4, 3]
len_k = "443"
k = (sum(grades_k)/len(len_k))
grades_a = [5, 5, 5, 4, 5]
len_a = "55545"
a = (sum(grades_a)/len(len_a))
print({f'Johnny: {j}, Bilbo: {b}, Steve: {s}, Khendrik: {k}, Aaron: {a}'})


