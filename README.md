# page-searcher
The CLI can be used to search a text in a PDF that occurs a number of times  or extract a block of pages from the pdf file

## Installation

    `python setup.py develop`

## Tutorial to use page-search

### 1. extractpages : 
There is an example of command to extract 4 pages from examples/ml.pdf and the first page to extract is the third page:

    `page-searcher extractpages examples/ml.pdf 3 4 `

By default the output pdf is called output.pdf bu you can change it :

    `page-searcher extractpages examples/ml.pdf 3 4 -o pdf_output.pdf` 
    or 
    `page-searcher extractpages examples/ml.pdf 3 4 --output pdf_output.pdf`

### 2. findpage : 
There is an example of command that return the list of pages's indexes that have the text 'machine learning' in it at least for 4 times:

    `page-searcher findpage examples/ml.pdf 'machine learning' 4 `


    