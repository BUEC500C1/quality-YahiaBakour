

def arabicToRoman(inputNumber):
    try:
        inputNumber = int(inputNumber)
    except Exception as e:
        print(e)
        return
    
    if inputNumber < 0 or inputNumber > 3999:
        return

    numToRoman = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
    answer = ""
    i = 0
    while inputNumber:
        firstdigit = inputNumber // numToRoman[i][0]
        inputNumber %= numToRoman[i][0]
        answer += (firstdigit * numToRoman[i][1])
        i+=1
    return answer