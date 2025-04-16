with open('lorem_morse.txt', 'r') as f1, open('expected_lorem_morse.txt', 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
    if line1 != line2:
        print(f"Difference in line {i}:")
        print("File1:", line1.strip())
        print("File2:", line2.strip())

     