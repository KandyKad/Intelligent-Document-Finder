from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import nltk                                                  #library uesd to get unique keywords
import re                                                    #library uesd to get unique keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summa import summarizer
from summa import keywords 
from gensim.summarization import keywords as key
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

def stem(word):                                     #function to get unique keywords
	regexp=r'^(.*?)(ing|ly|ed|ious|ies|ive|s|ment)?$'
	stem,suffix=re.findall(regexp,word)[0]
	return stem


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

    return sample

def get_info(path):                                          #function to get number of pages of input pdf
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        text = convert_pdf_to_txt(path, pages=range(0,number_of_pages))        
        LANGUAGE = "english"
        SENTENCES_COUNT = 10
        #url = "https://en.wikipedia.org/wiki/Automatic_summarization"
        #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain strings
        parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE)) #PlaintextParser.from_file for files
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)

        print(keywords.keywords(text))                  #original keywords
        keywordlist1=keywords.keywords(text,split=True)  #list of keywords
        keywordstring=" ".join(keywordlist1)             #string of keywords
        tokens= nltk.word_tokenize(keywordstring)

        print("\n",{stem(t) for t in tokens},"\n")            # gives set of unique kywords    
path='C:\\Users\\AMAN SHAKYA\\Desktop\\Infenion Startup India Project\\folder\\text_summarization.pdf'
get_info(path)

