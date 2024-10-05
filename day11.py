from itertools import pairwise

class Password:
    def __init__(self, pwd: str):
        self.ordinals = [ord(x)-ord('a') for x in pwd]

    def condition1(self) -> bool:
        ordinals = self.ordinals
        diffs = [b-a for (a,b) in pairwise(ordinals)]
        return (1,1) in pairwise(diffs)

    def condition2(self) -> bool:
        not_allowed = [ord('i')-ord('a'), ord('o')-ord('a'), ord('l')-ord('a')]
        return not any(x in not_allowed for x in self.ordinals)

    def condition3(self) -> bool:
        diffs = [b-a for (a,b) in pairwise(self.ordinals)]
        number_of_pairs = diffs.count(0)
        for i in range(0, len(diffs)-1):
            if diffs[i] == 0 and diffs[i+1] == 0:
                number_of_pairs -= 1

        return number_of_pairs>1
  
    def is_valid(self):
        return self.condition1() and self.condition2() and self.condition3()
    
    def _inrease(self):
        pos = len(self.ordinals) - 1
        while pos > 0 and self.ordinals[pos] == ord('z') - ord('a'):
            self.ordinals[pos] = 0
            pos -= 1

        if pos == 0 and self.ordinals[0] == ord('z'):
            raise "No more passwords!"
        
        self.ordinals[pos] = self.ordinals[pos] + 1

    def next(self):
        result = Password(str(self))
        result._inrease()
        while not result.is_valid():
            result._inrease()
        return result

    def __str__(self):
        return "".join(chr(x + ord('a')) for x in self.ordinals)


pwd = ""
with open("input11.txt") as f:
    pwd = f.readline().strip()

new_password = Password(pwd).next()
print(str(new_password))
new_password = new_password.next()
print(str(new_password))
