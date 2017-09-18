for i in range(int(input("How much do you want to get trolled? input a integer"))):
    file=open(str(i)+".txt", "w")
    print(str(i), file=file)
    file.close
