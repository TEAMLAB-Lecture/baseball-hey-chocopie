# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    #result = False
    for a in range (len(user_input_number)):
        if user_input_number[a] < '0' or user_input_number[a] > '9' :
            return False
    # ==================================
    return True


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    #result = None
    if(100 <= int(user_input_number) and 999 >= int(user_input_number)):
        return True
    # ==================================
    return False


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if 3 == len(three_digit):
        if 1 == three_digit.isdigit():
            tmp = three_digit[0]
            if tmp == three_digit[1] or tmp == three_digit[2]:
                return True
            tmp1 = three_digit[1]
            if tmp1 == three_digit[2]:
                return True
    #result = None
    # ==================================
    return False


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if 1 == user_input_number.isdigit():
        if 3 == len(user_input_number):
            tmp = user_input_number[0]
            if tmp != user_input_number[1] and tmp != user_input_number[2]:
                tmp1 = user_input_number[1]
                if tmp1 != user_input_number[2]:
                    return True
    #result = None
    # ==================================
    return False


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성

    result = get_random_number()
    st_result = str(result)
    flag = 1
    while(1):
        if 3 == len(st_result):
            tmp = st_result[0]
            if tmp != st_result[1] and tmp != st_result[2]:
                tmp1 = st_result[1]
                if tmp1 != st_result[2]:
                    flag = 0
        if flag == 0:
            break
        result = get_random_number()
        st_result = str(result)
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    #result = None
    result = [0, 0]
    if user_input_number == random_number:
        return [3, 0]
    if(len(user_input_number) == 3 and len(random_number) == 3 and user_input_number.isdigit() and random_number.isdigit()):
        for i in range(len(user_input_number)):
            for b in range(len(random_number)):
                if i == b:
                    if user_input_number[i] == random_number[b]:
                        result[0] += 1
                elif i != b:
                    if user_input_number[i] == random_number[b]:
                        result[1] += 1

    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    one_more_input = one_more_input.lower()
    if len(one_more_input) == 1:
        if one_more_input[0] == 'y':
            return True
    elif len(one_more_input) == 3:
        if one_more_input[0] == 'y' and one_more_input[1] == 'e' and one_more_input[2] == 's':
            return True
    # ==================================
    return False


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    #result = None
    one_more_input = one_more_input.lower()
    if len(one_more_input) == 1:
        if one_more_input[0] == 'n':
#        if one_more_input[0] == 'n' and one_more_input[1] == 0:
            return True
    elif len(one_more_input) == 2:
#        if one_more_input[0] == 'n' and one_more_input[1] == 'o' and one_more_input[2] == 0:
        if one_more_input[0] == 'n' and one_more_input[1] == 'o':
            return True
    # ==================================
    return False


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    flag = 0
    while(1):
        while (1):
            user_input = input('Input guess number : ')
            if user_input == "0":
                break
            if is_validated_number(user_input) == 1 :
                break
            else:
                print('Wrong Input')
        if user_input == "0":
            break
        result = get_strikes_or_ball(random_number, user_input)
        #if result[0] != 3 :
        print(result[0], "Strikes,", result[1], "Balls")
        if result [0] == 3:
            #print(result[0], "Strike")
            while(1):
                yes_no = input("You win, one more(Y/N) ?").strip()
#                yes_no = input("You win, one more \(Y\/N\)?")
                if(is_yes(yes_no) == 1):
                    random_number = str(get_not_duplicated_three_digit_number())
                    print("Random Number is : ", random_number)
                    break
                elif(is_no(yes_no) == 1):
                    flag = 1
                    break
                print('Wrong Input')
            if flag == 1:
                break
    #is_digit(user_input_number)
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
