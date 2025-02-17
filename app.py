import streamlit as st
from PIL import Image
import os
from utils.image_processing import resize_image, IMAGE_SIZES
from utils.twitter_api import post_images_to_twitter

st.title("📷 Image Resizer & Twitter Uploader")
st.write("Upload an image, resize it to multiple sizes, and post it to X (Twitter)!")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Resize Images
    resized_images = []
    for name, size in IMAGE_SIZES.items():
        resized_img = resize_image(image, size)
        img_path = f"temp_{name}.png"
        resized_img.save(img_path)
        resized_images.append(img_path)
        st.image(resized_img, caption=f"Resized: {name}", use_column_width=True)

    # Twitter Posting Button
    if st.button("Post to X (Twitter)"):
        post_images_to_twitter(resized_images)
        st.success("✅ Images posted successfully on X (Twitter)!")

