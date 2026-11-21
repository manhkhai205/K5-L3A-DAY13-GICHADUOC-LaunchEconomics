# Báo cáo cá nhân — NguyenDinhQuang-2A202603620

## 1. Thông tin thành viên
- Họ tên: Nguyễn Đình Quang
- MSSV: 2A202603620
- Email: quang8b9b@gmail.com
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách
- Viết và chạy `src/lab13.py`, file tính toàn bộ số liệu cho hồ sơ launch v0.
- CP1 · A1–A4: ba hàm xác suất, mô hình chi phí mỗi việc thành công (CPS), tách theo loại, chi phí cố định.
- CP2 · B1–B4: bảng độ nhạy, đổi hai yếu tố cùng lúc, giới hạn số lần chạy, kịch bản xem lại 100%.
- CP4 · D1: cỡ mẫu pilot, design effect, power.
- Cài môi trường Python (`.venv`, `requirements.txt`) và chuyển số cho các thành viên viết `bang_chi_phi.md` và `pilot_plan.yaml`.

## 3. Đóng góp cụ thể
- **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`. Qua cả ba phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
- **A2:** viết `mo_hinh(...)`. Tử số gồm token, tool, xem lại, làm lại của **mọi** lần chạy, kể cả lần lỗi; mẫu số chỉ đếm yêu cầu `thanh_cong`. Có tham số giá, lương, hệ số xem lại/làm lại và `max_lan_chay` để dùng lại cho phần B.
- **A3:** tách CPS theo 4 loại và pivot tỉ lệ ok theo `attempt` × `loai`, để kiểm tra chạy lại có giúp không.
- **A4:** thêm hàm `chi_phi_co_dinh` (40 triệu đ/tháng, phạm vi noi_dia + hang_nang), tính ở toàn quy mô và ở nửa lưu lượng.
- **B:** vòng lặp 9 kịch bản độ nhạy, kịch bản 2 yếu tố, chi phí hệ thống theo giới hạn chạy k = 1/2/3, kịch bản xem lại 100% và điểm hoà vốn.
- **D1:** viết `co_mau(p1, p2)` theo công thức hai tỉ lệ, tính design effect và số hiệu dụng cho 5 phương án chia nhóm, tính power bằng `statsmodels`.
- Sửa theo góp ý của người kiểm số: đổi dòng in A1 cho khớp checklist, bổ sung phần in A4.

## 4. Bằng chứng
- File: `src/lab13.py`. Commit: <!-- dán link/hash commit -->
- Số chính do code in ra, khớp với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`:

| Mục | Kết quả | Nhãn |
|---|---|---|
| A2 · Tổng chi phí mẫu | 4.373.585 đ | có simulated |
| A2 · Việc thành công | 978 | |
| A2 · CPS | 4.472 đ (0,37× so với 12.000 đ) | simulated |
| A3 · CPS quoc_te | 22.515 đ = 1,88× | simulated |
| A3 · CPS noi_dia | 2.696 đ = 0,22× | simulated |
| A4 · CPS có chi phí cố định, toàn quy mô | 4.599 đ = 0,38× | simulated |
| A4 · CPS có chi phí cố định, nửa lưu lượng | 5.784 đ = 0,48× | simulated |
| B1 · Làm lại ×2 / Xem lại ×2 / Token ×2 | +51,8% / +40,7% / +5,6% | simulated |
| B3 · Chi phí hệ thống thấp nhất | k = 2: 6.901.220 đ | simulated |
| B4 · Xem lại 100% | 11.743 đ = 0,98× (làm lại 9 phút) | simulated |
| D1 · Cỡ mẫu mỗi nhóm | 1.251 | |
| D1 · Power ở mức 5 điểm, n = 859 | 0,64 | |

## 5. Công cụ AI đã dùng
- **Claude:** dùng để giải thích nhiệm vụ của vai người viết code, gợi ý code cho các hàm trong `lab13.py` dựa trên công thức trong `docs/du_lieu_va_cong_thuc.md`, sửa lỗi cài môi trường trên Windows (`python3` không có, phải dùng `python`).
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` trên máy, xác nhận ba phép thử A1 đạt.
  - So từng số A2, A3, A4, B1–B4, D1 với bảng đối chiếu trong hướng dẫn. Tất cả khớp; chỉ B4 (làm lại 15,3 phút) ra 12.415 đ so với 12.414 đ, lệch 1 đ do làm tròn, nằm trong sai số 2%.
  - Tự kiểm tra tính tuyến tính: kịch bản giảm một nửa cho mức thay đổi bằng nửa kịch bản gấp đôi (5,6% → 2,8%; 40,7% → 20,3%).

## 6. Tự đánh giá
- Hoàn thành đủ phần code cho CP1, CP2, CP4. Mọi số khớp đáp án trong sai số 2% và có nhãn simulated đúng quy tắc.
- Hiểu được kết luận chính rút ra từ số: CPS chung 4.472 đ rẻ hơn người làm (0,37×), nhưng quoc_te đắt hơn (1,88×) nên cần loại khỏi phạm vi pilot; làm lại và xem lại là hai yếu tố chi phí lớn nhất.
- Cần cải thiện: phụ thuộc nhiều vào AI khi viết code ban đầu. Lần sau mình sẽ tự viết hàm trước rồi mới dùng AI để rà lỗi. Cũng nên đọc kỹ CHECKPOINTS.md từ đầu để khỏi phải sửa định dạng in ra.