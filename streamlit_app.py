import streamlit as st
import qrcode
from PIL import Image
import io

 
def generate_qr_code(data, fill_color='black', back_color='white', box_size=10, border=4):
    """
    Generate a QR code with customizable parameters

    :param data: Text or URL to encode in QR code
    :param fill_color: Color of the QR code
    :param back_color: Background color of the QR code
    :param box_size: Size of each box in the QR code
    :param border: Size of the border
    :return: PIL Image of the QR code
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return qr_img

def main():
    st.title(' QR Code Generator')    

    # Sidebar for customization
    st.sidebar.header('QR Code Customization')

    # Input data
    qr_data = st.text_input('Enter text or URL', placeholder='https://example.com')    

    # Color customization
    col1, col2 = st.columns(2)

    with col1:
        fill_color = st.color_picker('QR Code Color', value='#000000')

    with col2:
        back_color = st.color_picker('Background Color', value='#FFFFFF')

    
    # Size and border
    box_size = st.slider('QR Code Size', min_value=5, max_value=20, value=10)
    border = st.slider('Border Size', min_value=1, max_value=10, value=4)
    
