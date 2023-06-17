from deck import Deck
from player import Player


class Game:
    def __init__(self):
        name1 = input("имя игрока 1:")
        name2 = input("имя игрока 2:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"{winner} забирает карты"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f"{p1n} кладёт {p1c}, а {p2n} кладёт {p2c}"
        print(d)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "ничья"

    def play_game(self):
        cards = self.deck.cards
        print("Погнали")
        while len(cards) >= 2:
            m = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры."
            response = input(m)
            if response.capitalize == "X":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print(f"Игра окончена.{win} выиграл!")

game = Game()
game.play_game()
