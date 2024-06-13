[*Markdown Cheatsheet*](https://www.markdownguide.org/cheat-sheet/)

## Installation
#### Create virtual python environment(.venv) running python 3.12
##### On Mac
1. Open Terminal
2. Navigate to the directory where you want to create the virtual env
3. Create venv: `python3 -m venv env`
4. Activate: `source env/bin/activate`
5. Install Libraries with pip(possibly pip3)
6. When you're done, deactivate: `deactivate'
*you will need to activate venv in each terminal you want to use it*


#### Libraries
**PyMuPDF**
`pip install pymupdf`
[docs](https://pymupdf.readthedocs.io/en/latest/rag.html#rag-outputting-as-md)

**PyMuPDF4LLM**
`pip install pymupdf4llm`
[docs](https://pymupdf4llm.readthedocs.io/en/latest/index.html)
(installed both to explore functionality)

**pathlib**
native
[docs](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)





#### Subproblems
##### Opening files
###### Problem: 
  PyMuPDF does not try to determine the file type from file contents
  - implicitly determined through file extension, if extension missing or unknown,
    then it assumes it's a pdf
    `doc = pymupdf.open("some.file")`

  - explicitly with the file type parameter 
    `.open("some.file', filetype="json")`

###### Solution:
  Filter the files at imput using [filetype](https://pypi.org/project/filetype/)


#### Common Problems and Solutions
[docs](https://pymupdf.readthedocs.io/en/latest/recipes-common-issues-and-their-solutions.html)
Convert input file to pdf boilerplate may be of use
