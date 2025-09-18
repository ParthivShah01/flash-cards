# import streamlit as st
# from PyPDF2 import PdfReader, PdfWriter
# import google.generativeai as genai
# from io import BytesIO
# import json

# if "json_qna" not in st.session_state:
#    st.session_state["json_qna"] = []

# if "is_generated" not in st.session_state:
#    st.session_state["is_generated"] = False
   
# #Helper functions
# def flashcards(json_qna):
#     # Initialize session state
#     if "card_index" not in st.session_state:
#         st.session_state.card_index = 0

#     # CSS for flip animation
#     st.markdown("""
#         <style>
#         .flashcard {
#             background-color: transparent;
#             width: 350px;
#             height: 220px;
#             perspective: 1000px;
#             margin: 20px auto;
#         }
#         .flashcard-inner {
#             position: relative;
#             width: 100%;
#             height: 100%;
#             text-align: center;
#             transition: transform 0.8s;
#             transform-style: preserve-3d;
#         }
#         .flashcard:hover .flashcard-inner {
#             transform: rotateY(180deg);
#         }
#         .flashcard-front, .flashcard-back {
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             -webkit-backface-visibility: hidden;
#             backface-visibility: hidden;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             padding: 15px;
#             border-radius: 12px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#             font-size: 16px;
#         }
#         .flashcard-front {
#             background-color: #f8f9fa;
#             color: #333;
#         }
#         .flashcard-back {
#             background-color: #007bff;
#             color: white;
#             transform: rotateY(180deg);
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Current card
#     idx = st.session_state.card_index
#     qa = json_qna[idx]

#     # Render flashcard
#     st.markdown(f"""
#     <div class="flashcard">
#       <div class="flashcard-inner">
#         <div class="flashcard-front">
#           <b>Q{idx+1}:</b> {qa['question']}
#         </div>
#         <div class="flashcard-back">
#           {qa['answer']}
#         </div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Navigation buttons
#     col1, col2, col3 = st.columns([1,2,1])
#     with col1:
#         if st.button("⬅️ Previous", use_container_width=True):
#             if st.session_state.card_index > 0:
#                 st.session_state.card_index -= 1
#                 st.rerun()
#     with col3:
#         if st.button("Next ➡️", use_container_width=True):
#             if st.session_state.card_index < len(json_qna) - 1:
#                 st.session_state.card_index += 1
#                 st.rerun()

#     # Progress indicator
#     st.write(f"Card {idx+1} of {len(json_qna)}")


# def get_page_count(pdf_file):
#   reader = PdfReader(pdf_file)
#   num_pages = len(reader.pages)
#   max=num_pages
#   if(num_pages>=5):
#     max=5
#   return len(reader.pages), max

# def extract_text_from_pdf(pdf_obj):
#     reader = PdfReader(pdf_obj)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""   # handle pages with no text layer
#     return text

# def get_json_qna(text):
#   GOOGLE_API_KEY = 'AIzaSyDZ59r0tkW27sTwONQyXNb8257lgHCXoiw'
#   genai.configure(api_key = GOOGLE_API_KEY)
#   model = genai.GenerativeModel('gemini-1.5-flash')
#   response = model.generate_content(
#       "generate pure json of question and answer pair from the given content" \
#       f"{text}"
# )
#   return response.text




# def pdf_extract_pages(pdf_file, start, end):
#   reader = PdfReader(pdf_file)
#   writer = PdfWriter()
#   start-=1
#   for x in range(start, end):
#     writer.add_page(reader.pages[x])

#   output_pdf = BytesIO()
#   writer.write(output_pdf)
#   output_pdf.seek(0) 
  
#   # with open("extracted.pdf", "wb") as f:
#   #   f.write(output_pdf.read())
#   return output_pdf

# st.title("Flashcards Generator")

# #1. Upload pdf 
# pdf_file = st.file_uploader("Upload Textbook PDF", type="pdf")

# if(pdf_file):
#   num_pages, max = get_page_count(pdf_file)

#   #2. Get range of pages
#   selected_range = st.slider(
#       "Select a range of page numbers",
#       min_value=1,
#       max_value=num_pages,
#       value=(1, max)  
#   )

#   if st.button("Generate Flash Cards", type="primary"):
#     #3. Extract pages from pdf within range 
#     extracted_pdf = pdf_extract_pages(pdf_file, selected_range[0], selected_range[1])

#     #4. Extract text from the pdf pages
#     text = extract_text_from_pdf(extracted_pdf)
    
#     #5. Get JSON of question answers
#     raw_json = get_json_qna(text)
#     string_json = raw_json[7:-4]
#     json_qna = json.loads(string_json)
#     st.session_state["json_qna"] = json_qna
#     st.session_state["is_generated"] = True


# if(st.session_state["is_generated"] == True):
#     #6. Generate Flash Cards

#     flashcards(st.session_state["json_qna"])

