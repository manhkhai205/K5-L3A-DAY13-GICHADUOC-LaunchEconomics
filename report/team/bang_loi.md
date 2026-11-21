# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Viết Mạnh Khải · Người gắn nhãn 2: Nguyễn Cảnh Hiếu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng 80%, không phải viết lại định nghĩa)

Phân bố nhãn thống nhất: Do người dùng 4 ca (1, 6, 9, 14) · Hệ thống 5 ca (2, 7, 8, 15, 20) · Ngữ cảnh 4 ca (3, 10, 16, 18) · Giới hạn hệ thống 4 ca (4, 11, 13, 19) · Ngầm 3 ca (5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Không có ca nào không trùng (20/20). Người gắn nhãn 2 đã đánh dấu 6 ca phân vân khi gắn độc lập. Nhóm ghi quy tắc phân biệt cho 6 ca này để người vận hành sau này gắn nhãn nhất quán:

- **Ca 6, 9 · Do người dùng, không phải Hệ thống:** nguyên nhân gốc là khách chọn sai mục hoặc nhập sai loại mã. Việc trợ lý không gợi ý là chỗ cần sửa, ghi ở cột khắc phục, không đổi nhãn.
- **Ca 8 · Hệ thống, không phải Ngầm:** trợ lý dẫn một điều khoản không có thật, trái thiết kế. Trích dẫn hiện ra cho khách nên sai đã lộ ra. Số tiền đúng không xoá được lỗi.
- **Ca 13 · Giới hạn hệ thống, không phải Hệ thống:** câu hỏi nằm ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời mập mờ). Cách trả lời là chỗ cần sửa.
- **Ca 18 · Ngữ cảnh, không phải Hệ thống:** số tiền đúng chính sách. Chỉ có giả định "khách hiểu cách tính" là không khớp với khách.
- **Ca 20 · Hệ thống, không phải Do người dùng:** khách gửi lại sau 10 phút là hành vi hợp lý, không phải đầu vào sai. Nguyên nhân gốc là thiếu khoá chống trùng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (nối `trace_id` với `refund_request_created`) theo dõi hằng ngày; cảnh báo khi vượt **2%** tổng yêu cầu/ngày | Nhận diện định dạng mã sàn TMĐT để tự tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn thay vì dừng đột ngột | PM trợ lý hoàn phí |
| 20 | Hệ thống | Event `refund_ledger_write` kiểm tra theo thời gian thực và đối soát hằng ngày theo `idempotency_key` (`request_id`); ngưỡng cảnh báo **≥ 1 ca hoàn trùng** (kích hoạt luật dừng an toàn trong `pilot_plan.yaml`) | Bắt buộc khoá chống trùng `idempotency_key` theo `request_id` ở tầng sổ cái, chặn tạo lệnh thứ hai khi yêu cầu đang xử lý và trả thông báo chờ cho khách | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` (`reopened_within_7d = true`, `reason = khieu_nai_so_tien`) đối chiếu hằng tuần với `audit_sample_checked` (`lech_tien = 0`); cảnh báo khi vượt **1%** số đơn mở lại/tuần | Chuẩn hoá mẫu tin nhắn hoàn phí luôn hiển thị rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) kèm điều khoản chính sách áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason = thieu_du_lieu`, gắn `loai` từ `refund_request_created`) tổng hợp hằng tuần; cảnh báo khi vượt **5%** tổng yêu cầu/tuần trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt qua `handoff_to_staff` và loại nhóm `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`) ra khỏi phạm vi pilot (chỉ giữ `noi_dia` + `hang_nang`) | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo khi tỉ lệ đơn lệch tiền (`lech_tien != 0`) vượt **1%** mẫu kiểm tra/tuần | Tự động xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào `agent_run_completed` (`trace_id`) để đối soát | Kế toán trưởng |
