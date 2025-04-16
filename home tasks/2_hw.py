#задача 1
print ('задача 1')
a: int = 1
b: float = 1.2
c: str = 'строка'
d: list = [1,2,3]
e: bool = True

def task_1(a: int,b: float,c: str,d: list,e: bool):
    return a,b,c,d,e
print (task_1(a,b,c,d,e))
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))


#задача 2
print ('задача 2')
def task_2 (a:list =[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a
print("task_2 = ", task_2()[0:3])
#последовательность - список


#задача 3
print ('задача 3')
def task_3(a:int):
    return a*a
print(task_3(4))
