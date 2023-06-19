def ss(number_list, n):
    """Простой последовательный алгоритм поиска элемента в списке.
    Последовательно сверяется каждый элемент списка с искомым.
    В результате, если искомый элемент найден, то выводим True,
    в противном случае False.

    Args:
        number_list (list): Список элементов одного типа
        n (elem): Искомый элемент

    Returns:
        boolean: Логический тип. Верно, если элемент найден, и ложь в противном случае
    """
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


numbers = range(0, 100)
s1=ss(numbers,4)
print(s1)
s2=ss(numbers,202)
print(s2)
