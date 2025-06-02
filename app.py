import streamlit as st
import cv2
import numpy as np
from utils.rotate import rotate_image
from utils.crop import crop_image
from utils.annotate import annotate_image
from utils.resize import resize_image_by_scale

# ------------------------- PAGE SETUP -------------------------
st.set_page_config(page_title="Image Editor", page_icon="🖼️", layout="wide")

# ------------------------- SIDEBAR ----------------------------
st.sidebar.title("⚙️ Image Editor Controls")
operation = st.sidebar.selectbox("Choose Operation", ["Crop", "Rotate", "Annotate", "Resize"])
uploaded_file = st.sidebar.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

# ------------------------- MAIN TITLE -------------------------
st.markdown("<h1 style='font-size: 2.5rem;'>🖌️ Image Editor</h1>", unsafe_allow_html=True)

# ------------------------ IMAGE PROCESSING --------------------
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR", caption="📷 Original Image", use_container_width=True)
    st.divider()

    if operation == "Rotate":
        st.subheader("🔁 Rotate Image")
        angle = st.slider("Rotation Angle", -180, 180, 0)
        rotated = rotate_image(image, angle)
        st.image(rotated, channels="BGR", caption="🔄 Rotated Image", use_container_width=True)
        result = cv2.imencode('.png', rotated)[1].tobytes()
        st.download_button("⬇️ Download Rotated Image", result, "rotated.png", "image/png")

    elif operation == "Crop":
        st.subheader("✂️ Crop Image")
        col1, col2 = st.columns(2)
        with col1:
            x = st.number_input("X (start)", 0, image.shape[1], step=1)
            w = st.number_input("Width", 1, image.shape[1] - int(x), step=1)
        with col2:
            y = st.number_input("Y (start)", 0, image.shape[0], step=1)
            h = st.number_input("Height", 1, image.shape[0] - int(y), step=1)

        cropped = crop_image(image, x, y, w, h)
        st.image(cropped, channels="BGR", caption="📐 Cropped Image", use_container_width=True)
        result = cv2.imencode('.png', cropped)[1].tobytes()
        st.download_button("⬇️ Download Cropped Image", result, "cropped.png", "image/png")

    elif operation == "Annotate":
        st.subheader("📝 Annotate Image")
        text = st.text_input("Enter Annotation Text")
        st.markdown("🎨 **Choose Text Color**")
        r = st.slider("Red", 0, 255, 0)
        g = st.slider("Green", 0, 255, 255)
        b = st.slider("Blue", 0, 255, 0)
        color = (b, g, r)

        st.markdown("📍 **Text Position**")
        pos_x = st.slider("X Position", 0, image.shape[1])
        pos_y = st.slider("Y Position", 0, image.shape[0])

        annotated = annotate_image(image, text, (pos_x, pos_y), color=color)
        st.image(annotated, channels="BGR", caption="🖊️ Annotated Image", use_container_width=True)
        result = cv2.imencode('.png', annotated)[1].tobytes()
        st.download_button("⬇️ Download Annotated Image", result, "annotated.png", "image/png")

    elif operation == "Resize":
        st.subheader("📏 Resize Image")
        scale = st.slider("Scale (%)", value=50, min_value=0, max_value=100, step=10)
        resized = resize_image_by_scale(image, scale)
        st.image(resized, channels="BGR", caption=f"📐 Resized Image ({scale}%)")
        result = cv2.imencode('.png', resized)[1].tobytes()
        st.download_button("⬇️ Download Resized Image", result, "resized.png", "image/png")

else:
    st.warning("⚠️ Please upload an image from the sidebar to begin.")
