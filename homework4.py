#immutable_var = 'Anar', 22, 2001, 2024
#print(immutable_var)
#immutable_var[0][0] = 'Askerov'
#print(immutable_var)

mutable_list = ['Anar', 22, 2001, 2024]
print(mutable_list)
mutable_list.append(True)
mutable_list[0] = 'Askerov'
mutable_list.remove(2001)
mutable_list.extend([5])
print(mutable_list)
