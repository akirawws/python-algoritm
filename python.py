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