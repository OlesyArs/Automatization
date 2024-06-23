def is_yesr_leap(year):
    if (year % 4 == 0):
        print("Високосный год: " + str(year) + " True")
    else:
        print("Невискосный год: " + str(year) + " False")


is_yesr_leap(int(input("Введите год: ")))