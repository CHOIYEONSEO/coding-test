'''
시간제한 : 1초
메모리제한 : 128메가바이트

입력 : 
s : 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 (1 <= s의길이 <= 10,000)

출력 :
모든 알파벳을 오름차순으로 정렬하고 이어서 모든 숫자를 더한 값 출력

* 알파벳은 오름차순으로 정렬 후 출력
* 숫자는 더해서 출력
* ex. K1KA5CB7 -> ABCKK13

-> 구현
'''
s = list(input().rstrip())

s.sort()

count = 0
str_idx = 0
for i in range(len(s)):
    nums = s[i]
    if nums == '0' or nums == '1' or nums == '2' or nums == '3' or nums == '4' or nums == '5' or nums == '6' or nums == '7' or nums == '8' or nums == '9':
        count += int(nums)

    else:
        str_idx = i
        break

s = s[str_idx:]

if count != 0 :
    s.append(str(count))

print(*s, sep = '')