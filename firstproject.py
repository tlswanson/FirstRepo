print("""Let's keep track of our book genres and number of books within each genre.
First, let's refresh our mind of some common genres:
Fiction:
- Detective & Mystery
- Dystopian
- Fantasy
- Science Fiction
- Romance
- Graphic Novel


Non-Fiction:
- Memoir
- Autobiography
- Politics
- True Crime
- Historical
""")


#### Create comma separated file "Library" and declare columns
#f = open('Library.csv', 'w')
#f.write('"Title", "Author", "Genre", "Published YYYY", "Hardcover?", "Read?"')
#f.write('\n')
#f.close()

'''
#### Append input column answers to Library
with open('Library.csv','a') as file:
    titl = str(input('Title of book: '))
    auth = str(input('Author of book (Last, First): '))
    genr = str(input('Genre of book: '))
    publ = str(input('Published YYYY of book: '))
    hard = str(input('Is this a hardcover? Y or N: '))
    reyn = str(input('Have you read this book? Y or N: '))
    newentry = '"{}", "{}", "{}", "{}", "{}", "{}"\n'.format(titl, auth, genr, publ, hard, reyn)
    file.write(newentry)
'''
file = open('Library.csv','a')
#### If new_entry True, take input for new line to append to csv file
#### If new_entry False, stop taking data
def new_entry(f):
    answer = True
    while answer:
        q = input('ADD BOOK? Y or N: ')
        if q.lower() == 'y':
            titl = str(input('Title of book: '))
            auth = str(input('Author of book (Last, First): '))
            genr = str(input('Genre of book: '))
            publ = str(input('Published YYYY of book: '))
            hard = str(input('Is this a hardcover? Y or N: '))
            reyn = str(input('Have you read this book? Y or N: '))
            entry = '"{}", "{}", "{}", "{}", "{}", "{}"\n'.format(titl, auth, genr, publ, hard, reyn)
            f.write(entry)
        else:
            answer = False
            print('Okay, see you later!')
        

new_entry(file)