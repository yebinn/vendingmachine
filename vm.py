change = 0

def init():
    global change
    change = 0

def run(raw):
    global change

    tokens = raw.split(" ")
    cmd, params = tokens[0], tokens[1:]

    if cmd == "잔액":
        return "잔액은 " + str(change) + "원입니다"
    else:
        coin = params[0]
        change += int(coin)
        return coin + "원을 넣었습니다"
