import streamlit as st
import numpy as np
import cv2
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import io

st.set_page_config(page_title="Image Processing Suite", layout="wide")

st.title("🖼️ Image Processing using K-Means")

# =========================
# Sidebar
# =========================
option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Image Compression",
        "Image Segmentation",
        "Segmentation + Boundaries",
        "Segmentation + Edge Detection"
    ]
)

k = st.sidebar.slider("Number of Clusters (K)", 2, 20, 8)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# =========================
# Helper Functions
# =========================

def load_image(file):
    img = Image.open(file)
    img = img.resize((256, 256))  # fixed for performance
    return np.array(img)

def apply_kmeans(image, k, add_xy=False):
    h, w, c = image.shape
    pixels = image.reshape(-1, 3).astype(np.float32) / 255.0

    if add_xy:
        x = np.tile(np.arange(w), (h, 1)) / w
        y = np.tile(np.arange(h), (w, 1)).T / h
        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)
        features = np.concatenate([pixels, x, y], axis=1)
    else:
        features = pixels

    kmeans = MiniBatchKMeans(n_clusters=k, random_state=42, batch_size=1000)
    labels = kmeans.fit_predict(features)

    return labels, kmeans, h, w

# ⭐ Estimate file size based on K
def estimate_size(image_np, k):
    img = Image.fromarray(image_np)
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=90)
    size_kb = buffer.tell() / 1024

    # heuristic: fewer clusters → smaller size
    estimated = size_kb * (k / 20)
    return round(estimated / 1024, 2)  # MB

# =========================
# Main
# =========================

if uploaded_file:
    image = load_image(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Original Image", use_container_width=True)

    labels, kmeans, h, w = apply_kmeans(
        image,
        k,
        add_xy=("Segmentation" in option)
    )

    result_image = None

    # =========================
    # Compression
    # =========================
    if option == "Image Compression":
        compressed = kmeans.cluster_centers_[labels]
        compressed = np.clip(compressed * 255, 0, 255).astype("uint8")
        compressed = compressed.reshape(h, w, 3)

        result_image = compressed

        with col2:
            st.image(compressed, caption=f"Compressed (K={k})", use_container_width=True)

    # =========================
    # Segmentation
    # =========================
    elif option == "Image Segmentation":
        segmented = kmeans.cluster_centers_[labels][:, :3]
        segmented = (segmented.reshape(h, w, 3) * 255).astype("uint8")

        result_image = segmented

        with col2:
            st.image(segmented, caption=f"Segmented (K={k})", use_container_width=True)

    # =========================
    # Boundaries
    # =========================
    elif option == "Segmentation + Boundaries":
        labels_img = labels.reshape(h, w)

        boundaries = np.zeros((h, w), dtype=np.uint8)
        boundaries[:-1, :] |= (labels_img[:-1, :] != labels_img[1:, :])
        boundaries[:, :-1] |= (labels_img[:, :-1] != labels_img[:, 1:])

        boundary_img = image.copy()
        boundary_img[boundaries == 1] = [255, 0, 0]

        result_image = boundary_img

        with col2:
            st.image(boundary_img, caption="Boundaries", use_container_width=True)

    # =========================
    # Edge Detection
    # =========================
    elif option == "Segmentation + Edge Detection":
        segmented = kmeans.cluster_centers_[labels][:, :3]
        segmented = (segmented.reshape(h, w, 3) * 255).astype("uint8")

        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(gray, 100, 200)

        seg_edges = segmented.copy()
        seg_edges[edges != 0] = [0, 255, 0]

        result_image = seg_edges

        with col2:
            st.image(seg_edges, caption="Edges + Segmentation", use_container_width=True)

    # =========================
    # Show Estimated Size
    # =========================
    if result_image is not None:
        estimated_mb = estimate_size(result_image, k)
        st.info(f"📦 Estimated file size: ~{estimated_mb} MB (based on K={k})")

        # Convert to downloadable JPEG
        img_pil = Image.fromarray(result_image)
        buffer = io.BytesIO()
        img_pil.save(buffer, format="JPEG", quality=90)

        st.download_button(
            label="⬇ Download Image",
            data=buffer.getvalue(),
            file_name="processed.jpg",
            mime="image/jpeg"
        )

else:
    st.info("Upload an image to start 🚀")