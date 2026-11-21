# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ... · Lớp: ...

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc** [simulated] = 4.373.585 đ ÷ 978 việc thành công, gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí: làm lại 51,8%, xem lại 40,7% [simulated]. Chưa cộng chi phí cố định | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Số ca làm lại** (gấp đôi → **+51,8%**, 6.787 đ; giảm một nửa → −25,9%) · **2. Tỉ lệ xem lại** (gấp đôi → **+40,7%**, 6.292 đ; giảm một nửa → −20,3%) · **3. Lương nhân viên** (+25% → **+23,1%**, 5.506 đ) [simulated]. Giá token gấp đôi chỉ +5,6%. Mô hình cộng tuyến tính: token và xem lại cùng gấp đôi → +46,3% [simulated]. Vì vậy pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không phải giá token | Giả lập | Trưởng nhóm CSKH |
| 3 · So với nhân viên tự làm | Phạm vi pilot `noi_dia` + `hang_nang`: **4.599 đ = 0,38×** của 12.000 đ, đã cộng cố định 40 tr/tháng ở 45.000 yêu cầu/tháng; **0,48×** nếu khối lượng còn một nửa [simulated]. Cả hệ thống, mọi loại, tính cả 222 ca nhân viên làm thay: 5.865 đ/yêu cầu = 0,49× [simulated]. Thu hẹp phạm vi vì `quoc_te` 1,88× (thành công 27,3%; lần chạy 2 và 3 chỉ đúng 11,4% và 2,2%) và `doi_tac` 0,85× (sát ngưỡng, có điều khoản riêng); `noi_dia` 0,22×, `hang_nang` 0,69× [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (1.200 yêu cầu, chưa có nhóm đối chứng nên chưa quy được cho trợ lý): **chính** (đóng trong 24 giờ và không mở lại trong 7 ngày) **82,83%** (994/1.200) · **dùng** (tỉ lệ bỏ qua gợi ý: sửa + bỏ / số được xem lại) **27,12%** (48/177) · **an toàn** (mở lại trong 7 ngày) **4,25%** (51/1.200). Riêng phạm vi `noi_dia` + `hang_nang`: 92,26% · 21,09% · 3,97% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | ... | ... | ... |
| 6 · Pilot plan | ... | ... | ... |
| 7 · Rủi ro kinh tế | 3 rủi ro, chi tiết trong `chi_so.md` (E2): **(1) Xem lại 100% kéo dài:** 11.743 đ = **0,98×**, hoặc 12.415 đ = **1,03×** nếu làm lại 15,3 phút như dữ liệu; chỉ hoà vốn khi mỗi lần xem lại ≤ 4,8–5,1 phút [simulated]. Theo dõi: % được xem lại > 50% cuối bước 0.25 · **(2) Số ca làm lại tăng gấp đôi:** +51,8%, lên 6.787 đ [simulated]. Theo dõi: tỉ lệ làm lại theo tuần > 7% (chạy thử 4,89%) · **(3) Khối lượng còn một nửa:** cố định tăng từ +1.185 lên +2.370 đ/việc, 0,38× → 0,48× [simulated]. Theo dõi: việc thành công/tuần < 4.219 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
