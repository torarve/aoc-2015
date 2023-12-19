import re


def is_nice(word: str) -> bool:
    if len([x for x in word if x in "aeiou"])<3:
        return False
    
    has_double_letter = False
    for i in range(1, len(word)):
        has_double_letter = word[i-1] == word[i]
        if has_double_letter: break

    if not has_double_letter:
        return False

    for x in ["ab", "cd", "pq", "xy"]:
        if word.find(x)>=0:
            return False
    return True


assert is_nice("ugknbfddgicrmopn") == True
assert is_nice("aaa") == True
assert is_nice("jchzalrnumimnmhp") == False
assert is_nice("haegwjzuvuyypxyu") == False
assert is_nice("dvszwmarrgswjxmb") == False


with open("input05.txt") as f:
    nice_words = [x.strip() for x in f.readlines() if is_nice(x.strip())]

print(len(nice_words))

def is_nice2(word: str) -> bool:
    pair_appears_twice = False
    for i in range(len(word)-2):
        sub = word[i:i+2]
        pair_appears_twice = word[i+2:].find(sub)>=0
        if pair_appears_twice:
            break

    repeat_char = False
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            repeat_char = True
        if repeat_char:
            break

    return pair_appears_twice and repeat_char

assert is_nice2("qjhvhtzxzqqjkmpb")
assert is_nice2("xxyxx")
assert not is_nice2("uurcxstgmygtbstg")
assert not is_nice2("ieodomkazucvgmuy")

with open("input05.txt") as f:
    nice_words2 = [x.strip() for x in f.readlines() if is_nice2(x.strip())]

print(len(nice_words2))