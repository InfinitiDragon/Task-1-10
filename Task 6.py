sequence1 = "01010101"
sequence2 = "00011100011"

for sequence in [sequence1, sequence2]:
    i = 0
    while i < len(sequence) - 1:
        if sequence[i] != '0' or sequence[i + 1] != '1':
            print(False)
            break
        i += 2
    else:
        print(True)