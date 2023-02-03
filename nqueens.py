print ("Enter the number of queens")
N = int(input())
board = [[0 for x in range(N)]for x in range(N)]

def is_attack(i, j):
    for k in range(N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(N):
        for l in range(N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(num):
    #if n is 0, solution found
    if num==0:
        return True
    for i in range(N):
        for j in range(N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queen(num-1)==True:
                    return True
                board[i][j] = 0
    return False

N_queen(N)
for i in board:
    print (i)
