import os
import openai
from openai import Completion
import streamlit as st
from io import BytesIO
import pdfplumber
import time

openai_key = st.secrets["OPENAI_KEY"]
openai.api_key = openai_key

def main():
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    # extract the text
    if pdf is not None:
        try:
            # convert the uploaded pdf into a stream
            pdf_stream = BytesIO(pdf.getvalue())

            # Use pdfplumber to extract text
            with pdfplumber.open(pdf_stream) as pdf:
                text = '\n'.join(page.extract_text() for page in pdf.pages)

        except Exception as e:
            text = None
            st.error(f"Failed to extract text from PDF: {e}")

        if text:
            # split the text into chunks of approximately 2000 characters each
            chunk_size = 4000
            chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

            summaries = []
            total_tokens_used = 0
            chunk_count = 0
            # iterate over each chunk and summarize it

            st.header("İLK GRUP ÖZETLERİ:")
            for chunk in chunks:
              while True: # keep trying until the request succeeds
                try:
                  response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=[
                          {"role": "system", "content": f"Your task is to summarize the following text in Turkish Language(Don't give me any English text. İf important you can give me technical terms in english by specifying the Turkish Meaning in parantheses.):\n\n{chunk}"},
                      ],
                      max_tokens=2000
                  )
                  summary = response['choices'][0]['message']['content'].strip()
                  summaries.append(summary)
                  
                  st.write(summary)
                  tokens_used = response["usage"]["total_tokens"]
                  total_tokens_used += tokens_used
                  chunk_count += 1
                  print(f'Tokens used: {response["usage"]["total_tokens"]} and total tokens so far: {total_tokens_used} and {chunk_count}. chunk')
                  break
                except openai.error.RateLimitError as e:
      # if a RateLimitError occurred, wait for 60 seconds before retrying
                  print(f'We are waiting for rate limit for 120 seconds: {e}')
                  time.sleep(120)
                  pass
                except openai.error.APIError as e:
                  #Handle API error here, e.g. retry or log
                  print(f"OpenAI API returned an API Error: {e}")
                  time.sleep(120)
                  pass
                except openai.error.APIConnectionError as e:
                  #Handle connection error here
                  print(f"Failed to connect to OpenAI API: {e}")
                  time.sleep(120)
                  pass

            text2 = ' '.join(summaries)
            if text2:
            # split the text into chunks of approximately 2000 characters each
              chunk_size = 4000
              chunks2 = [text2[i:i+chunk_size] for i in range(0, len(text2), chunk_size)]

              summaries2 = []

          # THIS IS FOR SECOND TIME SPLIT SUMMARY TEXT INTO CHUNKS.
              st.header("İKİNCİ GRUP ÖZETLERİ:")
              for chunk in chunks2:
                while True:
                  try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": f"Your task is to summarize the following text in Turkish Language(Don't give me any English text. İf important you can give me technical terms in english by specifying the Turkish Meaning in parantheses.):\n\n{chunk}"},
                        ],
                        max_tokens=2000
                    )

                    summary2 = response['choices'][0]['message']['content'].strip()
                    st.write(summary2)
                    summaries2.append(summary2)
                    tokens_used = response["usage"]["total_tokens"]
                    total_tokens_used += tokens_used
                    chunk_count += 1
                    print(f'Tokens used: {response["usage"]["total_tokens"]} and total tokens so far: {total_tokens_used} and {chunk_count}. chunk  AND THIS IS SECOND CHUNK IN CHUNKS')
                    break
                  except openai.error.RateLimitError as e:
        # if a RateLimitError occurred, wait for 60 seconds before retrying
                    print(f'We are waiting for rate limit for 120 seconds: {e}')
                    time.sleep(120)
                  except openai.error.APIError as e:
                    #Handle API error here, e.g. retry or log
                    print(f"OpenAI API returned an API Error: {e}")
                    time.sleep(120)
                    pass
                  except openai.error.APIConnectionError as e:
                    #Handle connection error here
                    print(f"Failed to connect to OpenAI API: {e}")
                    time.sleep(120)
                    pass
# THIS IS FOR THIRD CHUNK IN CHUNKS

            text3 = ' '.join(summaries2)
            if text3:
            # split the text into chunks of approximately 2000 characters each
              chunk_size = 4000
              chunks3 = [text3[i:i+chunk_size] for i in range(0, len(text3), chunk_size)]

              summaries3 = []

          # THIS IS FOR THIRD TIME SPLIT SUMMARY TEXT INTO CHUNKS.
              st.header("ÜÇÜNCÜ GRUP ÖZETLERİ:")
              for chunk in chunks3:
                while True:
                  try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": f"Your task is to summarize the following text in Turkish Language(Don't give me any English text. İf important you can give me technical terms in english by specifying the Turkish Meaning in parantheses.):\n\n{chunk}"},
                        ],
                        max_tokens=2000
                    )

                    summary3 = response['choices'][0]['message']['content'].strip()
                    
                    st.write(summary3)
                    summaries3.append(summary3)
                    tokens_used = response["usage"]["total_tokens"]
                    total_tokens_used += tokens_used
                    chunk_count += 1
                    print(f'Tokens used: {response["usage"]["total_tokens"]} and total tokens so far: {total_tokens_used} and {chunk_count}. chunk  AND THIS IS THIRD CHUNK IN CHUNKS')
                    break
                  except openai.error.RateLimitError as e:
        # if a RateLimitError occurred, wait for 60 seconds before retrying
                    print(f'We are waiting for rate limit for 120 seconds: {e}')
                    time.sleep(120)
                  except openai.error.APIError as e:
                    #Handle API error here, e.g. retry or log
                    print(f"OpenAI API returned an API Error: {e}")
                    time.sleep(120)
                    pass
                  except openai.error.APIConnectionError as e:
                    #Handle connection error here
                    print(f"Failed to connect to OpenAI API: {e}")
                    time.sleep(120)
                    pass






          # Send combined chunks to OpenAI for a FOURTH AND COMPLETE summarization

              try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"Your task is to summarize the following text in Turkish Language(Don't give me any English text. İf important you can give me technical terms in english by specifying the Turkish Meaning in parantheses.):\n\n{' '.join(summaries3)}"},
                    ],
                    max_tokens=2000
                )

                summary4 = response['choices'][0]['message']['content'].strip()
                st.header("SON ÖZET:")
                st.write(summary4)
                total_tokens_used += tokens_used
                chunk_count += 1
                print(f'Tokens used: {response["usage"]["total_tokens"]} and total tokens so far: {total_tokens_used} and {chunk_count}. chunk AND THIS IS COMPLETE SUMMARY')
              except Exception as e:
                print(f'Tokens used: {response["usage"]["total_tokens"]}')
                st.error(f"Something happend: {e}")




# following text:\n\n{' '.join(chunk)}"}
        else:
            st.error("No text was extracted from the PDF")

if __name__ == '__main__':
    main()
