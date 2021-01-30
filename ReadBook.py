import pyttsx3 # pip install pyttsx3
import PyPDF2 # pip install PyPDF2
import os
from glob import glob

#Function to increment page number
def inc_page():
    with open("pageno.txt" , "r") as fp:
        page_no = fp.read()

    page_no = int(page_no) + 1
    page_no = str(page_no)

    with open("pageno.txt" , "w") as fp:
        fp.write(page_no)
    return page_no

#Function to update value of page number if value of pageno is 1
def update(pg):
    pg = str(pg)
    with open("pageno.txt" , "w") as s:
        pg = s.write(pg)
        s.close()

def checkIfFileExists():
    if(not os.path.exists('./pageno.txt')):
        with open('pageno.txt', 'w') as fp:
            fp.write('0')

def readPageNumberFromFile():
    with open('pageno.txt', 'r') as fp:
        return int(fp.read())
    
# Opening the pdf file present in the same directory as the python script
book_name = glob('*.pdf')[0]
print(f"Book: {book_name}")
book = open(book_name, 'rb')

#Read the PDF using PyPDF2
pdfReader = PyPDF2.PdfFileReader(book)

# Getting total number of pages
pages = pdfReader.numPages
pages = int(pages)
print(f"\nTotal Pages: {pages}")

speaker = pyttsx3.init()

# Setting speed of the speaker 
speaker.setProperty('rate', 130)

checkIfFileExists()

pgno = readPageNumberFromFile()
pgno = int(pgno)

if pgno == 0:
    pgno = int(input("Enter the starting page from where you want to listen: "))
    
#Condition for inputed number should not be greater than total number of pages
if pgno < pages:
    update(pgno)

    #Running loop from given page number to last page of PDF
    for num in range(pgno, pages):

        # Get page
        page = pdfReader.getPage(num)

        # Extracting the text
        text = page.extractText()
        print(f"\nPage Number: {num}\n")
        if(len(text)):
            print(text)

        # Just say it ;-)
        speaker.say(text)
        speaker.runAndWait()

        inc_page()
