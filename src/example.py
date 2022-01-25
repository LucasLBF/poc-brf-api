from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

PDF_PATH = "dataset/habitos_de_consumo_snacks.pdf"

def with_pdf (pdf_doc, fn, pdf_pwd="", *args):
    result = None
    try:
        # open the pdf file
        fp = open(pdf_doc, 'rb')
        # create a parser object associated with the file object
        parser = PDFParser(fp)
        # create a PDFDocument object that stores the document structure
        doc = PDFDocument(parser)
        # connect the parser and document objects
        parser.set_document(doc)
        # doc.set_parser(parser)
        # supply the password for initialization
        # doc.initialize(pdf_pwd)
        if doc.is_extractable:
            # apply the function and return the result
            result = fn(doc, *args)
        # close the pdf file
        fp.close()
    except IOError:
        # the file doesn't exist or similar problem
        pass
    return result

def _parse_toc(doc):
    toc = []
    try:
        outlines = doc.get_outlines()
        for (level, title, dest, a, se) in outlines:
            toc.append((level, title))
    except:
        pass
    return toc

def get_toc(pdf_doc, pdf_pwd=""):
    return with_pdf(pdf_doc, _parse_toc ,pdf_pwd)

## PAGE PARSING
def _parse_pages (doc):
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in doc.get_pages():
        interpreter.process_page(page)
        # receive the LTPage object for this page
        layout = device.get_result()
        # layout is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.

def get_pages (pdf_doc, pdf_pwd=''):
    with_pdf(pdf_doc, _parse_pages, pdf_pwd)
