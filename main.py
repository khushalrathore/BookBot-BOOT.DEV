def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def main():
    PATH = "books/frankenstein.txt"
    with open(PATH) as f:
        file_contents = f.read()
        words = file_contents.split()


        header = f"\n{f"Begin report of books/frankenstein.txt".center(40,'-')}"
        doc_fact = f"{f"{len(words)} words found in the document".center(40,' ')}\n"
        table_head = f"{40*'-'}\n|  Character  |  Number of Occurences  |\n{40*'-'} "
        footer = f"\n{f"End Report".center(40,' ')}\n\n"

        letter_counts = count_letters(file_contents)
        sortedK_letter_counts = dict(sorted(letter_counts.items()))
        sortedV_letter_counts = dict(sorted(letter_counts.items(), reverse=True,key=lambda item: item[1]))
        print(f"{header}\n\n{doc_fact}\n{table_head}")
        for i,j in sortedV_letter_counts.items():
            print(f"{f"|  {str(i).center(9)}  |  {str(j).center(20)}  |\n{40*'-'}"}")
    
    print(footer)

if __name__ == "__main__":
    main()
