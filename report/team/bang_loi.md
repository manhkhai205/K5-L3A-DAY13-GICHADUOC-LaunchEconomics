# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Viết Mạnh Khải · Người gắn nhãn 2: Nguyễn Cảnh Hiếu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ... *(Chờ so bộ nhãn độc lập của Người gắn nhãn 2 — Nguyễn Cảnh Hiếu)*

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (nối `trace_id` với `refund_request_created`) theo dõi hằng ngày; cảnh báo khi vượt **2%** tổng yêu cầu/ngày | Nhận diện định dạng mã sàn TMĐT để tự tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn thay vì dừng đột ngột | PM trợ lý hoàn phí |
| 20 | Hệ thống | Event `refund_ledger_write` kiểm tra theo thời gian thực và đối soát hằng ngày theo `idempotency_key` (`request_id`); ngưỡng cảnh báo **≥ 1 ca hoàn trùng** (kích hoạt luật dừng an toàn trong `pilot_plan.yaml`) | Bắt buộc khoá chống trùng `idempotency_key` theo `request_id` ở tầng sổ cái, chặn tạo lệnh thứ hai khi yêu cầu đang xử lý và trả thông báo chờ cho khách | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` (`reopened_within_7d = true`, `reason = khieu_nai_so_tien`) đối chiếu hằng tuần với `audit_sample_checked` (`lech_tien = 0`); cảnh báo khi vượt **1%** số đơn mở lại/tuần | Chuẩn hoá mẫu tin nhắn hoàn phí luôn hiển thị rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) kèm điều khoản chính sách áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason = thieu_du_lieu`, gắn `loai` từ `refund_request_created`) tổng hợp hằng tuần; cảnh báo khi vượt **5%** tổng yêu cầu/tuần trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt qua `handoff_to_staff` và loại nhóm `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`) ra khỏi phạm vi pilot (chỉ giữ `noi_dia` + `hang_nang`) | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo khi tỉ lệ đơn lệch tiền (`lech_tien != 0`) vượt **1%** mẫu kiểm tra/tuần | Tự động xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào `agent_run_completed` (`trace_id`) để đối soát | Kế toán trưởng |
