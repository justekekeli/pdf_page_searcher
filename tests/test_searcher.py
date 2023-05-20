import sys
sys.path.append('../page_searcher/')
from main import main
from PyPDF2 import PdfReader
import os
from click.testing import CliRunner

def test_find_output():
    """ test if the ouput of findpage is what want we want"""
    runner = CliRunner()
    result = runner.invoke(main, ['findpage','ml.pdf','machine learning','4'])
    assert '[5, 7, 10, 12, 24, 119, 121, 126, 127]' in result.output

def test_extract_output():
    """ TODO: test if the ouput of extract_ouput is what want we want"""

def test_number_pages():
    """ TODO: test if the number of pages to extract page don't exceed the number of page of the PDF"""
    pass

def test_first_page_index():
    """ TODO: Test if the first page to extract in not out of bound"""
    pass