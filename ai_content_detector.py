# -*- coding: utf-8 -*-
"""AI_Content_Detector.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ksem6lvX2U-8xha3dKs7tX8VyKShDvCp
"""

pip install fitz

pip install regex

pip install NLTK

pip install frontend

pip install pymupdf

pip install  PyPDF4

pip install NLTK

import nltk
nltk.download('punkt')

pip install Decimal

import re
from nltk import ngrams
from collections import Counter
import math
from io import BytesIO
import requests
import PyPDF4
from nltk.tokenize import word_tokenize
import fitz

# Function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove non-alphanumeric characters and extra whitespaces
    text = re.sub(r'[^a-z0-9\s]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    
    # Split text into tokens
    tokens = text.split()
    
    return tokens

# Function to calculate perplexity of text using n-gram model with sliding window
def calculate_perplexity(text, n=3):
    # Preprocess text
    tokens = preprocess_text(text)
    
    # Generate n-grams
    ngrams_list = list(ngrams(tokens, n))
    
    # Count n-grams
    ngrams_counts = Counter(ngrams_list)
    
    # Calculate total number of n-grams
    total_ngrams = sum(ngrams_counts.values())
    
    # Calculate perplexity score
    entropy = 0
    for ngram in ngrams_counts:
        prob = ngrams_counts[ngram] / total_ngrams
        entropy += -math.log(prob, 2)
    perplexity = 2**entropy
    
    return perplexity

# Ask user for PDF file path
pdf_file_path = input("Enter the path to your PDF file: ")

# Open the PDF file in read-binary mode
with open(pdf_file_path, 'rb') as pdf_file:
    # Create a PyPDF4 PdfFileReader object
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()
    
    # Loop through each page and extract the text
    for page_num in range(num_pages):
        # Get the page object
        page_obj = pdf_reader.getPage(page_num)
        
        # Extract the text from the page
        page_text = page_obj.extractText()

        tokens = word_tokenize(page_text)
        # Count the number of words
        num_words = len(tokens) 

# Display perplexity score
print("Perplexity of the PDF file is:", (perplexity_score))

#perplexity_percentage = 100 / 2**(perplexity_score / num_words)


from decimal import Decimal
        
# function to calculate perplexity percentage
def calculate_perplexity_percentage(perplexity_score, num_words):
    z = 0
    perplexity = Decimal(perplexity_score) ** Decimal(1/num_words)
    perplexity_percentage = Decimal(100) / perplexity
    return perplexity_percentage

     
perplexity_score = calculate_perplexity(page_text)

try:
  print("Perplexity of the PDF file is:", (perplexity_score))
  perplexity_percentage = calculate_perplexity_percentage(perplexity_score, num_words)
  print(f"The perplexity percentage is: {perplexity_percentage:.2f}%")
except:
  print("Cannot divide by zero")


if perplexity_percentage < 50:
    print("The document is AI generated")
else:
    print("The document is not AI generated")