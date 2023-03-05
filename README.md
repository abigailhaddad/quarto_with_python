# quarto_with_python

The purpose of this is to use Python (from within Python, not the command line) to call Quarto to generate PDFs, Word docs, and HTML. 

 The *main.py* file contains a couple of pieces of functionality:
  * Calling quarto.render() to render files
  * Using search and replace to modify the .qmd file (in this case, to change the date displayed and change the years that the code uses to filter the meteorite data)
  
 The purpose of the search/replace function is to edit the QMD file without doing it manually -- it's a way of passing it parameters, although it's not an ideal one because you have to make sure you don't have the text strings in search in any other places in your file.
 
-The *meteorites.qmd* file in the qmd folder is the file used by main.py to generate the files in the qmd folder starting with "meteorites." 

These are:

  * A PDF
  * A Word file
  * An HTML file

-The main.py reads in meteorites.qmd, makes changes to it (date displayed and years filtering the data), and saves it as meteorites_new_years.qmd, and then outputs a Word file based on this new file.

