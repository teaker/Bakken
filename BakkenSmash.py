#Bakken project.  This program will search all files contained within a user-specified
# directory for a user-specified phrase.  If the phrase is found in a given file, the 
# page containing the term will be extracted and saved to a new file.

import PyPDF2
import re
import os

print('''\


______       _    _                _____                     _     
| ___ \     | |  | |              /  ___|                   | |    
| |_/ / __ _| | _| | _____ _ __   \ `--. _ __ ___   __ _ ___| |__  
| ___ \/ _` | |/ / |/ / _ \ '_ \   `--. \ '_ ` _ \ / _` / __| '_ \ 
| |_/ / (_| |   <|   <  __/ | | | /\__/ / | | | | | (_| \__ \ | | |
\____/ \__,_|_|\_\_|\_\___|_| |_| \____/|_| |_| |_|\__,_|___/_| |_|

This program will search all PDF files contained within a directory 
for a word or phrase.  If the phrase is found in a given PDF, the 
page containing the term will be extracted and saved as a new PDF.

    ''')

# Enter the search term here:
String = input("Enter search string: ")

#Enter directory containing original PDFs:
inputDir = input("Enter path to directory containing PDFs to search (make sure to include \ at end): ")
outputDir = input("Enter path to directory where you would like PDFs saved (make sure to include \ at end): ")
outputAppend = input("Enter text to be appended to end of output filenames: ")

#For each file in the directory:
for filename in os.listdir(inputDir):

    # Set each pdf file
    object = PyPDF2.PdfFileReader(inputDir + filename, 'rb')

    # Get number of pages in the pdf
    NumPages = object.getNumPages()

    # Setup the file writer
    output = PyPDF2.PdfFileWriter()

    # Do the search
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        if re.search(String, Text):
            print("File: " + filename + "  |  " + "Page: " + str(i))
            output.addPage(object.getPage(i))
            outputStream = open(outputDir + filename.split('.')[0] + outputAppend + ".pdf", "wb")
            output.write(outputStream)
            outputStream.close()
