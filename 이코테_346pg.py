'''
시간제한 : 1초
메모리제한 : 128메가

입력 : 
p : 균형잡힌 괄호 문자열 ('('와 ')'로만 이루어진 문자열. 길이 2이상 1,000이하 짝수)

출력:
올바른 괄호 문자열

변환 과정
1. 입력이 빈 문자열인 경우, 빈 문자열 반환
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리.
   u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며, v는 빈문자열이 될 수 있음
3. 수행한 결과를 문자열 u에 이어 붙인 후 반환.
    3-1. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
    4-1. 빈 문자열에 첫 번째 문자로 '()'를 붙인다.
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
    4-3. ')'를 다시 붙인다.
    4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    4-5. 생성된 문자열을 반환한다.

* 문자열 p를 이루는 '('와 ')'의 개수는 항상 같다
* 만약 p가 이미 올바른 괄호 문자열이라면 그대로 return 하면 된다.
'''

# 틀린 내 코드
'''
def isEmpty(s):
    if s == '':
        return True
    return False
    
def step_two(s):
    open_num = 0
    close_num = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            open_num += 1
        elif s[i] == ')':
            close_num += 1
        
        if open_num == close_num:
            return (s[:i+1], s[i+1:])
        
        
def isRight(s):
    for i in range(len(s) // 2):
        if not(s[i] == '(' and s[len(s)-i-1] == ')'):
            return False   
    return True

def removeReverse(x):
    x = x[1:-2]
    for i in range(len(x)):
        if x[i] == '(':
            x[i] = ')'
        else:
            x[i] = '('
    return x

def step_three(s):
    u, v = step_two(s)

    if isRight(u):
        if isEmpty(v):
            return u
        else:
            return u + step_three(v)
    else:
        if isEmpty(v):
            return '(' + ')' + removeReverse(u)
        else:
            return step_three(v)
            
def solution(p):
    answer = step_three(p)
    
    return answer
'''


def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i
        
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    
    return True
            
def solution(p):
    answer = ''
    
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if check_proper(u):
        answer = u + solution(v)
        
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer