from PyPDF2 import PdfReader,PdfWriter
import click

@click.group()
def main():
    pass

@main.command()
@click.argument('pdf',type= click.Path(exists=True))
@click.argument('search_text', type=str)
@click.argument('times', type=int)
def findpage(pdf, search_text, times):
    """ Return the indexes of the pages that contains the search text """
    pages_with_text = []

    with open(pdf, 'rb') as file:
        pdf = PdfReader(file)

        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text = page.extract_text()

            if text.lower().count(search_text.lower()) >= times:
                pages_with_text.append(page_num)

    if pages_with_text:
        click.echo(f"The text '{search_text}' was found on the following pages:")
        click.echo(pages_with_text)
    else:
        click.echo(f"The text '{search_text}' was not found in the PDF.")

    return pages_with_text

@main.command()
@click.argument('pdf',type= click.Path(exists=True))
@click.argument('numfirstpage', type=int)
@click.argument('numpages', type=int)
@click.option('-o', '--output', default='output.pdf', help='Output PDF file path')
def extractpages(pdf, numfirstpage, numpages,output):
    """ Extract a block of pages from a pdf """
    output_pdf = PdfWriter()
    with open(pdf, 'rb') as file:
        pdf = PdfReader(file)
        nb_pages = len(pdf.pages)
        if numfirstpage > nb_pages:
            raise IndexError(f'The first page is out of the bound , the pdf has {nb_pages}')
        
        if numfirstpage + numpages > nb_pages:
            raise IndexError(f'The number of pages to extract is out of the bound , the pdf has {nb_pages}')
        
        for page_num in range(numfirstpage, numfirstpage + numpages):
                page = pdf.pages[page_num]
                output_pdf.add_page(page)
    
        with open(output, 'wb') as output_file:
            output_pdf.write(output_file)

    click.echo(f"Extracted pages saved as '{output}'.")

if __name__ == '__main__':
    main()