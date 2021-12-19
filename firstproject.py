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

#### If new_entry True, take input for new line to append to csv file
#### If new_entry False, stop taking data
def new_entry(f):
    answer = False
    while not answer:
        q = input('ADD BOOK? Y or N: ')
        if q.lower() == 'y':
            titl = str(input('Title of book: '))
            auth = str(input('Author of book (Last, First): '))
            genr = str(input('Genre of book: '))
            publ = str(input('Published YYYY of book: '))
            hard = str(input('Is this a hardcover? Y or N: ')).upper()
            reyn = str(input('Have you read this book? Y or N: ')).upper()
            d = {'title':titl, 'author':auth, 'genre':genr, 'year': publ, 'hardcover':hard, 'read':reyn}
            ver = input('Verify information entered above. Is EVERYTHING correct? Y or N: ')
            if ver.lower() != 'y':
                edit = input('What needs to be changed? (Title, Author, Genre, Year, Hardcover, Read): ')
                edit_val = input('Enter new answer to question: ')
                if edit.lower() in d.keys():
                    d[edit] = edit_val
                    edited = '"{}", "{}", "{}", "{}", "{}", "{}"\n'.format(d['title'], d['author'], d['genre'], d['year'], d['hardcover'].upper(), d['read'].upper())
                    f.write(edited)
                    print()
                else: 
                    print("Let's just try again.")
                    break
            else:
                entry = '"{}", "{}", "{}", "{}", "{}", "{}"\n'.format(titl, auth, genr, publ, hard, reyn)
                f.write(entry)
                print()
        else:
            answer = True
            print('Okay, see you later!')
        
with open('Library.csv','a') as file:
    new_entry(file)