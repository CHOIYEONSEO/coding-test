# 내 코드
def find_same(s):
    result = []
    count = 1
    
    len_s = len(s)

    for i in range(len_s-1):
        if s[0] == s[1]:
            count += 1
            s.remove(s[0])
            
            if len(s) == 1:
                result.append(str(count))
                result.append(s[0])
        
        else:
            if count != 1:
                result.append(str(count))
                
            result.append(s[0])
            s.remove(s[0])
            
            if len(s) == 1:
                result.append(s[0])
                
            count = 1
            
    return len(''.join(result))


def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1): # 몇개 단위로 압축할지     8번 반복 / 4번 반복 
        split_s = [s[k:k+i] for k in range(0, len(s), i)] 
            
        answer = min(answer, find_same(split_s))
    
    return answer