class VendingMachine:
    def __init__(self):
        self._change = 0
        self._valid_coins = [500, 100, 50, 10]

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"

        elif cmd == "동전":
            coin = params[0]

            if int(coin) in self._valid_coins:
                self._change += int(coin)
                return coin + "원을 넣었습니다"
            else:
                return "알 수 없는 동전입니다"

        elif cmd == "음료":
            known_beverage = {
                "커피":150,
                "우유":200,
                "밀크커피":300,
            }

            beverage = params[0]
            if beverage not in known_beverage:
                return "알 수 없는 음료입니다"

            price = known_beverage[beverage]
            if self._change < price:
                return "잔액이 부족합니다"
            self._change = self._change - price
            return beverage + "가 나왔습니다"

        elif cmd == "반환":
            if self._change == 0:
                return "반환할 동전이 없습니다"

            changes = []
            for coin in self._valid_coins:
                n = self._change // coin
                changes.append(n)
                self._change -= coin * n
            return "다음이 반환되었습니다: 500원 " + str(changes[0]) + "개, 100원 " + str(changes[1]) + "개, 50원 " + str(changes[2]) +"개, 10원 " + str(changes[3]) + "개"

        else:
            return "알 수 없는 명령입니다"
