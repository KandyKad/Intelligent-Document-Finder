from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summa import summarizer
from summa import keywords

def convert_pdf_to_txt(path, pages=None):'''conversion of pdf into text'''
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open('file path', 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    sample = text

    stop_words = set(stopwords.words('english'))#stopwords

    word_tokens = word_tokenize(sample)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    new_sentence = ' '.join(filtered_sentence)
    
    print(keywords.keywords(text))#keywords
    txt=summarizer.summarize(text)#summary
    print(summarizer.summarize(txt))

    return text
text = convert_pdf_to_txt('file path', pages=[0,1,2,3,4])

