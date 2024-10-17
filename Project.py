import streamlit as st
import PyPDF2
import google.generativeai as genai

import PIL.Image 

my_secret = st.secrets['GEMINIKEY']
genai.configure(api_key=my_secret)
model = genai.GenerativeModel("gemini-1.5-flash",
  system_instruction ="""
  You are a teahcer who are able to help learners to succeed in the essay writing especially in English Language.
  The learner will have their input in the form of file, image or text. 
  You will check the file, image or text and give the output with the list below:
  1. strengths and weaknesses based on the essay that they have given. 
  2. which type of essay that is suitable to them. The type of essay would be narraitve, argumentative, expository, and persuasive. 

  """)


# def upload_files():
#         """Uploads files and images simultaneously and stops when the user is done."""

#         # Create a container to hold the file uploaders
#         file_upload_container = st.container()

#         # Allow multiple file uploads
#         uploaded_files = file_upload_container.file_uploader(
#             "Upload Files or Images",
#             accept_multiple_files=True,
#             type=["pdf", "jpg", "png", "txt", "csv", "docx", "xlsx", "mp3", "mp4"]  # Add more types as needed
#         )

#         # Display uploaded files
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 st.write(f"Uploaded file: {uploaded_file.name}")

#                 # Save the uploaded file to the local file system
#                 if uploaded_file.name:
#                     # Create a directory if it doesn't exist
#                     os.makedirs("uploads", exist_ok=True)
#                     file_path = os.path.join("uploads", uploaded_file.name)
#                     with open(file_path, "wb") as f:
#                         f.write(uploaded_file.read())

# if st.button("Upload"):
#   upload_files()

# if st.button("Analyse"):
#   upload_files = st.session_state.get("", [])
#   if upload_files:  # Check if the list is not empty
#       response = model.generate_content(upload_files)
#       st.write(response.text)
#   else:
#       st.warning("Please upload files first.")

# if st.button("PDF"):
#   prompt = st.file_uploader("Please upload the pdf here", type="pdf")
#   if prompt is not None:  # Check if a file is uploaded
#     # Read the contents of the uploaded PDF file
#     pdf_file_content = prompt.read() 
#     pdf_reader = PyPDF2.PdfReader(pdf_file_content) 

#     text = ""
#     for page in range(len(pdf_reader.pages)):
#       text += pdf_reader.pages[page].extract_text()
#     response = model.generate_content(text)
#     st.caption(response.text)

# if st.button("Text"):
#   prompt = st.text_input("Enter a prompt")
#   response = model.generate_content(prompt)
#   st.write(response.text)

# if st.button("Image"):
#   prompt = st.file_uploader("Please upload the image here", type="png")
#   if prompt is not None:  # Check if a file is uploaded
#     # Read the contents of the uploaded PDF file
#     PIL.Image.open(prompt)
#     response = model.generate_content(["prompt",image])
#     print(response.text)

if st.button("Analyse"):
  with open("UBMM1011_FICT_G13_Alibaba Group Holdings Limited.pdf", "rb") as pdf_file:
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      # Extract text from the PDF
      text = ""
      for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
      response = model.generate_content(text,generation_config= genai.types.GenerationConfig(
                                         max_output_tokens=20,
                                         stop_sequences=[","],
                                         temperature =0)
                                       )    
  with open("UBMM1011_FICT_G11_MICROSOFT CORPORATION (2).pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Extract text from the PDF
    text = ""
    for page in range(len(pdf_reader.pages)):
      text += pdf_reader.pages[page].extract_text()
    response = model.generate_content(text)

  
  with open("UBMM1011_FICT_L4_G12_Nestle.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Extract text from the PDF
    text = ""
    for page in range(len(pdf_reader.pages)):
      text += pdf_reader.pages[page].extract_text()
    response = model.generate_content(text)
  
  st.write(response.text)
  
  
