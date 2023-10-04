import pyperclip
import sys
import os
import pickle


def save_pickle(PATH, c_list):
    with open(PATH, mode="wb") as f:
        pickle.dump(c_list, f)


def main():
    path = 'C:\\yoshikawa\\Mybat\\files\\data\\mcp_lists.pickle'
    tpath = 'C:\\yoshikawa\\Mybat\\files\\data\\mcp_lists.txt'
    if len(sys.argv) < 2:
        print("argment ERROR\nmcp comand")
        exit()
    key = sys.argv[1].lower()

    save_file = [
        "alias".ljust(14) + "contents\n",
        "-------------------------\n"
    ]
    aliases = []

    if not os.path.isfile(path):
        aliases = []
    else:
        with open(path, mode="rb") as f:
            aliases = pickle.load(f)

    if key == "remove":
        if os.path.isfile(path):
            os.remove(path)
        if os.path.isfile(tpath):
            os.remove(tpath)
        exit()

    if key == "show":
        for i in range(len(aliases)):
            alias = aliases[i][0]
            content = aliases[i][1]
            save_file.append(alias.ljust(14)+content+"\n")
        with open(tpath, "w", encoding="utf-8") as f:
            f.writelines(save_file)
        os.system("start /b " + tpath)
        exit()

    if key == "save":
        if not len(sys.argv) == 3:
            print("argment ERROR\nmcp save alias")
            exit()
        nalias = sys.argv[2]
        ncontents = pyperclip.paste()
        aliases.append([nalias, ncontents])
        aliases.sort()
        save_pickle(path, aliases)
        exit()

    for i in range(len(aliases)):
        alias = aliases[i][0]
        content = aliases[i][1]
        if key == alias:
            pyperclip.copy(content)
            exit()


if __name__ == '__main__':
    main()
