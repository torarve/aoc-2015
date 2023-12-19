from hashlib import md5

key = "iwrupvqb"
i = 1
while md5(f"{key}{i}".encode()).hexdigest()[:5] != "00000":
    i += 1

print(i)

while md5(f"{key}{i}".encode()).hexdigest()[:6] != "000000":
    i += 1

print(i)
