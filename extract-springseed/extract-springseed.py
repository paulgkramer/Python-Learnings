import json
from os import listdir
import sys
import os.path

Location = "/Users/Paul/GitHub/Python-Learnings/extract-springseed/extract-springseed-files/"
output_location = "/Users/Paul/GitHub/Python-Learnings/extract-springseed/output/"
notebook_dict = {}


def write(filename,content):
    print('Creating new text file: ' + filename)

    name = filename  # Name of text file coerced with +.txt

    try:
        file = open(filename,'w')   # Trying to create a new file or open one
        file.write(content)
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python




# def create_notebook():

for filename in listdir(Location):

  extension = os.path.splitext(filename)[1]

  if extension == ".list":
    list_filename = Location + filename
    notebook_file_contents = open(list_filename).read()
    notebook_id = eval(notebook_file_contents)['id']
    notebook_name = eval(notebook_file_contents)['name']
    notebook_dir = output_location + notebook_name

    if not os.path.exists(notebook_dir):
      os.makedirs(notebook_dir)
      notebook_dict[notebook_id] = notebook_name



# def create_note():

for filename in listdir(Location):

  extension = os.path.splitext(filename)[1]

  if extension == ".note":
    json_filename = Location + filename
    json_file_contents = open(json_filename).read()

    str_content = eval(json_file_contents)['content']
    notebook_id = eval(json_file_contents)['notebook']
    note_name = eval(json_file_contents)['name'].replace('/', '')
    note_directory = [val for key, val in notebook_dict.items() if notebook_id in key]


    output_filename = output_location + note_directory[0] + "/" + note_name

    write(output_filename,str_content)


  # create_notebook()
  # create_note()
