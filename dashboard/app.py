import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from core.stats import get_dataset_stats
from core.stats import total_image_count
from core.stats import total_classes
from core.qa_checks import validate_dataset
from core.qa_checks import detect_missing_labels
from core.health_score import calculate_health_score
from core.health_score import get_health_status
from core.health_score import get_health_status
from utils.constants import BONE_PATH, CHEST_XRAY_PATH, SKIN_PATH, VERIFIED_PATH
from visualization.charts import chart_data
from visualization.charts import visualize_data
from visualization.image_preview import get_verified_images

#streamlit run dashboard/app.py


# Date and time
st.caption(f"Last updated: {datetime.now().strftime("%d, %b, %Y, %I:%M %p")}")

# Title
st.title("Medical Dataset QA Dashboard")
st.write("Healthcare dataset validation and annotation quality inspection tool")


# KPI Data
corrupted_files = len(validate_dataset())
missing_labels = len(detect_missing_labels())
health_score = calculate_health_score()
issues = corrupted_files + missing_labels

with st.container(border=True):
    kpi_data = {
    "Health": f"{health_score}%",
    "Total images": total_image_count(),
    "Total classes": total_classes(),
    "Issues": issues
}

    kpi_cols = st.columns(len(kpi_data))

    for i, (label, value) in enumerate(kpi_data.items()):
        kpi_cols[i].metric(
            label=label,
            value=value
            )


# Data statistics 
with st.container(border=True):
    # Class-wise count
    status = get_dataset_stats()
    st.subheader("📊 Dataset Statistics")
    columns = st.columns(len(status))
    for i, (class_name, count) in enumerate(status.items()):
        columns[i].metric(
            label=class_name.capitalize(),
            value=count
        )

        


# Validate dataset
Validation_summary ={
    "Corrupted Files" : len(validate_dataset()),
    "Missing Labels": len(detect_missing_labels())
}
with st.container(border=True):
    st.subheader("🔍 Dataset Validation")
    validates = st.columns(len(Validation_summary))
    for i, (label, value) in enumerate(Validation_summary.items()):
        validates[i].metric(
            label=label,
            value=value
            )



# # emtry .txt file   [--- IGNORE ---]
# empty_files = read_text_files()
# st.subheader("Empty text files")
# st.write(f"Empty text files: {len(empty_files)}")
# for file in empty_files:
#     st.write(file)


# Health score
score = calculate_health_score()
status = get_health_status(score)

Health_data = {
    "Health Score": score,
    "Health Status": status
}

with st.container(border=True):
    st.subheader("❤️ Dataset Health Score ")

    Health = st.columns(len(Health_data))
    for i,(label, value) in enumerate(Health_data.items()):
        Health[i].metric(
            label=label,
            value=value
            )         


#data visualization
st.subheader("📈 Class Distribution Analysis")

data_keys, data_values = chart_data()
fig = visualize_data(data_keys, data_values)
st.pyplot(fig)

st.divider()



# Data Preview
st.header("🖼️ Data Preview")

#Chest priview
verified_images = get_verified_images(CHEST_XRAY_PATH)
st.subheader("Chest X-ray Annotations")

if verified_images:
    cols = st.columns(3)

    for col, image in zip(cols, verified_images):
        with col:
            st.image(image, width="stretch")
else:
    st.info("No preview images available.")

st.divider()

#Bone priview
verified_images = get_verified_images(BONE_PATH)
st.subheader("Bone X-ray Annotations")

if verified_images:
    cols = st.columns(3)

    for col, image in zip(cols, verified_images):
        with col:
            st.image(image, width="stretch")
else:
    st.info("No preview images available.")

st.divider()

#Skin priview
verified_images = get_verified_images(SKIN_PATH)
st.subheader("Skin Lesion Annotations")

if verified_images:
    cols = st.columns(3)

    for col, image in zip(cols, verified_images):
        with col:
            st.image(image, width="stretch")
else:
    st.info("No preview images available.")