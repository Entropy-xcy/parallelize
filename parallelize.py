import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    commands = []
    with open(input_file, "r") as f:
        commands = f.readlines()

    targets = []

    for i in range(len(commands)):
        targets.append("cmd{}".format(i))

    print("default: ", end="")
    for t in targets:
        print(t, end=" ")
    print("\n")

    for i in range(len(commands)):
        print(targets[i]+":\n\t", end="")
        print(commands[i])
