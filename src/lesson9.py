
def file_refactor(file_name: str) -> str:
    with open(f'data/{file_name}', encoding="utf-8") as file:
        new_txt = []
        for line in file.readlines():
            if line.isalpha():
                new_txt.append(line)
            else:
                new_word = ""
                for lin in line:
                    if lin.isalpha():
                        new_word += lin
                if len(new_word) != 0:
                    new_txt.append(new_word)
        # return new_txt
        with open('data/new_txt.txt', 'w', encoding="utf-8") as new_file:
            new_file.write("\n".join(new_txt))
