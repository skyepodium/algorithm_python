MAX_INT = 101
end_x, end_y = 0, 0
a = [[False for _ in range(MAX_INT)] for _ in range(MAX_INT)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dragon = []
result = 0
n = int(input())

def make_generation():

    size = len(dragon)

    for i in range(size-1, -1, -1):
        dir = (dragon[i] + 1) % 4

        global end_x, end_y
        end_x = end_x + dx[dir]
        end_y = end_y + dy[dir]

        a[end_x][end_y] = True

        dragon.append(dir)

for i in range(n):
    y, x, d, g = map(int, input().split())

    dragon.clear()

    end_x = x
    end_y = y

    a[end_x][end_y] = True

    end_x = x + dx[d]
    end_y = y + dy[d]

    a[end_x][end_y] = True

    dragon.append(d)

    for i in range(g):
        make_generation()
    
for i in range(MAX_INT-1):
    for j in range(MAX_INT-1):

        if a[i][j] and a[i][j+1] and a[i+1][j] and a[i+1][j+1]:
            result += 1

print(result)
