while True:
    number=input("How much do you want to get trolled? input a integer")
    try:
        number=int(number)
        if number<=10:
            raise ValueError
    except ValueError:
        pass
for i in range(number):
    file=open(str(i)+".txt", "w")
    print(str(i), file=file)
    file.close
