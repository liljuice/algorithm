def solution(n, k, cmd):
    name = [x for x in range(0, n)]
    maxRow = n - 1 # 행의 개수
    deleted = [False] * (n)
    rowBin = []
    # [0 1 2 3 4 5 6 7]
    for i in range(len(cmd)):
        com = list(cmd[i].split())
        if com[0] == 'D':
            move = int(com[1])
            while move:
                if deleted[k + 1] == False:
                    k += 1
                    move -= 1
                else:
                    k += 1
        elif com[0] == 'U':
            move = int(com[1])
            while move:
                if deleted[k - 1] == False:
                    k -= 1
                    move -= 1
                else:
                    k -= 1
        elif com[0] == 'C':
            maxRow = -1
            for i in range(len(deleted)):
                if deleted[i] == False:
                    maxRow = i
                    
            if k == maxRow: # 지우려는 행이 표의 마지막 행인 경우
                deleted[k] = True
                rowBin.append(k)
                move = 1            
                while move:
                    if deleted[k - 1] == False:
                        k -= 1
                        move -= 1
                    else:
                        k -= 1            
            else:
                deleted[k] = True
                rowBin.append(k)
        elif com[0] == 'Z':
            revive = rowBin.pop()
            deleted[revive] = False
    answer = ''   
    result = []
    for i in range(len(deleted)):
        if deleted[i]: #지워짐
            result.append('X')
        else:
            result.append('O')
    answer = "".join(result)

    return answer
