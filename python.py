# сортировка 
# jun - пузырек / вставки / набор Q(n²)

# middle - быстрая сортировка / слияние q(nlogn)

# специфика отдельного языка python (
# sorted/list.sort - timesort (стабильный(q(nlogn)))
# и при почти отсоритрованном q(n)
# )

# пузырек - сосединие пары, большой элемент всплывает вправо

# выбор - на позицию i ставим минимум из хвоста 
# и потом происходит сортировка 

# вставки - берем следующий элемент и вдвигаем в уже отсортированный префикс поэтому на почти отсортированным почти линейно выполняется

# quick sort - 
# выбор опорного элемента
# разделение на три группы
# рекурсия
# сборка 

# лечение худшего случая быстрой сортировки - случайно брать pivot (опорный элемент) 
# медиана трех - беретие медиану (среднее значение из трех элементов массива - первый  средйний послдений

# merge - рекурсивно делится пополам до тех пор пока каждый подмасив не будет состоять из одного элемента 
# далее идет слияние отсортированных в один новый масив
# гланая проблема - память, каждый подмассив жрет память

# heap 
# построить max-кучу по принципу o(n) и n раз снимать корень

# timsort 
# мелкие досортироваыет вставками, крупные сливает как merge 
# функция sorted в питоне - на реальных данных быстре голого merge/quick 

# в продакшене возьму sorted/list.sort(timesort)
# свою пшу только если прооят алгоритм или нужен особвый вариант внешнй сортировки

# O(1) - всегда одно и тоже
# O(log n ) - каждый шаг режет задачу пополам
# O(n) - один проход по массиву
# O(n²) вложенный цикл или двойной 
# O(n + k) - прошел массив  + диапозон значений
# O(n log n) - лучшая сортировка


# Quicksort
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    return (quicksort([x for x in array if x < pivot])
            + [x for x in array if x == pivot]
            + quicksort([x for x in array if x > pivot]))


# merge - тсбальиный всегда по n(log n)

def mergesort(array):
    if len(array) <= 1:
        return array
    merge = len(array) // 2
    L,R = mergesort(array[:merge]), mergesort(array[merge:])
    i = j = 0
    out = []

    while i < len(L) and j < len(R):
        if L[i] > R[j]: # дает стабильность
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1

    return out + L[i:] + R[j:]


# heap 
import heapq

def heap(array):
    h = array[:]
    heapq.heapify(h)
    return [heapq.heapify(h) for _ in range(len(h))]

# time sort = merge + insertion 




# Паттерны на масивах и строках

# 1 - бинарный поиск 
# массив уже отсортирован или ответ число и при увлеличении кандитата условия из нет становится да
# наивный перебор O(n) а половинками O(logn)
# Каждый шаг смотрим на середину и выкидываем половину
# базовый поиск и левая вставка


# нужен когда массив уже отсортирован и ответ число и при увеличении каднтита условия из мало становитяс хватит
# каждый шаг выкидываем половину время по O(log n), O(n)
# когда брать - найтич исло, первую последную позицию, корень 
# минимальная скорость при которой успеем что-то 
# когда не брать - массив не отсортирован или сортировать дорого тогда словарь или линейный подход 

def binary_search(array, target):
    left = 0
    right = len(array) - 1 
    while left <= right:
        mid  = (left + right) // 2

        if array[mid] == target :
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1 # если элемента нет left - индекс куда его нужно ставить 
    
# левая граница (первое вхождение или место вставки)

def lower_bound(array, target):
    left = 0
    right = len(array) - 1 
    while left <= right:
        mid  = (left + right) // 2

        if array[mid] == target :
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return left 
    

# два указателя
# два индекса. поиск идет либо с концов на встречу, либо оба слева на право. смысл поска - убрать вложенный цикл 

# пара с суммой на отсортированном массиве 
# сумма маленькая двигаем влево, большая - вправо 
# каждый массив один раз проходит O(n) после сортировки 

# когда брать - пара или тройка которую нужно найти одновременно, палиндром/контейнер с водой/ слить два отсортированных / убрать дубилкаты 
# если массив не отсоритрованный sort либо словарь 

