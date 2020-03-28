from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import nltk '''library uesd to get unique keywords'''
import re   '''library uesd to get unique keywords'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summa import summarizer
from summa import keywords

def convert_pdf_to_txt(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(path, 'rb')
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
    print(keywords.keywords(text))#original keywords
    txt=summarizer.summarize(text,ratio=0.2)#summary of original summary(SAY NEW)
    print(txt)
    print(summarizer.summarize(txt,ratio=0.2))
    summarylist=summarizer.summarize(text,split=True)#list of new
    summarystring=" ".join(summarylist)#string of NEW
    
    b=keywords.keywords(summarystring,split=True)#keywords obtained from string of NEW

    keywordlist1=keywords.keywords(text,split=True)#list of keywords
    keywordstring=" ".join(keywordlist1)#string of keywords
    keywordlist2=keywords.keywords(keywordstring,split=True)
    tokens= nltk.word_tokenize(keywordstring)
    print({stem(t) for t in tokens})      # gives set of unique kywords
    print(len({stem(t) for t in tokens})) # gives number of unique kywords


    return text

def get_info(path):                #function to get number of pages of input pdf
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        text = convert_pdf_to_txt(path, pages=range(0,number_of_pages))
        
def stem(word):                    #function to get unique keywords
	regexp=r'^(.*?)(ing|ly|ed|ious|ies|ive|s|ment)?$'
	stem,suffix=re.findall(regexp,word)[0]
	return stem
    
path='C:/Users/AMAN SHAKYA/Desktop/Infenion Startup India Project/folder/text_summarization.pdf'
get_info(path)

