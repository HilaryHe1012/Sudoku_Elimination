# checks if a sudoku is solved or not
def solved(s) :
    for row in s:
        for number in row:
            if number == 0:
                return False
    return True

# performs horizontal check
def horizontalCheck(x, val, s) :
    for number in s[x]:
        if number == val:
            return False
    return True

# vertical check
def verticalCheck(y, val, s) :
    column = [i[y] for i in s]
    for number in column:
        if number == val:
            return False
    return True

# 3x3 square check
def subSquareCheck(x,y,val,s) :
    colS = ((y-1) // 3)*3
    rowS = ((x-1) // 3)*3
    square = [s[y][x] for x in range(rowS, rowS+3) for y in range(colS, colS+3)]
    return val not in square

# elimination sub function
def elimination (x, y, s) :
    possible = []
    for number in range(1,10):
        if subSquareCheck(x+1, y+1, number, s):
            if horizontalCheck(y, number, s):
                if verticalCheck(x, number, s):
                    possible.append(number)
    
    if len(possible) == 1:
        return possible[0]
    elif len(possible) > 1:
        return 0
    else:
        raise Exception("Sudoku Invalid")

# applying the elimination strategy, strategy is a function
# general, can be used with any strategy
def applyStrategy(strategy, s) :
    s_after = s[:]
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0:
                number = strategy(x,y,s)
                if number != 0:
                    s_after[y][x] = number
    return s_after != s

# bring all together
def sudokuSolver (s, strategies) :
    result = []
    count = 0
    while solved(s) == False: 
        for strategy in strategies:
            applyStrategy(strategy, s)
            result.append(applyStrategy(strategy, s))
            count += 1
            if len(result) == len(strategies) and len(strategies) == result.count(False):
                break
        if count >= 100:
            raise Exception("Sudoku Unsolvable")
    return s