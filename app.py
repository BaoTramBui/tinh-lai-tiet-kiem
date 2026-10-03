import streamlit as st

st.set_page_config(
    page_title="Tính lãi tiết kiệm",
    page_icon="💰"
)

st.title("💰 Tính lãi gửi tiết kiệm")
st.write("Nhập thông tin để tính tiền lãi dự kiến.")

so_tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10000000.0,
    step=500000.0,
    format="%.0f"
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

tien_lai = so_tien_gui * lai_suat / 100 * ky_han / 12
tong_nhan = so_tien_gui + tien_lai

col1, col2 = st.columns(2)

with col1:
    st.metric("Tiền lãi", f"{tien_lai:,.0f} VNĐ")

with col2:
    st.metric("Tổng nhận", f"{tong_nhan:,.0f} VNĐ")

st.caption(
    "Công thức: Tiền lãi = Tiền gửi × Lãi suất năm × Số tháng / 12"
)
