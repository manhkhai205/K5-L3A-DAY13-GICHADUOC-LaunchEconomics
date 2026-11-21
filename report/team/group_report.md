# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: `GICHADUOC`
- Lớp: `L3A`
- Repo: `K5-L3A-DAY13-GICHADUOC-LaunchEconomics`
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng bộ **hồ sơ launch v0 (Gate 2a)** cho trợ lý hoàn phí của LogiX-VN từ dữ liệu chạy thử 2 tuần ở 6 depot (mẫu 1.200 yêu cầu, 1.624 lần chạy giả lập) để trả lời bốn câu hỏi: (1) có đáng chạy không, (2) nhân viên có dùng không, (3) khi hỏng xử lý thế nào, và (4) pilot thiết kế ra sao để tách được tác động và ra quyết định. Nhóm chia 4 vai chuẩn theo `TEAM.md`, chạy song song hai luồng (tính toán/kiểm số và gắn nhãn/giữ hồ sơ) rồi đối chiếu chéo sau mỗi checkpoint.

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí và độ nhạy):** Hoàn thiện `src/lab13.py` qua đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính chi phí mọi lần chạy kể cả lần lỗi ở tử số chia cho số việc `thanh_cong`, tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và phân tích độ nhạy 9 yếu tố, giới hạn chạy lại `k = 1/2/3`, kịch bản xem lại 100% trong [`bang_chi_phi.md`](bang_chi_phi.md) và [`src/lab13.py`](../../src/lab13.py).
- **Nhiệm vụ C (Phân loại lỗi và khắc phục):** Hai thành viên gắn độc lập 20 ca lỗi theo năm loại Google PAIR theo nguyên nhân gốc, đối chiếu tỷ lệ đồng thuận, viết quy tắc phân biệt các ca dễ lẫn và gán cách phát hiện đo được kèm một vai trò phụ trách cho 5 ca đại diện trong [`bang_loi.md`](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính 5 câu cỡ mẫu D1, trả lời 5 câu tách tác động D2, lựa chọn đơn vị chia cụm và thiết lập 3 luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ trong [`pilot_plan.yaml`](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro và hồ sơ launch v0):** Đặc tả 5 chỉ số E1, 11 event có `trace_id`, 3 dòng rủi ro kinh tế E2 trong [`chi_so.md`](chi_so.md) và tổng hợp thành hồ sơ 1 trang 7 mục kèm đề xuất cuối tại [`ho_so_launch_v0.md`](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí thật & phạm vi:** Chi phí mỗi việc thành công đạt **4.472 đ** `[simulated]` (gấp **16,3×** hoá đơn token+tool `274,7 đ/yêu cầu`), trong đó giờ nhân viên chiếm **92,5%** (`51,8%` làm lại, `40,7%` xem lại `[simulated]`). Sau khi cộng cố định 40 triệu đ/tháng, phạm vi pilot **`noi_dia` + `hang_nang`** đạt **4.599 đ = 0,38×** mức `12.000 đ` ở 45.000 yêu cầu/tháng (**5.784 đ = 0,48×** ở nửa khối lượng `[simulated]`). Loại `quoc_te` (**22.515 đ = 1,88×** `[simulated]`, thành công `27,3%`) và `doi_tac` (**10.215 đ = 0,85×** `[simulated]`) bị loại khỏi pilot. Chi phí cả hệ thống (gồm 222 ca nhân viên làm thay) là **5.865 đ/yêu cầu = 0,49×** `[simulated]`.
- **Độ nhạy & mức xem lại:** Yếu tố nhạy nhất là **số ca làm lại** (`+51,8%` / `−25,9%`) và **tỉ lệ xem lại** (`+40,7%` / `−20,3%` `[simulated]`), mạnh hơn nhiều so với giá token (`+5,6%`). Tối ưu tổng chi phí hệ thống nằm ở giới hạn **2 lần chạy** (`6.901.220 đ` `[simulated]`). Nếu phải xem lại 100%, chi phí vọt lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (15,3 phút thực tế trong dữ liệu `[simulated]`).
- **Lỗi & chỉ số chạy thử:** Đồng thuận gắn nhãn đạt **20/20 = 100%**. Chỉ số chạy thử (chưa có đối chứng): đóng ≤ 24h không mở lại 7 ngày **82,83%** (phạm vi pilot **92,26%**), bỏ qua gợi ý **27,12%** (phạm vi **21,09%**), mở lại 7 ngày **4,25%** (phạm vi **3,97%**).
- **Thiết kế pilot & đề xuất cuối:** Chia theo **20 + 20 nhân viên**, chấp nhận **MDE 6 điểm** (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`; power còn **0,64** nếu tác động thật chỉ 5 điểm). Đề xuất cuối: **Go có điều kiện** cho riêng `noi_dia` + `hang_nang` kèm 5 điều kiện kiểm tra (bắt đầu từ `2026-12-01` tới ngày quyết định `2027-01-05`).
- **Kết quả duyệt chéo từ hội đồng Gate 2a:** *(Cập nhật sau phiên duyệt chéo 17:00–17:45; phiếu nhóm mình chấm nhóm khác nằm tại [`phieu_cham.md`](phieu_cham.md)).*

## 5. Khó khăn và cách xử lý

- **Khác biệt môi trường & làm tròn số:** Trên Windows dùng lệnh `python` thay cho `python3`, và kịch bản B4 (15,3 phút làm lại) ra `12.415 đ` so với `12.414 đ` trong hướng dẫn do làm tròn (sai lệch < 0,01%, trong ngưỡng 2%); nhóm đã chạy lại `src/lab13.py` và `yaml.safe_load` kiểm chứng độc lập trên 3 máy khác nhau.
- **Thiếu cỡ mẫu cụm ở mức MDE 5 điểm:** Với 40 nhân viên hiện có, chia 20 + 20 cụm chỉ đạt tối đa `1.000` hiệu dụng/nhóm (`< 1.251`); nhóm giải quyết bằng cách nâng MDE lên 6 điểm (`859/nhóm`, `m ≥ 299`) và ghi thẳng power `0,64` là con số bất lợi kèm điều kiện ký chấp nhận rủi ro trước pilot.
- **Đồng bộ tên event & nhãn `[simulated]` khi làm song song:** Rà soát chéo toàn thư mục `report/team/` trước mốc 17:00, bổ sung event `input_validation_failed` vào `chi_so.md` để khớp bảng khắc phục Ca 9 và gắn bổ sung nhãn `[simulated]` cho mọi số liệu thuộc nhóm suy từ cột `_simulated`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng commit của 4 thành viên xem tại [`TEAM.md`](../../TEAM.md) và 4 báo cáo cá nhân:
- [`2A202603664_NguyenVietManhKhai.md`](2A202603664_NguyenVietManhKhai.md) (Người gắn nhãn 1)
- [`2A202603620_NguyenDinhQuang.md`](2A202603620_NguyenDinhQuang.md) (Người viết code)
- [`2A202603573_VuDucAnh.md`](2A202603573_VuDucAnh.md) (Người kiểm số)
- [`2A202603667_NguyenCanhHieu.md`](2A202603667_NguyenCanhHieu.md) (Người gắn nhãn 2, kiêm giữ hồ sơ)

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện tại dùng dữ liệu `simulated`; bắt buộc bật đủ 11 event có `trace_id` để thay bằng số đo thật (`staff_review_decision`, `staff_rework_completed`) ngay sau tuần 1 pilot.
- Đợt chạy thử 2 tuần chưa có nhóm đối chứng nên chưa thể quy nguyên nhân cho trợ lý; cần hoàn tất pilot 20 + 20 nhân viên có nhóm đối chứng chạy song song.
- Ba chỉ số E1 hiện tính bằng script kiểm chứng riêng ngoài `src/lab13.py`; hai mốc kiểm tra `2026-12-01` là ngày giả định để chốt điều kiện tiền pilot do đề bài không ấn định ngày khởi chạy.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (`arxiv.org/abs/2504.13359`)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure" (`pair.withgoogle.com`)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`)
- Tài liệu nội bộ: [`docs/du_lieu_va_cong_thuc.md`](../../docs/du_lieu_va_cong_thuc.md), [`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
