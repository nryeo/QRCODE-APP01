import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import pyshorteners  # 라이브러리 추가

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

def shorten_url(url):
    """
    Shorten a given URL using pyshorteners.
    :param url: Original long URL
    :return: Shortened URL
    """
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)  # TinyURL로 단축
        return short_url
    except Exception as e:
        st.error(f"Error shortening URL: {e}")
        return None

def is_valid_url(url):
    """
    Validate if the input text is a valid URL.
    :param url: Input text
    :return: Boolean indicating if the URL is valid
    """
    return url.startswith("http://") or url.startswith("https://")

# Streamlit App
st.title("QR Code Generator with URL Shortener")

# Sidebar for customization
st.sidebar.header("Select Functionality")
mode = st.sidebar.radio(
    "Choose what you want to do:",
    ("Generate QR Code", "Shorten URL", "Both"),
)

# Input text from the user
input_text = st.text_input("Enter text or URL:")

if input_text:
    if mode == "Generate QR Code" or mode == "Both":
        qr_data = input_text

        # Generate QR code
        qr_image = generate_qr_code(qr_data)

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

    if mode == "Shorten URL" or mode == "Both":
        if is_valid_url(input_text):
            short_url = shorten_url(input_text)
            if short_url:
                st.success(f"Shortened URL: {short_url}")
        else:
            st.error("Invalid URL. Please enter a valid URL starting with http:// or https://")

# Display note about TinyURL usage
st.sidebar.markdown(
    "*This application uses the TinyURL API via the `pyshorteners` library for URL shortening.*"
)

# Requirements (save as requirements.txt):
# streamlit
# qrcode
# pillow
# pyshorteners
