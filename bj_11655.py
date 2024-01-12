import sys

S = sys.stdin.readline()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

S = list(S)

for i in range(len(S)):
    if S[i].isupper():
        S[i] = S[i].lower()
        S[i] = alphabet[(alphabet.index(S[i]) + 13) % 26]
        S[i] = S[i].upper()

    elif S[i].islower():
        S[i] = alphabet[(alphabet.index(S[i]) + 13) % 26]

sys.stdout.write(''.join(S))