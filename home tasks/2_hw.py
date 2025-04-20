#задача 1
print ('задача 1')


def task_1() -> tuple:
    a: int = 1
    b: float = 1.2
    c: str = 'строка'
    d: list = [1, 2, 3]
    e: bool = True
    return a, b, c, d, e

task_1()
print(task_1())
for element in task_1():
    print(element, type(element))

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
