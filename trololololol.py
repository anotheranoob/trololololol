while True:
    number=input("How much do you want to get trolled? input a integer")
    try:
        number=int(number)
        print(number)
        if number<=0:
            raise ValueError
        break
    except ValueError:
        pass
for i in range(number):
    file=open(str(i)+".txt", "w")
    print(str(i), file=file)
    file.close
