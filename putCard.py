
class PutCard:

    def __init__(self, cardlist):
        self.HandCard = cardlist
        self.putCount = 0
        self.downCardList = [1, 1, 100, 100]

    # def equalCard(self,card):
    #     if card in self.HandCard:
    #         return True
    #     else:
    #         return False

    def getDownCardList(self):
        return self.downCardList

    def resetPutCount(self):
        self.putCount = 0

    def getPutCount(self):
        return self.putCount


    def displayCard(self):
        cardlist = ''
        for i in range(4):
            cardlist += (str(self.downCardList[i]) + ' ')
        return cardlist


    def guess(self, cardlist, deckNum):
        count = 0

        for i in range(len(cardlist)):
            if cardlist[i] == '':
                continue
            else:
                c = int(cardlist[i])

            if c + 10 == self.downCardList[0] or c > self.downCardList[0]:
                count += 1
            elif c + 10 == self.downCardList[1] or c > self.downCardList[1]:
                count += 1
            elif c - 10 == self.downCardList[2] or c < self.downCardList[2]:
                count += 1
            elif c - 10 == self.downCardList[3] or c < self.downCardList[3]:
                count += 1
            elif (c - 10) in cardlist:
                count += 1
            elif (c + 10) in cardlist:
                count += 1


        # print(self.cardList[0] , self.cardList[1], self.cardList[2], self.cardList[3])
        # print(count)

        if count < 2 and deckNum > 0:
            return False
        elif count < 1 and deckNum == 0: #덱 0장일때는 1개만 가능해도 메세지 안뜨게 처리
            return False
        else:
            return True


    def checkPut(self, downNum, holdNum, label):
        if label < 2:
            if downNum < holdNum or downNum == holdNum + 10:
                self.downCardList[label] = holdNum
                self.putCount +=1
                return True
        else:
            if downNum > holdNum or downNum == holdNum-10:
                self.downCardList[label] = holdNum
                self.putCount+=1
                return True

        return False

