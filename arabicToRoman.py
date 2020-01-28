

def arabicToRoman(inputNumber):
    inputNumber = int(inputNumber)
    
    if inputNumber < 0 or inputNumber > 3999:
        raise Exception('inputNumber should not exceed 3999 or be lower than 0. The value of inputNumber was: {}'.format(inputNumber))

    numToRoman = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
    answer = ""
    i = 0
    while inputNumber:
        firstdigit = inputNumber // numToRoman[i][0]
        inputNumber %= numToRoman[i][0]
        answer += (firstdigit * numToRoman[i][1])
        i+=1
    return answer