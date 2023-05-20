from PyPDF2 import PdfFileReader
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
        pdf = PdfFileReader(file)

        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            text = page.extract_text()

            if text.lower().count(search_text.lower()) >= times:
                pages_with_text.append(page_num)

    if pages_with_text:
        print(f"The text '{search_text}' was found on the following pages:")
        print(pages_with_text)
    else:
        print(f"The text '{search_text}' was not found in the PDF.")

    return pages_with_text

@main.command()
@click.argument('pdf',type= click.Path(exists=True))
@click.argument('numfirstpage', type=int)
@click.argument('numpages', type=int)
@click.option('-o', '--output', default='output.pdf', help='Output PDF file path')
def extractpages(pdf, numfirstpage, numpages,outputfile):
    """ Extract a block of pages from a pdf """
    output_pdf = PdfFileWriter()
    with open(pdf, 'rb') as file:
        pdf = PdfFileReader(file)
        for page_num in range(numfirstpage, numfirstpage + numpages):
            if page_num < pdf.numPages:
                page = pdf.getPage(page_num)
                output_pdf.addPage(page)
    
        with open(outputfile, 'wb') as output_file:
            output_pdf.write(output_file)

    print(f"Extracted pages saved as '{output_file}'.")

if __name__ == '__main__':
    main()