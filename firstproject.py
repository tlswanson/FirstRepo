import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

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
#with open('Library.csv', 'w', newline='') as f:
    #writing = csv.writer(f)
    #writing.writerow(["Title", "Author", "Genre", "Published YYYY", "Hardcover?", "Read?"])


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
                    edited = [d['title'], d['author'], d['genre'], d['year'], d['hardcover'].upper(), d['read'].upper()]
                    csv.writer(f).writerow(edited)
                    print()
                else: 
                    print("Let's just try again.")
                    break
            else:
                entry = [titl, auth, genr, publ, hard, reyn]
                csv.writer(f).writerow(entry)
                print()
        else:
            answer = True
            print('Okay, see you later!\n')
        
#### Option to add books is initiated
with open('Library.csv','a', newline='') as file:
    new_entry(file)

#### Let's start messing with the data now
#### I will make a dictionary of the genres and count within genre, to be pie plotted
with open('Library.csv','r') as l:
    lib = csv.reader(l) # This is the whole file
    next(lib, None) # Let's just skip over the header, for now

    dict_genres = {} # Create a dictionary of genres and count within genres
    for line in lib:
        dict_genres[line[2]] = dict_genres.get(line[2],0) + 1
    print(dict_genres)
    fig, ax = plt.subplots() # Create a pie plot of genre data
    ax.pie(dict_genres.values(), labels=dict_genres.keys(), autopct='%1.1f%%')
    plt.show()
        
    



