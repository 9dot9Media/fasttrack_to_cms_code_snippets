def repeat_print(string, count=1):
    for _ in range(count):
        print(string)


repeat_print("hi", count=4)
repeat_print(string="hi", count=4)
repeat_print(count=4, string="hi")
