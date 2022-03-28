#PART 1 - STUDENT VERSION

#passed-variable used to promt and represent credit at pass
#defer-variable used to promt and represent credit at defer
#fail-variable used to promt and represent credit at fail

passed=int(input('please enter your credits at pass : '))
defer=int(input('please enter your credits at defer : '))
fail=int(input('please enter your credits at fail : '))

#if condition is used for Progression outcomes
if passed == 120 and defer == 0 and fail == 0:
    print('Progress')

elif passed == 100 and defer == 20 and fail == 0 :
    print('Progress (module trailer)')

elif passed == 100 and defer == 0 and fail == 20 :
    print('Progress (module trailer)')

elif passed == 40 and defer == 0 and fail == 80:
    print('Exclude')

elif passed == 20 and defer==20 and fail == 80:
    print('Exclude')

elif passed == 20 and defer==0 and fail == 100:
    print('Exclude')
    
elif 40 <= passed <= 80:
    print('Do not progress - module retriever')

elif 20 <= defer <= 80:
    print('Do not progress - module retriever')

elif 0 <= fail <= 60:
    print('Do not progress - module retriever')

elif passed == 20 and 40 <= defer <= 100 and 0 <= fail <= 60:
    print('Do not progress - module retriever')

elif passed == 0 and 60 <= defer <= 120 and 0 <= fail <= 60:
    print('Do not progress - module retriever')

elif passed == 0 and 0 <= defer <= 40 and 80 <= fail <= 120:
    print('Exclude')
