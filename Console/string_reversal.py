raw = "1234567890"
reversed = ""
for i in range(len(raw)):
    j = len(raw) - 1 - i
    reversed += raw[j]

print(reversed)
