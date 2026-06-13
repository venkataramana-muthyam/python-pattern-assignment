def pyramid(h):
    for i in range(1,h+1):
        spaces = " "*(h-i)
        stars = "*"*i
        print(spaces+stars)

pyramid(5)