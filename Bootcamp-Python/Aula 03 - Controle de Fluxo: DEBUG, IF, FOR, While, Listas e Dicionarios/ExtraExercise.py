book_a = "The book is green"
book_b = "green The book is"

try:
    if len(book_a) == len(book_b):

        dict_a = {}
        for i in book_a:
            dict_a[i] = dict_a.get(i, 0) + 1

        dict_b = {}
        for i in book_b:
            dict_b[i] = dict_b.get(i, 0) + 1

    if dict_a == dict_b:
        print("The books are anagrams")

    dict_a = dict(sorted(dict_a.items(), reverse=False))
    dict_b = dict(sorted(dict_b.items(), reverse=False))

    print(dict_a)
    print(dict_b)

except Exception as e:
    print(f"An error occurred: {e}")
