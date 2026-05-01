import math

benford = [math.log(1+i) - math.log(i) for i in range(1, 10)]

def firstDigit(num: int, zero:bool = False) -> int:
    if math.isnan(num):
        return 0

    if num < 0:
        num *= -1

    while zero and num < 1 and num != 0:
        num *= 10

    while num > 9:
        num //= 10
    
    return int(num)

def probOfDigits(nbs: list(int), zero:bool = False) -> dict:
    sizeOfNbs = len(nbs)

    tmp = [0 for _ in range(sizeOfNbs)]
    for i in range(sizeOfNbs):
        tmp[i] = firstDigit(nbs[i], zero)

    nbOfOcc = [0 for _ in range(9)]
    for j in tmp:
        if j < 1:
            continue
        nbOfOcc[j-1] += 1

    data = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for k in range(9):
        data[k+1] = float("{:.4f}".format(nbOfOcc[k]/sizeOfNbs))*100

    return data

def checkBenford(data, benford):
    exact = True
    before = 101.0
    for key, value in data.items():
        if value >= before:
            return False, False

        if exact and value != benford[key-1]:
            exact = False

        before = value

    return True, False

def BenfordLaw(data):
    law, exact = checkBenford(data, benford)
    if law:
        if exact:
            print("This dataset is a perfect representation\
             of the Benford's Law!")
        else:
            print("This dataset respects Benford's Law")
    else:
        print("This dataset does not respect Benford's Law")
    input("Press enter to continue...")
