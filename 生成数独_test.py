import random
import copy

#创建一个数独数组用于存储
sudoku1=[[0 for i in range(9)] for j in range(9)]

#数独难度
difficult=[0,1,2,3]
#生成一个随机的数独
def create_sudoku():
    #首先生成一个随机的完整的数独，然后再随机挖洞，挖洞的时候要保证挖洞后的数独有唯一解
    sudoku=[[0 for i in range(9)] for j in range(9)]#先生成一个9*9的数独
    #生成第一行
    sudoku[0]=random.sample(range(1,10),9)
    for i in range(1,9):
        #生成第i行
        for j in range(9):
            #生成第i行第j列的元素
            #生成一个列表，这个列表里面包含1-9，然后从这个列表里面随机取一个数，然后把这个数从列表里面删除
            list1=list(range(1,10))
            for k in range(i):
                if sudoku[k][j] in list1:
                    list1.remove(sudoku[k][j])
            sudoku[i][j]=random.choice(list1)
    return sudoku
#定义一个函数，用来挖洞,难度为difficult数组的分层，0为最简单，3为最难
def dig_holes(sudoku):
    #难度为1的时候，挖掉10个洞，难度为2的时候，挖掉20个洞，难度为3的时候，挖掉30个洞
    #测试
    difficult=1;
    sudoku_dig=copy.deepcopy(sudoku)
    if difficult==0:
        holes=10
    elif difficult==1:
        holes=20
    elif difficult==2:
        holes=30
    elif difficult==3:
        holes=40
    for i in range(holes):
        #先随机挖洞，然后判断挖洞后的数独是否有唯一解，如果有唯一解，则继续挖洞，如果没有唯一解，则重新挖洞
        while True:
            row=random.randint(0,8)
            col=random.randint(0,8)
            if sudoku_dig[row][col]==0:
                continue
            else:
                sudoku_dig[row][col]=0
                sudoku_solve=copy.deepcopy(sudoku_dig)
                if solve_sudoku(sudoku_solve):
                    continue
                else:
                    break
    return sudoku_dig
#定义一个函数，用来判断一个数独是否有唯一解
def solve_sudoku(sudoku):
    #用递归方法来求解数独
    #首先判断数独是否有空格
    if is_full(sudoku):
        #数独已经求解完毕
        return True
    else:
        #数独没有求解完毕，则找到第一个空格的位置
        for i in range(9):
            for j in range(9):
                if sudoku[i][j]==0:
                    #找到一个空格，然后从1-9挨个尝试
                    for k in range(1,10):
                        sudoku[i][j]=k
                        #判断填入的数字是否满足数独的规则
                        if is_valid(sudoku,i,j):
                            #如果满足数独的规则，则继续求解数独
                            if solve_sudoku(sudoku):
                                #数独有解
                                return True
                            else:
                                #数独无解
                                continue
                        else:
                            #如果不满足数独的规则，则继续尝试下一个数字
                            continue
                    #如果1-9都尝试完毕之后，发现数独无解，则返回False
                    return False
        #如果数独没有空格，但是数独没有求解完毕，则返回False
        return False
#判断数独是否有空格
def is_full(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return False
    return True
#判断填入的数字是否满足数独的规则
def is_valid(sudoku,row,col):
    #首先判断填入的数字所在的行是否满足数独的规则
    for i in range(9):
        if i!=col:
            if sudoku[row][i]==sudoku[row][col]:
                return False
    #然后判断填入的数字所在的列是否满足数独的规则
    for i in range(9):
        if i!=row:
            if sudoku[i][col]==sudoku[row][col]:
                return False
    #然后判断填入的数字所在的3*3的小方格是否满足数独的规则
    row_left=row//3*3
    col_left=col//3*3
    for i in range(row_left,row_left+3):
        for j in range(col_left,col_left+3):
            if i!=row and j!=col:
                if sudoku[i][j]==sudoku[row][col]:
                    return False
    return True
#打印数独
def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=' ')
        print()

if __name__ == '__main__':
    sudoku1=create_sudoku()
    sudoku1=dig_holes(sudoku1)
    print_sudoku(sudoku1)