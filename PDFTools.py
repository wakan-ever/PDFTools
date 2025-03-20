import streamlit as st
from pypdf import PdfReader, PdfWriter
from pdf2image import convert_from_bytes
import img2pdf
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="PDF Utility Tool", page_icon="📄")

# ---------------- Sidebar Navigation with Buttons ---------------- #
st.sidebar.title("📄 PDF Utility Tool")
st.sidebar.markdown("### Choose a Tool:")

# Define session state to remember user selection
if "app_mode" not in st.session_state:
    st.session_state.app_mode = None  # Default selection

# Buttons for selecting tools
if st.sidebar.button("📑 Merge PDFs"):
    st.session_state.app_mode = "📑 Merge PDFs"
if st.sidebar.button("📉 Compress PDFs"):
    st.session_state.app_mode = "📉 Compress PDFs"
if st.sidebar.button("🔒 Encrypt PDFs (User Password)"):
    st.session_state.app_mode = "🔒 Encrypt PDFs (User Password)"

# Assign the selected mode
app_mode = st.session_state.app_mode

# ---------------- Display Introduction on Main Page ---------------- #
if app_mode is None:
    st.title("📄 PDF Utility Tool ")

    st.markdown("""
    ### **🔹 Overview**
    This web-based PDF tool allows you to **merge, compress, and secure PDF files** without needing **Adobe Acrobat** or any paid software.  
    It’s completely **free** and runs on your web browser—no installation required!

    ### **💡 Features**
    ✅ **Merge PDFs** – Combine multiple PDFs into one.  
    ✅ **Compress PDFs** – Reduce file size of scanned PDFs without losing much quality.  
    ✅ **Encrypt PDFs** – Protect your PDFs with passwords.  
    ✅ **No Need for Adobe Acrobat** – 100% free and online!  

    ---
    
    ### **📌 How to Use**
    1️⃣ Select a tool from the **sidebar**.  
    2️⃣ Upload your PDF(s).  
    3️⃣ Click the **Download** button when processing is complete.  
    """)

    st.info("👈 **Use the sidebar to select a tool and get started!**")


# ---------------- PDF Functions ---------------- #
def merge_pdfs(uploaded_files):
    merger = PdfWriter()
    for uploaded_file in uploaded_files:
        merger.append(uploaded_file)

    output_buffer = BytesIO()
    merger.write(output_buffer)
    merger.close()
    output_buffer.seek(0)

    return output_buffer

def compress_scanned_pdf(uploaded_pdf, dpi=100, quality=60):
    images = convert_from_bytes(uploaded_pdf.getvalue(), dpi=dpi)
    processed_images = []

    for img in images:
        img = img.convert("RGB")
        img_io = BytesIO()
        img.save(img_io, format="JPEG", quality=quality)
        processed_images.append(img_io.getvalue())

    output_pdf = BytesIO()
    output_pdf.write(img2pdf.convert(processed_images))
    output_pdf.seek(0)

    return output_pdf

def encrypt_pdf(uploaded_pdf, password):
    reader = PdfReader(uploaded_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    output_pdf = BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf


# ---------------- Page Rendering Based on Selection ---------------- #
if app_mode:
    st.title(app_mode)


if app_mode == "📑 Merge PDFs":
    st.subheader("Merge Multiple PDFs")
    
    st.info("### How to Use:\n1️⃣ Upload two or more PDF files.\n\n"
            "2️⃣ The tool will merge them in the order you upload them.\n\n"
            "3️⃣ Click 'Download Merged PDF' to save the combined file.")
    
    uploaded_files = st.file_uploader("Upload PDFs to merge", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        merged_pdf = merge_pdfs(uploaded_files)
        st.success("✅ PDFs successfully merged!")
        st.download_button(
            label="📥 Download Merged PDF",
            data=merged_pdf,
            file_name="merged.pdf",
            mime="application/pdf"
        )

elif app_mode == "📉 Compress PDFs":
    st.subheader("Compress Scanned PDFs")

    st.info("### How to Use:\n1️⃣ Upload a **scanned** PDF file.\n\n"
            "2️⃣ This tool reduces file size by compressing images inside the PDF.\n\n"
            "3️⃣ Click 'Download Compressed PDF' to save your optimized file.")

    uploaded_file = st.file_uploader("Upload a scanned PDF", type="pdf")

    if uploaded_file:
        st.write("🔄 Processing...")
        compressed_pdf = compress_scanned_pdf(uploaded_file)
        st.success("✅ Compression successful! File size reduced.")
        st.download_button(
            label="📥 Download Compressed PDF",
            data=compressed_pdf,
            file_name="compressed.pdf",
            mime="application/pdf"
        )

elif app_mode == "🔒 Encrypt PDFs (User Password)":
    st.subheader("Encrypt a PDF with a Password")

    st.info("### How to Use:\n1️⃣ Upload a PDF file you want to protect.\n\n"
            "2️⃣ Enter a strong password.\n\n"
            "3️⃣ Click 'Download Encrypted PDF' to save your protected file.\n\n"
            "🔐 **Once encrypted, only users with the password can open the file.**")

    uploaded_file = st.file_uploader("Upload a PDF to encrypt", type="pdf")
    password = st.text_input("🔑 Enter Password", type="password")

    if uploaded_file and password:
        encrypted_pdf = encrypt_pdf(uploaded_file, password)
        st.success("✅ PDF successfully encrypted!")
        st.download_button(
            label="📥 Download Encrypted PDF",
            data=encrypted_pdf,
            file_name="protected.pdf",
            mime="application/pdf"
        )
