def hello_world():
    print("Hello world!")


def gugudan(dan):
    for i in range(1, 10):
        print("{} * {} = {}".format(dan, i, dan*i))


gugudan(int(input()))
hello_world()
