import streamlit as st
import qrcode

st.title("========== QR Code Generator ==========")

# Get text or URL
data = st.text_input("Enter text or URL:")

# File name
filename = st.text_input("Enter file name:")

if st.button("Generate QR Code"):

    if data and filename:

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="darkgreen",
            back_color="white"
        )

        # Convert QR image
        img = img.get_image()

        file_path = f"{filename}.png"
        img.save(file_path)

        st.success("✅ QR Code Generated Successfully!")

        st.image(img, caption="Your QR Code")

        with open(file_path, "rb") as file:
            st.download_button(
                label="Download QR Code",
                data=file,
                file_name=file_path,
                mime="image/png"
            )

    else:
        st.warning("Please enter text and file name")