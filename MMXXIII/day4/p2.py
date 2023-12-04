from p1 import loadFile


class Card:
    # copies includes the original
    copies = 1
    points = 0

    def __init__(self, card: str) -> None:
        cardValues = card.split(":")[1]
        winningNumbers, myNumbers = cardValues.split("|")
        self.winningNumbers = winningNumbers.split()
        self.myNumbers = myNumbers.split()

        points = 0
        for number in self.winningNumbers:
            if number in self.myNumbers:
                points = points + 1
        self.points = points

    def getPoints(self):
        return self.points

    def createCopies(self):
        self.copies += 1

    def __len__(self):
        return self.copies


if __name__ == "__main__":
    inp = loadFile()
    cards = []
    for card in inp:
        cards.append(Card(card))
    for i in range(len(cards)):
        card = cards[i]
        winningNumbers = card.getPoints()
        for _ in range(card.copies):
            for inc in range(1, winningNumbers + 1):
                index = i + inc
                if index < len(cards):
                    cards[index].createCopies()

    total = 0
    for card in cards:
        total += len(card)

    print(total)
