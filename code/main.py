# -*- coding: utf-8 -*-
"""
This calls the quarto render function, which renders a qmd file
You have to have both the quarto library and various other libraries installed
You can use the requirements.txt file

"""

import quarto
import os
from datetime import date

def renderAsDoc(qmd_folder, qmd_file, output_format):
    # this is just my function around the quarto.render() function
    os.chdir(qmd_folder)
    quarto.render(input=qmd_file, output_format=output_format)
    
def replaceThingsInYourQMD(qmd_folder, qmd_file, replacement_dictionary, new_qmd_file):
    # this reads in your qmd and searches and replaces text based on a dictionary
    # and then outputs it with a different name
    os.chdir(qmd_folder)
    with open(qmd_file, 'r') as file :
      filedata = file.read()
      for key in list(replacement_dictionary.keys()):
          value=replacement_dictionary[key]
          filedata = filedata.replace(key, value)
    with open(new_qmd_file, 'w') as file:
      file.write(filedata)
      
qmd_folder=r"C:\Users\abiga\OneDrive\Documents\Python Scripts\quarto demo\qmds"
qmd_file="meteorites.qmd"
new_qmd_file="meteorites_new_years.qmd"
    
renderAsDoc(qmd_folder, qmd_file, "docx")
renderAsDoc(qmd_folder, qmd_file, "pdf")
renderAsDoc(qmd_folder, qmd_file, "html")
      
replacement_dictionary={'March 03, 2023': date.today().strftime('%B %d, %Y'),
'first_meteor_year=1995': 'first_meteor_year=2000',
'last_meteor_year=2000' : 'last_meteor_year=2023'}


replaceThingsInYourQMD(qmd_folder, qmd_file, replacement_dictionary, new_qmd_file)

renderAsDoc(qmd_folder,new_qmd_file, "docx")
