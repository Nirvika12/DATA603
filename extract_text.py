import sys
import math
from PyPDF2 import PdfReader


# My birthday is on 12th September 1999
# This is a function to select book based on birth month
def select_book_range(birth_month):
    book_ranges = {
        1: (4, 515),    # Philosopher's Stone (Pages 4 - 515)
        2: (519, 1083),  # Chamber of Secrets (Pages 519 - 1083)
        3: (1087, 1807),  # Prisoner of Azkaban (Pages 1087 - 1807)
        4: (1811, 3090), # Goblet of Fire (Pages 1811 - 3090)
        5: (3095, 4794), # Order of the Phoenix (Pages 3095 - 4794)
        6: (4799, 5942), # Half-Blood Prince (Pages 4799 - 5942)
        7: (5946, 7287)  # Deathly Hallows (Pages 5946 - 7287)
    }
    
    # for months btwn 8-12 divide it by 2 and round it up.
    if birth_month >= 8 and birth_month <= 12:
        index = math.ceil(birth_month / 2)
    else:
        index = birth_month
    
    return book_ranges.get(index, (4, 515))  # Setting default to Philosopher's Stone if not found

# This is a function to extract text from a pdf
def extract_pages(file_path, start_page, page_count, output_path):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    
    # handling if pages exceed the book
    if start_page + page_count > total_pages:
        page_count = total_pages - start_page
    
    # write to output file
    with open(output_path, 'w', encoding='utf-8') as text_file:
        for page_num in range(start_page, start_page + page_count):
            text = reader.pages[page_num].extract_text()
            if text:
                text_file.write(text + '\n')

# Main function 
def main():
    if len(sys.argv) < 5:
        print("Usage: python extract_text.py <pdf_path> <birth_month> <birth_date> <birth_year>")
        sys.exit(1)
    
    # Reading command line arguments
    pdf_path = sys.argv[1]         # book path
    birth_month = int(sys.argv[2]) # Birth month 
    birth_date = int(sys.argv[3])  # Birth date 
    birth_year = int(sys.argv[4])  # Birth year 
    
    # Select book based on birth month
    book = select_book_range(birth_month)
    
    # Part 1: Extract next 10 pages starting from the birth date into file1.txt
    date_start_page = book[0] + birth_date - 1 #subtracting 1 due to 0 indexing
    extract_pages(pdf_path, date_start_page, 10, 'file1.txt')
    print(f"Pages based on birth date extracted to 'file1.txt'")
    
    # Part 2: Extract next 10 pages into another text file (file2.txt) starting from birth year(last 2 digits)
    year = birth_year % 100  #last 2 digits
    
    year_start_page = book[0] + year - 1 #subtracting 1 due to 0 indexing
    extract_pages(pdf_path, year_start_page, 10, 'file2.txt')
    print(f"Pages based on birth year extracted to 'file2.txt'")

# Execute the main function
if __name__ == "__main__":
    main()
