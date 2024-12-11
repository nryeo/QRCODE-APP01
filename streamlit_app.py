import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit App
st.title("QR Code Generator")

# Input text from the user
input_text = st.text_input("Enter text to generate QR code:")

if input_text:
    # Generate QR code
    qr_image = generate_qr_code(input_text)

    # Display the QR code
    st.image(qr_image, caption="Generated QR Code", use_column_width=True)

    # Provide download option
    buffered = BytesIO()
    qr_image.save(buffered, format="PNG")
    buffered.seek(0)

    st.download_button(
        label="Download QR Code",
        data=buffered,
        file_name="qr_code.png",
        mime="image/png",
    )
