def task_1():
        a=[]
        for i in range(0,100):
                if i % 2 == 0:
                        a.append(i)
        print('task#1 - ',a)

task_1()

def task_2(a,b):
        x=a*b
        print('task#2 - ',x)

task_2(2,2)


def task_3(word):
        if word == word[::-1]:
                print('task#3 - True')
        else:
                print('task#3 - False')

                
task_3('dad')
task_3('privet')

def task_4(a,b):
        x = 0
        for i in a:
                if i == b:
                        x = x + 1
        print('task#4 - ',x)

task_4([1,2,3,4,4,4,4,4,4], 4)
        
        
