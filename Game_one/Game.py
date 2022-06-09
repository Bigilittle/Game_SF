import numpy as np


def randome_number(number:int = 1) -> int:

    ''' Данная функция отгадывает число, учитывая данные о том, больше чило, или меньше

    Args:
       number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: количесвто попыток
    '''

    first=1
    last=101
    count=0
    
    while True:

        count+=1
        comp_number=np.random.randint(first,last)

        if comp_number>number:   #Если число получилось больше, то ставим ограничение, измянее переменную last
            last=comp_number   #благодаря этому теперь отрезок в котором мы можем взять число, уменьшено 
        elif comp_number<number: 
            first=comp_number+1
        else:
            break  #выход из цикла

    return count   
            

def Count_func_randome_number(random_funs):
    '''За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
       -

    Returns:
        int: среднее количество попыток
    '''

    count_ls = [] # список для сохранения количества попыток
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_funs(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Данный алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
    

if __name__=='__main__':    
    Count_func_randome_number(randome_number)
