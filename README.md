# Nail Salon SQL Marketing
 SQL database for nail salons places to export into CSV and send mail ads out

# Getting Started
`pip install pandas`

# Instructions
1. Use the google maps web scraper to grab CSV data of any amount of places or businesses with the name and addresses included.
2. Open the csv file in excel and delete all the columns except for the name and addresses columns.

## Data Manipulation
3. Use excel to mass create insert into commands using concatenation.
4. Open MySQL workbench and connect to your localhost.
5. Create a new SQL script with SQL commands to create a database and a table with name and address columns which must be unique.
6. Copy and paste the insert commands from excel into the script and run the script.
7. Manipulate data with SQL.
8. Run an SQL csv export query to create a csv from the data.

## Continued
9. Create a new folder where you want the edited PDF files and move editpdf.py into it.
10. Also move BOPQUOTE.pdf to that folder.
11. Change csv_path to the location of the csv file.
12. Change pdf_path to the empty pdf you want to add the text from the data into.
13. cd to the new folder and run `python editpdf.py`
14. The edited pdf files will be in the same folder.