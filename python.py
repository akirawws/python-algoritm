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