outcome_1 = 0
outcome_2 = 0
outcome_3 = 0
outcome_4 = 0
#creating a function for histogram and total outcome
def horizontal_histogram():
    print('Progress ',outcome_1, '  : ' , ('* ' * outcome_1))
    print('Trailer ',outcome_2, '   : ' , ('* ' * outcome_2))
    print('Retriever ',outcome_3, ' : ' , ('* ' * outcome_3))
    print('Excluded ',outcome_4, '  : ' , ('* ' * outcome_4))
    print('\n')
    print(total_outcome,'outcomes in total.')

prog_list=[120,0,0]
print('Progress')
outcome_1 +=1

trailer_list_1=[100,20,0]
print('Progress (module trailer)')
outcome_2 +=1
trailer_list_2=[100,0,20]
print('Progress (module trailer)')
outcome_2 +=1

retriever_list_1=[80,20,20]
print('Do not progress - module retriever')
outcome_3 +=1
retriever_list_2=[60,40.20]
print('Do not progress - module retriever')
outcome_3 +=1
retriever_list_3=[40,40,40]
print('Do not progress - module retriever')
outcome_3 +=1
retriever_list_4=[20,40,60]
print('Do not progress - module retriever')
outcome_3 +=1

exclude_list_1=[20,20,80]
print('Exclude')
outcome_4 +=1
exclude_list_2=[20,0,100]
print('Exclude')
outcome_4 +=1
exclude_list_3=[0,0,120]
print('Exclude')
outcome_4 +=1

print('\n')

total_outcome = outcome_1+ outcome_2 + outcome_3 + outcome_4

horizontal_histogram()
