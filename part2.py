#PART 2 - STUDENT VERSION (VALIDATION)
total=int(120)
#creating a function for passed, defer , fail so that it can be called.
def passed_1():
    while True:
        #error is handled here
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
        #error is handled here
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
        #error is handled here
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
#function portion_1 is created so that it can be called under the total incorrect condition so that it can continue.
def portion_1():
    
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

    elif total > 120:
        print('Total incorrect.\n')
        passed_1()
        defer_1()
        fail_1()
        portion_1()
        
        


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




portion_1()
















