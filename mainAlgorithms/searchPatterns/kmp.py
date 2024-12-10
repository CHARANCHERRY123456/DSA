text = "aabaacaadaabaaba"; pattern = "aaba"
actual_answer = [0,9,12]


def build_lps(pattern):
    currentIndex , prefixLength = 1 , 0
    lps = [0]*len(pattern)
    while currentIndex < len(pattern):
        if pattern[currentIndex] == pattern[prefixLength]:
            prefixLength += 1
            lps[currentIndex] = prefixLength
            currentIndex += 1
        else:
            if prefixLength != 0:
                prefixLength = lps[prefixLength-1]
            else:
                lps[currentIndex] = 0
                currentIndex += 1
    return lps

lps = build_lps(pattern)
ti = 0 # pointer to store the index of text
pi = 0 # pointer to store the index of pattern

ans = [] # to store the starting indices where pattern is matched
while ti < len(text):
    if text[ti] == pattern[pi]:
        ti += 1
        pi += 1
        if pi == len(pattern):
            ans.append(ti - pi)
            pi = lps[pi-1]
    else:
        if pi != 0:
            pi = lps[pi - 1]
        else:
            ti += 1

print(ans)
print(ans == actual_answer)






