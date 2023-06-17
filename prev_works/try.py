def func_1(x=1):
    print("Данная фунция пытается поделить целое число на 2.")
    if not(isinstance(x, int)):
        print("Получена на ввод СТРОКА. Пытаюсь привести число к целому типу")
        try:
            x=int(x)
            print(x)
            return(x/2)
        except ValueError:
            print("Вы ввели НЕ ЧИСЛО! Значение будет заменено на 1")
            x=1
            x=int(x)
            print(x)
            return(x/2)
    else:
        return (x/2)
            
def func_2(x):
    print("Данная фунция пытается умножить целое число на 4.")
    if not(isinstance(x, int)):
        print("Получена на ввод СТРОКА. Пытаюсь привести число к целому типу")
        try:
            x=int(x)
            print(x)
            return(x*4)
        except ValueError:
            print("Вы ввели НЕ ЧИСЛО! Значение будет заменено на 1")
            x=1
            x=int(x)
            print(x)
            return (x*4)
    else:
        return (x*4)        
x=input("Введите целое число: ")
y=func_1(x)
print ("x= "+str(x)+"\t,y= "+str(y) )
z=func_2(y)
print ("x= "+str(x)+"\t,y= "+str(y) +"\t,z= "+str(z) )

