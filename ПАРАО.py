passw = int(input())

san = str(passw)

digit1 = int(san[0])
digit2 = int(san[1])
part1 = digit1 + digit2

digit3 = int(san[1])
digit4 = int(san[2])
part2 = digit3 + digit4

print(str(max(part1, part2)) + str(min(part1, part2)))