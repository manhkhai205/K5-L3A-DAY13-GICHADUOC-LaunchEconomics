# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200 toàn mẫu) · **92,26%** (906/982 phạm vi `noi_dia` + `hang_nang`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177 toàn mẫu) · **21,09%** (27/128 phạm vi `noi_dia` + `hang_nang`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200 toàn mẫu) · **3,97%** (39/982 phạm vi `noi_dia` + `hang_nang`) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu nhóm can thiệp mở gợi ý trợ lý | Số yêu cầu có `agent_suggestion_shown` chia tổng `refund_request_created` thuộc nhóm trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền hoặc hoàn trùng | Số ca lệch tiền ở `audit_sample_checked` hoặc trùng `idempotency_key` ở `refund_ledger_write` chia số đơn kiểm tra/tuần | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (toàn mẫu) và 92,26% (phạm vi pilot), không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id, loai, so_tien_vnd, arm, depot, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy, kể cả lần `loi` |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id, phut_lam_lai, ly_do, trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien_hoan, ket_qua, trace_id` | Khi ghi nhận giao dịch hoàn phí vào sổ cái |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi vượt số lần chạy tối đa hoặc ngoài phạm vi và chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, closed_within_24h, trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách / CSKH | `reopened_at, reopened_within_7d, reason, trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán / QA | `so_tien_da_hoan, so_tien_dung, lech_tien, trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn |
| `input_validation_failed` | Cổng CSKH / Agent | `request_id, field, raw_value_type, trace_id` | Khi khách nhập sai định dạng đầu vào (mã đơn sàn TMĐT, thiếu số tài khoản) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`82,83%` chạy thử):** nối `refund_request_created` + `ticket_closed` (đóng ≤ 24h) + `ticket_reopened` (không mở lại ≤ 7 ngày) qua `trace_id`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý (`27,12%` chạy thử):** tính từ `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo`) chia tổng `staff_review_decision` (hoặc đối chiếu với `agent_suggestion_shown`).
- **Chỉ số dùng (tự đề xuất) — Tỉ lệ mở gợi ý:** tính từ `agent_suggestion_shown` chia `refund_request_created` (`arm = treatment`).
- **Chỉ số an toàn — Lỗi lọt đến khách (`4,25%` chạy thử):** tính từ `ticket_reopened` (`reopened_within_7d = true`) chia `refund_request_created`.
- **Chỉ số an toàn (tự đề xuất) — Sai tiền / hoàn trùng:** tính từ `audit_sample_checked` và `refund_ledger_write` (`idempotency_key`).
- **Chi phí thật trong pilot (thay số `simulated`):** nối `agent_run_completed` (token + tool mọi lần chạy) + `staff_review_decision` (`phut_xem_lai` thật) + `staff_rework_completed` (`phut_lam_lai` thật) + `handoff_to_staff` qua `trace_id`; chỉ số nào chưa bật đủ `phut_xem_lai`/`phut_lam_lai` thật thì vẫn là `simulated`, chưa đo được trực tiếp.
- **Phát hiện lỗi đầu vào người dùng (`bang_loi.md`, ca 9):** tính từ `input_validation_failed` chia tổng `refund_request_created` theo ngày qua `trace_id` (cảnh báo khi vượt 2%/ngày).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ `4.472 đ` lên **`6.787 đ`** (`simulated`) | Tỉ lệ ca `lam_lai` theo tuần > **7%** (mức chạy thử trong phạm vi là **4,89%**, 48/982 ca) | Thu hẹp pilot về riêng `noi_dia`, giới hạn 2 lần chạy, rà 20 trace `lam_lai` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài suốt pilot | Chi phí lên **`11.743 đ` = 0,98×** (9 phút làm lại) hoặc **`12.415 đ` = 1,03×** (15,3 phút thực tế), hoà vốn xem lại ≤ **4,8–5,1 phút** (`simulated`) | Tỉ lệ ca `duoc_xem_lai` > **50%** vào cuối bước `0.25` hoặc thời gian xem lại bình quân > **4,8 phút/ca** | Giảm xem lại theo bậc theo điểm tin cậy khi tỉ lệ `sua + bo` < **15%** | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng gấp đôi từ **`+1.185 đ/việc`** (45.000 yc/tháng → `4.599 đ = 0,38×`) lên **`+2.370 đ/việc`** khi giảm nửa khối lượng (`5.784 đ = 0,48×`, `simulated`) | Số việc thành công mỗi tuần < **50%** kế hoạch (< `4.219` việc/tuần trong phạm vi pilot) | Dừng mở rộng quy mô pilot, đàm phán lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
