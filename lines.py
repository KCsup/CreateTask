def main():
    fileDir = input("Path to In File: ")
    i = open(fileDir, "r")
    lines = i.readlines()
    newL = []
    lineNum = 1
    for l in lines:
        spaces = ""
        for _ in range(6 - len(str(lineNum))):
            spaces += " "
        newL.append(f"{lineNum}{spaces}{l}")
        lineNum += 1
    
    i.close()

    with open("out.txt", "w") as out:
        out.writelines(newL)
        out.close()


if __name__ == "__main__":
    main()