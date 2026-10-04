import streamlit as st
st.image("logo.jgp.JPG")
st.set_page_config(page_title="Tính lãi gửi tiết kiệm", page_icon="📋")

st.title("📋 Thông tin khoản tiền gửi")

# 1. Nhập liệu từ người dùng
so_tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0,
    value=10000000,
    step=1000000,
    format="%d"
)

ky_han = st.number_input(
    "Kỳ hạn gửi (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=5.00,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
)

phuong_phap = st.radio(
    "Phương pháp tính lãi",
    ["Lãi đơn", "Lãi kép"],
    horizontal=True
)

st.caption(
    "Lãi suất được tính theo năm. Với lãi kép, tiền lãi được nhập vào gốc "
    "theo chu kỳ đã chọn. Vì vậy, hàng tháng và hàng quý là chu kỳ tính "
    "lãi/tái đầu tư trong mô hình này."
)

# 2. Xử lý tính toán khi nhấn nút
if st.button("🧧 TÍNH TIỀN LÃI", use_container_width=True):
    r = lai_suat / 100  # Chuyển % sang số thập phân
    
    if phuong_phap == "Lãi đơn":
        # Công thức lãi đơn
        tien_lai = so_tien_gui * r * (ky_han / 12)
        tong_nhan = so_tien_gui + tien_lai
    else:
        # Công thức lãi kép
        # Tùy thuộc vào hình thức nhận lãi/ghép gốc
        if hinh_thuc == "Hàng tháng":
            m = 12  # 12 lần/năm
        elif hinh_thuc == "Hàng quý":
            m = 4   # 4 lần/năm
        else:
            # Nếu chọn Cuối kỳ với Lãi kép, mặc định ghép lãi theo tháng
            m = 12  
        
        # Số thời gian tính theo năm
        t = ky_han / 12
        tong_nhan = so_tien_gui * ((1 + r / m) ** (m * t))
        tien_lai = tong_nhan - so_tien_gui

    st.divider()
    
    # 3. Hiển thị kết quả
    st.subheader("Tiền lãi")
    st.markdown(f"### **{tien_lai:,.0f} VNĐ**".replace(",", "."))
    
    st.subheader("Tổng nhận")
    st.markdown(f"### **{tong_nhan:,.0f} VNĐ**".replace(",", "."))
