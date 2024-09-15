import math


def discriminant(a:float|int, b:float|int, c:float|int)-> float|int:
    return b*b-4*a*c


def discriminant_check(D:float|int)-> int:
    if abs(D) < 0.000001:
        return 1
    if D > 0:
        return 2

    return 0

#def find_quadratical_equation():#



def solve_quadratical_equation(a:float|int, b:float|int, c:float|int)->list[float]:
    D = discriminant(a, b, c)
    check = discriminant_check(D)
    if check == 0:
        return []
    if check == 1:
        x1 = -b / (2*a)
        return[x1]
    return [-b + math.sqrt(D) / 2 / a , -b - math.sqrt(D) / 2 / a]


#print(solve_quadratical_equation(1, 0, -9)) 
# x**2 -9 = 0

def find_a(task:str)->float:
    # x.find('x^2')
    return float(task[:task.find('x^2')])
# 4*x^2 - 2*x + 1 = 0   
#4.5x^2+2x+1
def find_b(task:str)->float:
    # x.find('x^2')
    tmp= task[task.find('x^2')+3:]
    peremennaya = tmp[:tmp.find('x')]
    if peremennaya[0] == '+':
        peremennaya = peremennaya[1:]
    return float(peremennaya)

def find_c(task:str)->float:
    tmp= task[task.find('x^2')+3:]
    peremennaya = tmp[tmp.find('x')+1:]
    if peremennaya[0] == '+':
        peremennaya = peremennaya[1:]
    return float(peremennaya)


def final_calculator(stroka:str)-> list[float]:
    stroka = stroka.replace(' ', '')
    a = find_a(stroka)
    b = find_b(stroka)
    c = find_c(stroka)
    print(a, b, c)
    return solve_quadratical_equation(a, b, c)

print(final_calculator('4x^2-4x+1'))


