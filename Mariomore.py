height = input('Height')

while height.isdigit() == False or int(height) < 0 or int(height) > 23:
    height = input('Height')

height = int(height)
length = height + 1

for x in range (height , 0, -1):
    print(' ' * (x) + '#' * (length - (x)) + '  ' + '#' * (length - (x)) + ' ' * (x))
