#!/usr/bin/python
import os, sys

# TODO: MORE COMMENTS

#set path

script_dir = os.path.dirname(os.path.abspath(__file__)) #<-- absolute dir the script is in
start_dir = "books" # use "." if books are in current directory
path = os.path.join(script_dir, start_dir)

items = os.listdir( path )

# List of all sub directories to startpath:
dirs = [x[0] for x in os.walk(path)]

# This would print all the files and directories

f = open('output.html','w')

for subdir in dirs:

   files = []
   for file in os.listdir(subdir):
      if os.path.isfile(os.path.join(subdir, file)):
         files.append(os.path.join(subdir, file))

   f.write("<h2>"+os.path.relpath(subdir, path)+"</h2><br>"+'\n')
   
   #print(files)
   

   for file in files:
         #print ( file )
         relativePath = os.path.relpath(file, subdir)
         nopdf = os.path.splitext(relativePath)[0]
         #print ( nopdf )
         f.write("<a target=\"_blank\" href=\"/"+file+"\""+">"+nopdf+"</a> <br>"+'\n')

f.close()