def two_sum_sorted(array, target):
    left = 0
    right = len(array) - 1 

    while left < right: 
        sum = array[left] + array[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        else: 
            right += 1

# 3sum - сортировка для каждого i два указателя на кхвосте 
# дубликаты пропускаем иначе один и тот же триплет вылетет много раз 
# и того O(n²) и это оптимально для каждой задачи в общем случае 

def three_sum(array):
    array.sort()
    result = []
    for first in range(len(array)):
        if first > 0 and array[first] == array[first-1]:
            continue
        left = first + 1
        right = len(array) - 1 
        while left < right:
            sum = array[first] + array[right] + array[left]

            if sum == 0:
                result.append(array[first] + array[left] + array[right])
                left +=1
                while left < right and array[left] == array[left - 1]:
                    left +=1
            elif sum < 0:
                left += 1
            else: 
                right +=1
    return result


# хеш таблица 
# нужна когда важен непорядок а 
# - уже видел ? dict и set 
# сколько раз ? dict как счетчик
# если дополения до суммы ?  two sum для неостроитрованного массива
# среденее O(1) на проверку 
# dict и set и частота O(1) это главный способ превратить O(n²) когда порядок не важен

# когда брать - two sum без сортирови, дубликаты, анограмы, частоты подмассив с суммой
# когда не брать - нужен порядок или неприрывный кусок с ограничениями это окно 
def two_sum(array, target):
    # значение -> индекс где мы его уже встречали
    index_by_value = {}
    for index, value in enumerate(array):
        # какое число должно стоять раньше
        need = target - value
        if need in index_by_value:
            return index_by_value[need], index
        # кладем текующее после проверки иначе value + value взял элемент дважды 
        index_by_value[need] = index 

# групировка анограм одно и тоже слово после сортировки слов дает один ключ
def group_anagrams(array):
    group = {}
    for word in array:
        # анаграммовые одинаковые ключи (eat и tea  -> (e,a,) -> одинаковый ключ)
        key = tuple(sorted(word))
        # список в ключ словаре нельзя, а кортеж можно он хешируется
        group.setdefault(key, []).append(word)
    return list(group.values())

# подмассив с сумой таргет. окно ломется на отрицательных числах префикс + словаря 

def count_subbray_with_sum(array,target):
    # сколько раз встречался такой префикс 
    # префикс 0 встречался один раз и мы ставим пустой кусок перед началом
    count_by_prefix = {0:1} # хеш это и есть словарь который хранит какой префикс 
    prefix_sum = 0
    answer = 0

    for value in array:
        prefix_sum += value 

        # ищем - если раньше был префикс (текущий таргет) то кусок между ними дает ровно target 
        answer += count_by_prefix.get(prefix_sum - target,0)
        count_by_prefix[prefix_sum] = count_by_prefix.get(prefix_sum) + 1
    return answer

# префикс это не кусок строки и не начало слова, это сумма массива с начала до текущей позиции 
numbers = [1,2,3,4] # префикс сумма равно 10
words = ["cat", "biba", "aboba"]
# count_by_prefix = {0:a,1:ab,2:abo}
# кусок [2,3] - это индексы 1,2 префиксы до 2 индекса - 6 
# префикс до 0 = 1 (все до куска )
# 6-1 = 5, и 2 +3 = 5
# идем по массиву один раз в словаарь поменим какой префикс уже встречался 
# и сколько раз на текущем prefix спрашиваем я уже видел prefix - target \
# если уже увидел то кусок между тем местом и текущим дает ровно target 
# поэтому связка называетяс префиксные суммы 

# по префиксу - окно ломется если в массиве есть минусы 
# а профикс = словарь работает всегда
# смысл идеи префикс prefix[right] - prefix[left-1] = target
# и текущий таргет  

# two sum префиксов нет - там ключ - само по себе число
# префикс появляется только когда спрашивают сумму непреривного куска 

# бинарка
# проверка есть ли число
numbers_task_1 = [1,4,8,3,7,11,25,40] 
target_task_1  = 7 
# провериь что есть таргет в массиве. вернуть индекс или -1 
# проверка первого вхождения 
numbers = [1,2,2,2,2,4,6]
target = 2 
# проверить самый левый индек где стоит 2 
# куда встаивть 
numbers = [30,20,10,40]
target = 25 
# числа нету, индекс вернуть куда его вставить чтобы ммассив стал отсоритрованным 


# Два указателя
# Пара с суммой 
numbers = [1,2,4,7,11]
target = 11
#Массив уже отсортирован верни два индекса ( любой порядок)
# Палиндром
text = "привет"
textp = "шалаш"
taxtw = "Нажал кабан на баклажан"
# Вернуть True false
# Слить два отсортированных массива 
left = [1,4,7] 
right = [2,3,5,8]
# два указателя как в merge верни один отсортированный список



# Хэш
# Two sum без сортировки 
numbers = [3,1,4,2] 
target = 6
# Верни два индекса не сортируй иначе индексы поедут
# Првоерка на дубликаты
numbers = [5,1,3,1]
numbers = [5,1,3]
# Верни True если какоето число уже встречалось дважды
# Анаграммы 





# бинарка 1 задание
numbers_task_1 = [1,4,8,3,7,11,25,40] 
target_task_1  = 7 

def binary_search(array, target):
    array.sort()
    left = 0
    right = len(array) - 1 
    while left <= right:
        mid  = (left + right) // 2

        if array[mid] == target :
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1

result_task_1 = binary_search(numbers_task_1, target_task_1)
print(result_task_1)



# задание 2
numbers = [1,2,2,2,2,4,6]
target = 2 

def binary_search(array, target):
    array.sort()
    left = 0
    right = len(array) - 1 
    while left < right:
        mid  = (left + right) // 2

        if array[mid] < target :
            right = mid + 1
        else:
            right = mid 
    return left
    
result_task_1 = binary_search(numbers, target)
print(result_task_1)


# задание 3 
numbers = [30,20,10,40]
target = 25 

def binary_search(array, target):
    array.sort()
    print(array)
    left = 0
    right = len(array) - 1 

    while left <= right:
        mid  = (left + right) // 2

        if array[mid] == target :
            right = mid - 1
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

result_task_1 = binary_search(numbers, target)
print(result_task_1)


# задание 4 
# Пара с суммой 
numbers = [1,2,4,7,11]
target = 11
#Массив уже отсортирован верни два индекса ( любой порядок)

def two_sum_sorted(array, target):
    print(array)
    left = 0
    right = len(array) - 1 

    while left < right: 
        sum = array[left] + array[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        else: 
            right -= 1
    return -1

result_task_1 = two_sum_sorted(numbers, target)
print(result_task_1)


# задание 5
# Палиндром
text = "привет"
textp = "шалаш"
textw = "Нажал кабан на баклажан"
# Вернуть True false

def palindrome(text):
    text = text.lower().replace(" ", "")
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome(text))
print(palindrome(textp))
print(palindrome(textw))

# задание 6 
# Слить два отсортированных массива 
left = [1,4,7] 
right = [2,3,5,8]
# два указателя как в merge верни один отсортированный список

def merge_array(arrayleft, arrayright):
    resultarray = []
    left = 0
    right = 0

    while left < len(arrayleft) and right < len(arrayright):
        if arrayleft[left] <= arrayright[right]:
            resultarray.append(arrayleft[left])
            left += 1
        else: 
            resultarray.append(arrayright[right])
            right += 1
    while left < len(arrayright): 
        resultarray.append(arrayright[right])
        right += 1

    while right < len(arrayleft):
        resultarray.append(arrayleft[arrayleft])
        left += 1
    return resultarray

# скользящее окно
# ответ — это непрерывный отрезок
# правый всегда подтягивается пока условие успешно
# каждый индекс входит и выходит один раз O(n)
# 
# максимум суммы окна длины 3 array =[2,1,5,1,3,2]

def max_sum_window(array,window_size):
    current_sum = sum(array[:window_size])
    best_sum = current_sum
    for right in range(window_size,len(array)):
        left_leaving = right - window_size
        current_sum += array[right] - array[left_leaving]
        best_sum = max(best_sum,current_sum)
    return best_sum

# плавяющая длина
# самая длинная подстрока без поворотов 
text = "abcabcbb"
def longest_substring_repeat(text):
    last_index_char = {}
    best_lenght = 0
    left = 0
    for right,char in enumerate(text):
        if char in last_index_char and last_index_char[char] >= left:
            left = last_index_char[char] + 1
        last_index_char[char] = right
        best_lenght = max(best_lenght,right - left + 1)
    return best_lenght

# right / char / повтор в окне / left / окно / длина / best

# 0       a   нет                 0      a       1      1
# 1       b   нет                 0      ab      2      2
# 2       c   нет                 0      abc     3      3
# 3       a   да старая а 0       1      bca     3      3
# 4       b   да старая б 1       2      cab     3      3
# 5       c   да старая на 2      3      abc     3      3
# 6       b   да b на 4 4>= 3     5      cb      2      3
# 7       b   да b на 6           7      b       1      3

# подстроки abc,bca,cab все длины 3, длинее нет
# зачем >= left в "abbc " на второй а (индекс 3) старая а стоит на 0
# к этому моменту left 
# если прыгнуть на 0 + 1 = 1 окно поедет назад — так нельзя
# условие сторый индекс >= left это и отсекает окно
# 
# 
# шаблон Плавающее окно всегда одно и тоже
# расширил Right добавил text[right] в состоянии (частоты суммы число различных)
# пока пл окно плохое — сдвиг left и убрал text[left] из состояния
# Окно всегда хорошее обновил ответ
# 
# минимум длины окна в котором сумма >= target числа неотрицательные 
# иначе левый край нельзя безопасно двигать 



# ответ (abc) — проверка >= left 
# обязательна старое вхождение левее окна уже мертвое на него нельзя прыгать
# шаблон любой задачи с окном расширения right — пока плохо сдвинул left и вычел
# состояние — обновил ответ

# когда не брать — непрерывный индексы или сумма ровно К при отрицательных числах

# Фиксированное окно
# numbers = []
# заполняете его случайными значениями от 1-15 (числа)
# кол значения 10к
# длина окна 5
# найти максимум сумму любого окна длины 5
# и макс окно с длиной 5
# засечь время import time
# 
# с засечко времени для сравнения 
# сделать обычный перебор значений каждых 5 элементов сумму l;


# стек и очередь
# стек - LFIO - послендний открыл первым закрыл 
# очередь - FIFO - кто раньше ушел пришел того раньше обработали 

# если касаемо питона - deque - очередь только тут  не list.pop(0)

def valid_parentthese(text):
    opening_close = {")":"(","]":"[","}":"{"}
    stack = []
    for char in text: 
        if char in '([{':
            stack.append(char)
        elif not stack or stack.pop() != opening_close[char]:
            return False
        return not stack
    

# стек - стопка тарелок 
# положил сверху - забрал сверху
stack = []
stack.append(10) # положили тарелку 10 севрху
stack.append(20)
stack.append(30)
top = stack.pop() # 30 сняли сверху
# в стеке остались 10 и 20
# append и pop - с конца списка 0(1) память элементов лежит одновременно в худшем O(n)
# берем стек если задача звучит так - последняя скокба должна быть закрытой
# отмена действия cntrl+z снимает последнствее
# путь к a/b/../c снимает папку 
# ближайщий большой справа кто еще ждет своего большого 
# не берем стек если важен порядок прихода, кого обслужили первым-  это очередь

# скобки по шагам 
# каждая закрывающая скобка обязана снять  именно последную открывающ
# счетчик (и) этого не ловит в :"([])" скобок поровну порядок неверный
# пример функции def valid_paretthese 

# text = "({[]})"

# Символ    Дейсвие     Стек
# (         кладем      (
# {         кладем      ({
# [         кладем      ({[
# )         снимаем     ({
# }         снимаем     (
# ]         снимаем     пусто

# пустой стек в конце - все открытые закрыты - ответ True 
# text = "([))"

# символ    действие    стек до снятия  стек в текущий момент
# (         кладем (    пусто           (
# [         кладем [    (               ([
# )         сверху [
# 

# путь в папку - тот же стек 
# a/b/../c - означает вы зашлив A зашли В .. вышли из В зашли в С итог бует A/C 

def path_smpl(path):
    stack = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
        else: 
            stack.append(part)
    return "/" + "/".join(stack)

# при пустом стеке ничего не снимается (выше корня не подняться )
# монотонный стек - следющий справа 
# для каждого числа - перое строо большее справа не такого 
numbers = [2,1,2,4,3]
# нельзя для каждого смотреть весь хвост O(n²)
# стек индексов хранит тех кто еще ждет 
# сверху всегда меньше чем под ним значения в стеке убивают 
def next_greqter_elements(array):
    result = [-1] * len(array)
    stack_indexs = []
    for index,value in enumerate(array):
        while stack_indexs and array[stack_indexs[-1]] < value:
            preview_index = stack_indexs.pop()
            result[preview_index] = value
        stack_indexs.append(index)
    return result

# для каждого числа найти первое строго большее справа если такого нет -1
 
# индекс 0 1 2 3 4 
# число 2 1 2 4 3
# ответ 4 2 4 -1 -1

# как это работает - у двойки на индексе 0 справа большее ближайшее - 4. 2 на индексе 2 не больше.
# у единициы на индексе 1 ближайшее большее 2 на индексе 2 
# что лежит в стеке - не числа а индексы чисел которые не нашли себе большее справа 
# числа убивают индекса сверху вниз. самый маленький из идущих под ним большее 

# пока стек такой, новый элемент может закрыть только вершину 
# если вершина меньше текущего она нашла ответ - снимаем
# если новая вершина тоже меньше - снимаем и ее 
# если только вершина уже не меньше текущего остальные подней 

# связанный список 
# индекс numbers[i] нет ходишь только по .next
# середина и указатель - разной скорости 

# список 1 → 2 → 3 → 4 → None 
# разворот  триссыллки иначе потеряем хвост 
def reverse_list(head):
    current = head 
    previous = None
    while current:
        next_node = node = current.next 
        current.next = previous 
        previous = current
        current = next_node
    
    return previous 

# шаг   current     next_node   после разворота стрелки    previous станет 
# 1     1           2           1→None                     1
# 2     2           3           2→1→None                   2
# 3     3           4           3→2→1None                  3
# 4     4           None        4→3→2→1                    4
# 5     None        Null        Exit                       Head = 4 


# порядок строк важен начало сохранить next node потом перейти на стрелку 

# серединна 
# fast - прыгает через узел когда он в конце slow в середине 
# 1 → 2 → 3 → 4 → 5 
# шаг   slow    fast
# 1     1       1
# 2     2       3
# fast.next is None slow = 3 / fast = 5 
# на четной длинне slow встанет на правую середину (клаассика LeetCode )

# цикл
# Если кольцо есть быстрый догонит медленного внутри кольца если fast уперся в none - цикла нет
# Когда брать - разворот , цикл слияние двух отсортированных удалять n-й c конца 

# задание
# проверка верны ли скобки
# ()[]{}  
# ([)]
# ((())
# упростить путь 
# a/./b 

# в кассу встали ана боря вика в этом порядке 
# кого вызвали первым кто вторым кто остался 

# также аню борю и вику положили в стек и сняли всех в каком порякдке выйдут 
# чем отличаются от очереди 

from collections import deque
queue = deque()
queue.append("Анна")
queue.append("Боря")
queue.append("Вика")
first = queue.popleft() # анна 
# остались боря вика
# deque.append и deque.popleft - O(1)
# list.pop() не очередь каждый вызов
# сдвигает все оставшиеяся O(n)
# тысяча таких вызовов уже квадат

array = ["Анна", "Боба", "Вика"]

# очередь обхода по уровням 


from collections import deque
queue = deque()
queue.append("Анна")
queue.append("Боря")
queue.append("Вика")
first = queue.popleft() # анна 
second = queue.popleft() # боря
third = queue.popleft() # викай

print("Первый: ", first)
print("Второй: ", second)
print("Третий: ", third)

stack = []
stack.append("анна")
stack.append("боря")
stack.append("вика")

out_1 = stack.pop()
out_2 = stack.pop()
out_3 = stack.pop()

print("стек - ", out_1,out_2,out_3)