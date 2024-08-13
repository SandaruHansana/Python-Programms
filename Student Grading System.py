

#Variables

pass_c = 0
defer_c = 0
fail_c = 0

progress = 0
progress_trailer = 0
exclude = 0
retriver = 0

progress_list=[]
progress_trailer_list=[]
exclude_list=[]
retriver_list=[]

output_list={}

#Get inputs of Volume of credits & student_id

while True:
    credit_range = [0, 20, 40, 60, 80, 100, 120]
    try:
        student_id=input('Enter your student id - ')
        if len(student_id)==8 and student_id[0]=="w":
            while True: 
                pass_c = int(input('Please enter your credits at pass: '))
                if pass_c not in credit_range:
                    print('out of range')
                else:
                    break
            while True:
                defer_c = int(input('Please enter your credits at defer: '))
                if defer_c not in credit_range:
                    print('out of range')
                else:
                    break
            while True:
                fail_c = int(input('Please enter your credits at fail: '))
                if fail_c not in credit_range:
                    print('out of range')
                else:
                    break
        else:
            print("Enter valid input")
            continue

#Process and Print of outcomes 

        while pass_c+defer_c+fail_c==120:
            if pass_c == 120:  
                print('Progress')
                progress += 1
                progress_list=["progress-"+str(pass_c)+","+str(defer_c)+","+str(fail_c)]
                output_list[student_id]=(progress_list)
                break
            elif pass_c == 100:
                print('Progress (module trailer)')
                progress_trailer += 1
                progress_trailer_list=["progress (module trailer)-"+str(pass_c)+","+str(defer_c)+","+str(fail_c)]
                output_list[student_id]=(progress_trailer_list)
                break
            elif 60 < fail_c <= 120:
                print('Exclude')
                exclude += 1
                exclude_list=["exclude-"+str(pass_c)+","+str(defer_c)+","+str(fail_c)]
                output_list[student_id]=(exclude_list)
                break
            elif 0 <= fail_c <= 60:
                print('Module retriever')
                retriver += 1
                retriver_list=["do not progress-module retriver-"+str(pass_c)+","+str(defer_c)+","+str(fail_c)]
                output_list[student_id]=(retriver_list)
                break
        else:
            print('Total incorrect')
            print('\n')

    except ValueError:  
        print('Integer required')

#Ask to continue or quit programme        

    need_to_continue = str(input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: "))
    print('\n')

    if need_to_continue == 'y':
        continue    
    elif need_to_continue == 'q':

#Histogram
        
        print('-'*50)
        print('\nHistogram\n')
        print('Progress', progress, ' :', progress*'*')
        print('Trailer', progress_trailer, ' :', progress_trailer*'*')
        print('Retriever', retriver, ' :', retriver*'*')
        print('Excluded', exclude, ' :', exclude*'*', '\n')
        print((progress + progress_trailer + retriver + exclude), ' outcomes in total')
        print('-'*50)

#Print the result from dictionary

        result = str(output_list).strip('}{').replace('[', '').replace(']', '').replace("'",'')
        print(result)
        break
    else:
        break
