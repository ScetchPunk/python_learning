def bottles_of_beer(bob):
    """Печатает текст песенки про 99 бутылок пива.

    Args:
        bob (int): Должно быть целым числом.
    """
    if bob < 1:
        print( "Нет бутылок пива на стене. Нет бутылок пива")
        return
    tmp = bob
    bob -=1
    print(f'{tmp} бутылок пива на стене.\n{tmp} бутылок пива на стене.\nВозьми одну, пусти по кругу,\n{bob} бутылок пива на стене.\n')
    bottles_of_beer(bob)

bottles_of_beer(99)