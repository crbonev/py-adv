symbols = {}
text = input()
for symbol in text:
    if symbol not in symbols:
        symbols[symbol] = 1
    else:
        symbols[symbol] += 1

for symbol, occurrences in sorted(symbols.items()):
    print(f'{symbol}: {occurrences} time/s')