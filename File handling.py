# with  r mode (read(), readline(), readlines())

with open("PH example.txt","r") as f:
    content = f.read()
    print(content)

with open("PH example.txt","r") as f:
    content = f.readline()
    print(content)

with open("PH example.txt","r") as f:
    content = f.readlines()
    print(content)

with open("ph example2.txt","r") as f:  #if you want to read file and file is not created it yet then
    content= f.read()                   #it shows you error
    print(content)

# with w mode (write(), writelines())                # if you want to read file and file is not created it yet then
                                                      #it will create a new file and insert the string in the file
file = open("ph example2.txt","w")                    # but if file is also created then it will override the data
file.write("Nmaaste!")
file.close()
#OR

with open("ph example3.txt","w") as f:
    f.write("Namaaste!, kaise ho")


# with a mode (append())                                # if you want to read file and file is not created it yet then
                                                        #it will create a new file and insert the string in the file
                                                         # but if file is also created then it's just add the data next to the recent data the data
                                                

with open("ph example2.txt","a") as f:
    f.write("\nAgain Kaha jaa rhe ho!")  



####   CODES    ######

with open("ph example.txt","r") as f:
    content = f.read()
    print(content)


with open("ph example.txt","r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))


with open("ph example.txt", "r") as f:
    words = f.read().split()
    print("number ofwords:", len(words) )


with open("ph example.txt", "r") as f1:
    content = f1.read()
with open("ph examples.txt", "w") as f2:
    f2.write(content)


with open("ph examples.txt", "a") as f:
    content = f.write("\naaj mai yha ja rha hoon")


lines = ["tum mujh kal mile the\n","mere saath ghoomne chaloge?\n","mere ghar par  aaj koi function hai\n"]
with open("ph example.txt","w") as f:
    f.writelines(lines)
print("Lines written successfully")


with open("ph examples.txt","r") as f:
    lines = f.readlines()
    for line in lines[ :5]:
        print(line)


try:
    with open("ph example1.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")


with open("ph examples.txt","r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"line {line_number}:  {line.strip()}")


report_text = """Data Analysis Report
---------------------
Project: Sales Data Review
Date: 17 July 2026

Summary:
- Total records processed: 5000
- Missing values handled: 120
- Average sales per region calculated
- Top 3 performing regions identified

Conclusion:
Data cleaned successfully and ready for SQL integration.
"""
with open("fh3.txt", "w") as f:
    f.write(report_text)
    print("file created successfully")


with open("fh3.txt","r") as f:
    words = f.read().split()
    longest_word = words[0] 
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print ("longest_word:", longest_word)



with open("fh3.txt", "r") as f:
    words = f.read().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency = word
    print(frequency)



with open("fh3.txt","r") as f1, open("fh2.txt","w") as f2:
    for line in f1:
        if line.strip() != "" :
            f2.write(line)
    print("Blank removes sucessfully")


with open("fh4.txt","r") as f:
    words = f.read().split()
    frequency = {}
def return_frequent_words(words):
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency = word
    return(frequency)``


    






🔹 10 Basic File Handling Questions
Read a text file and print its contents.

Count the number of lines in a file.

Count the number of words in a file.

Copy contents from one file to another.

Append new text to an existing file.

Write multiple lines into a file using writelines().

Read a file and print only the first 5 lines.

Check if a file exists before opening it.

Read a file and print each line with its line number.

Create a new file and write a short report into it.

🔹 10 Intermediate File Handling Questions
Read a file and return the longest word.

Count the frequency of each word using a dictionary.

Remove blank lines from a file.

Return the top 5 most frequent words.

Merge two text files into one.

Count how many times a given word appears in a file.

Reverse the contents of a file (line order).

Read a file and return all unique words using a set.

Read a file and return the average word length.

Write a program to replace all occurrences of a word in a file with another word.

🔹 10 Advanced File Handling Questions
Read a CSV file (without Pandas) and print each row.

Parse a CSV file and calculate the average of a numeric column.

Detect duplicate rows in a CSV file.

Read a JSON file and convert it into a dictionary.

Extract specific keys from a JSON file and print them.

Split a large text file into two smaller files (first half, second half).

Read a file and return the longest line.

Count vowels and consonants in a file.

Read a log file and return the count of error messages.

Simulate a mini SQL query: read a CSV and filter rows where a column matches a condition.





                                           