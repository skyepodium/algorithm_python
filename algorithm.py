from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 9007))

# print("서버와 연결되었다.")
findCoin = 0
while findCoin < 100:
    data = clientSock.recv(2048).decode('utf-8')
    print(data)

    size = len(data)
    # print("문자열 길이 = " + str(size))
    if size != 0 and size != 1102 and size != 13 and size != 14:
        data = data.split(" ")
        data[0] = data[0].split("=")
        data[1] = data[1].split("=")
        n = data[0][1]
        c = data[1][1]
        n = int(n)
        c = int(c)
        # print(n)
        # print(c)


        start = 0
        end = n-1
        while 1:
            mid = (start + end) // 2
            # print(start, end, mid)

            if start != end and end != mid:
                message = ""
                sumValue = (mid - start + 1) * 10
                for i in range(start, mid + 1):
                    message = message + " " + str(i)
                message += "\n"
                # print(message)
                c -= 1
                clientSock.send(message.encode('utf-8'))

                resultValue = clientSock.recv(2048).decode('utf-8')
                # print("sumValue = " + str(sumValue))
                # print("resultValue = " + resultValue)
                resultValue = int(resultValue)

                if sumValue > resultValue:
                    # print("end = mid")
                    end = mid
                else:
                    # print("start = mid")
                    start = mid + 1
            else:
                # print("가짜 코인 번호 = " + str(start))
                result = str(start) + "\n"
                clientSock.send(result.encode('utf-8'))
                c -= 1
                # print("c의 개수" + str(c))
                if c != -1:
                    data = clientSock.recv(2048).decode('utf-8')
                    # print(data)                    
                    clientSock.send(result.encode('utf-8'))
                    c -= 1
                findCoin += 1
                print("찾은 가짜 코인 개수 = " + str(findCoin))
                break
data = clientSock.recv(2048).decode('utf-8')
print(data)

