class Card:
    suits = ["пик", "червей", "буб", "треф"]

    values = [
        None,
        None,
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "валет",
        "дама",
        "король",
        "туз",
    ]

    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v
        self.suit = s

    ### Перегрузка сравнения для карт: "меньше, чем"
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    ### Перегрузка сравнения для карт: "больше, чем"
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        ### сорсери предлагает упростить логику сравнения.
        ### Оставлю тут так для понимания
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"


# card1 = Card(12, 2)
# print(card1)
# card2 = Card(11, 3)
# print(card2)
# print(card1 > card2)
