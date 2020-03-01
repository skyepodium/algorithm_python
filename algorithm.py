from socket import *
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('pwnable.kr', 9007))
findCoin = 0
while findCoin < 101:
    data = clientSock.recv(2048).decode('utf-8')
    print(data)
    size = len(data)
    if size != 0 and size != 1102 and size != 13 and size != 14:
        data = data.split(" ")
        data[0] = data[0].split("=")
        data[1] = data[1].split("=")
        n = data[0][1]
        c = data[1][1]
        n = int(n)
        c = int(c)
        start = 0
        end = n-1
        while 1:
            mid = (start + end) // 2
            if start != end and end != mid:
                message = ""
                sumValue = (mid - start + 1) * 10
                for i in range(start, mid + 1):
                    message = message + " " + str(i)
                message += "\n"
                c -= 1
                clientSock.send(message.encode('utf-8'))
                resultValue = clientSock.recv(2048).decode('utf-8')
                resultValue = int(resultValue)
                if sumValue > resultValue:
                    end = mid
                else:
                    start = mid + 1
            else:
                result = str(start) + "\n"
                clientSock.send(result.encode('utf-8'))
                c -= 1
                if c != -1:
                    data = clientSock.recv(2048).decode('utf-8')
                    clientSock.send(result.encode('utf-8'))
                    c -= 1
                findCoin += 1
                print("coin!!! = " + str(findCoin))
                break
