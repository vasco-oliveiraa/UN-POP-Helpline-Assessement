import streamlit as st
from fpdf import FPDF
import base64

from Recommendations.Accessibility import accessibility

export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    
    # Get the rendered HTML string from the Streamlit component
    html_string = accessibility.get_iframe_html()

    # Add the HTML string to the PDF
    pdf.multi_cell(0, 10, html_string)
    
    # Generate the PDF file
    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    # Create the download link
    download_link = create_download_link(pdf_bytes, "test")

    # Display the download link
    st.markdown(download_link, unsafe_allow_html=True)
