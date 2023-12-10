#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20191817 이름 : 이정훈


# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

# solution 함수는 my_string, target 이라는 매개변수를 입력받는다
def solution(my_string, target):
    # answer = 0 으로 초기화 
    answer = 0
    # target에 해당하는 단어의 집합이 my_string에 있다면
    # answer = 1 해당하는 단어가 없다면 answer=0
    if target in my_string:
        answer = 1
    else:
        answer = 0
    return answer
print(solution('answer', 'sw'))

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    # 문자를 한 글자 단위로 분리한다.
    letter =letter.split()
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    # answer 해석된 문자를 담을 배열을 선언 
    answer = ''

    # 딕셔너리를 보고 모스부호가 어떠한 알파벳에 속하는지 찾고 answer에 차례대로 대입한다.
    for c in letter:
        answer+= morse[c]

    return answer


print(solution('.. .- -- - .- .-.. . -. - . -.. .- - .... .- .-. -.. .-- --- .-. -.- ... --- .. -.-. --- -- . .. -. ..-. .. .-. ... - .--. .-.. .- -.-. . .-- .... . .-. . ...- . .-. .. --. ---' ))

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.


# solution에는 int 형의 숫자가 입력된다.
def solution(age):
    # int형은 str형으로 바꿔준다.
    original_age= str(age)
    answer = ''
    # original_age를 P857_age 행성의 나이로 매핑시키기 위해 사전을 정의한다.
    P857_age ={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    # original_age를 P857_age 행성의 나이로 매핑시켜 answer 배열에 담는다
    for i in original_age:
        answer += P857_age[i]

    return answer

print(solution(23))


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

#solution 함수를 정의하고 각 원의 반지름을 받는다.
def solution(r1, r2):
    answer = 0
    # 첫번째 for 반복문을 실행하여 r1과 r2 사이에 있는(원위의 점)
    # x좌표와 y좌표가 모두 정수인 점의 개수를 answer에 누적시킨다.
    for i in range(0, r1):
        answer += int((r2**2 - i**2)**0.5) - int((r1**2 - i**2 - 1)**0.5)
    # 두 번째 for 반복문을 실행하여 r1과 r2 사이에 있는(원위의 점이 아닌 두 원의 공간사이의 점들)
    # x좌표와 y좌표가 모두 정수인 점의 개수를 answer에 누적시킨다.
    for i in range(r1, r2):
        answer += int((r2**2 - i**2)**0.5)
    return answer * 4

print(solution(3,6))

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]


# solution 함수는 int 형 집합인 배열 numbers를 입력으로 받는다(리스트)
def solution(numbers):
    # 이중 for문을 사용하여 배열의 순서번호,인덱스를 구분하게해준다.
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # 배열의 앞에 숫자와 뒤에 숫자의 결합과 뒤의 숫자와 앞의숫자의 결합을 str로 형변환 후 묶는다
            # 그리고 if을 통해 비교하기위해 int형으로 형변환 후 결합된 수를 비교한다
            # if 문의 앞에의 숫자의 조합이 더 크면 유지하고, 뒤에 숫자의 조합이 더 크면 순서(i,j)를 바꾸어준다.
            # 이를 반복한다.   
            if int(str(numbers[i]) + str(numbers[j])) < int(str(numbers[j]) + str(numbers[i])):
                numbers[i], numbers[j] = numbers[j], numbers[i]
    # for문이 끝나면 str 형태로 만들어준다 => join 함수를 사용하여 이어붙이기 위해
    # numbers들을 join하여 모두 붙여준다. 
    answer = ''.join(map(str, numbers))
    return answer

numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print(result)