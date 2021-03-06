import fitz

def get_images(PDF_PATH: str, i: int) -> None:
    pdf_file = fitz.open(PDF_PATH)
    source = pdf_file.name.replace("dataset/", "")
    for img in pdf_file.get_page_images(i):
        xref = img[0]
        pix = fitz.Pixmap(pdf_file, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.save("p%s-%s-%s.png" % (i, xref, source), "img")
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.save("p%s-%s-%s.png" % (i, xref, source))
            pix1 = None
        pix = None
