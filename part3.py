#PART 3 - STAFF VERSION WITH HISTOGRAM
outcome_1 = 0
outcome_2 = 0
outcome_3 = 0
outcome_4 = 0
def restart(): #introducing the function for repeating the the whole process for part 3
    def passed_1():
        while True:
            try:
                global passed
                passed =int(input('please enter your credits at pass : '))
                if passed > 120 or passed < 0 or passed % 20 != 0:
                    print('Out of range.\n')
                    passed_1()
                break
            except ValueError:
                print('Integer required.\n')
    passed_1()

    def defer_1():        
        while True:
            try:
                global defer
                defer =int(input('please enter your credits at defer : '))
                if defer > 120 or defer < 0 or defer % 20 != 0:
                    print('Out of range.\n')
                    defer_1()
                break
            except ValueError:
                print('Integer required.\n')

    defer_1()

    def fail_1():        
        while True:
            try:
                global fail
                fail =int(input('please enter your credits at fail : '))
                if fail > 120 or fail < 0 or fail % 20 != 0:
                    print('Out of range.\n')
                    fail_1()
                break
            except ValueError:
                print('Integer required.\n')

    fail_1()


    total = passed + defer + fail
    
    def portion_1():
    
        if passed == 120 and defer == 0 and fail == 0:
            print('Progress')
            global outcome_1
            outcome_1 +=1
            
        elif passed == 100 and defer == 20 and fail == 0 :
            print('Progress (module trailer)')
            global outcome_2
            outcome_2 +=1

        elif passed == 100 and defer == 0 and fail == 20 :
            print('Progress (module trailer)')
            outcome_2
            outcome_2 +=1

        elif passed == 40 and defer == 0 and fail == 80:
            print('Exclude')
            global outcome_4
            outcome_4 +=1
            
        elif passed == 20 and defer==20 and fail == 80:
            print('Exclude')
            outcome_4
            outcome_4 +=1

        elif passed == 20 and defer==0 and fail == 100:
            print('Exclude')
            outcome_4
            outcome_4 +=1

        elif total > 120:
            print('Total incorrect.\n')
            passed_1()
            defer_1()
            fail_1()
            portion_1()

        elif 40 <= passed <= 80:
            print('Do not progress - module retriever')
            global outcome_3
            outcome_3
            outcome_3 +=1
        
        elif 20 <= defer <= 80:
            print('Do not progress - module retriever')
            outcome_3
            outcome_3 +=1
        
        elif 0 <= fail <= 60:
            print('Do not progress - module retriever')
            outcome_3
            outcome_3 +=1
          
        elif passed == 20 and 40 <= defer <= 100 and 0 <= fail <= 60:
            print('Do not progress - module retriever')
            outcome_3
            outcome_3 +=1

        elif passed == 0 and 60 <= defer <= 120 and 0 <= fail <= 60:
            print('Do not progress - module retriever')
            outcome_3
            outcome_3 +=1
            
        elif passed == 0 and 0 <= defer <= 40 and 80 <= fail <= 120:
            print('Exclude')
            outcome_4
            outcome_4 +=1

    portion_1()

    global total_outcome
    global outcome_1
    global outcome_2
    total_outcome = outcome_1 + outcome_2 + outcome_3 + outcome_4


restart() #calling the function so that the programs starts

#creating a function for histogram and total outcome
def horizontal_histogram():
    print('Progress ',outcome_1, '  : ' , ('* ' * outcome_1))
    print('Trailer ',outcome_2, '   : ' , ('* ' * outcome_2))
    print('Retriever ',outcome_3, ' : ' , ('* ' * outcome_3))
    print('Excluded ',outcome_4, '  : ' , ('* ' * outcome_4))
    print('\n')
    print(total_outcome,'outcomes in total.') 
    

while True:    
    while True:
        reply = str(input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: "))
        if reply in ('y', 'q'):
            break
    if reply == 'y':
        print('\n')
        restart() #function is called so it starts the program again
        continue
    elif reply == 'q':
        horizontal_histogram()#function is called so it quits and outputs the histogram and total outcome
        break
