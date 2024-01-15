# Ask your PDF: Streamlit and OpenAI Application
## Overview
This project is a Streamlit web application that uses OpenAI's GPT model to summarize PDF documents. The application allows users to upload a PDF, then extracts the text and generates summaries in Turkish.

# What the Code Does
Uploads PDF: Users can upload a PDF file to the application.  
Extracts Text: The text is extracted from the PDF using pdfplumber.  
Summarizes Text: The extracted text is sent to OpenAI's GPT model, which generates summaries in Turkish. This process is done in multiple stages to refine the summary.  
Displays Summaries: The application displays these summaries on the web page.  
Handles Errors: Includes error handling for issues like rate limits and connection errors with OpenAI.  
# What I Learned
Streamlit for Web Apps: Learned how to use Streamlit to create interactive web applications.  
Text Extraction from PDF: Gained experience in extracting text from PDF files using pdfplumber.  
Integrating OpenAI API: Learned to integrate and use OpenAI's API for text summarization.  
Handling API Limitations: Developed skills in handling API limitations like rate limits and errors.  
Iterative Summarization Process: Understood the process of breaking down text into chunks for summarization and refining the summary in stages.  
# Simple and Efficient  
This project demonstrates a simple yet efficient way to use AI for practical purposes like summarizing documents. It's a great example of how different technologies can be combined to create useful applications.  
