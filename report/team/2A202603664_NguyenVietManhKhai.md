# Báo cáo cá nhân — NguyenVietManhKhai-2A202603664

## 1. Thông tin thành viên

- Họ tên: Nguyễn Viết Mạnh Khải
- MSSV: `2A202603664`
- Email: `manhkhai205@gmail.com`
- Vai trong nhóm: **Người gắn nhãn 1** (kiêm khởi tạo và quản trị repo nhóm `manhkhai205`)

## 2. Phần việc phụ trách

- Khởi tạo và quản trị repo nhóm `K5-L3A-DAY13-GICHADUOC-LaunchEconomics`, điền thông tin thành viên ban đầu trong `TEAM.md`.
- **Người gắn nhãn 1 (CP3):** gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, so nhãn với Người gắn nhãn 2 (Nguyễn Cảnh Hiếu) và xây dựng bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`.
- **Theo dõi điều kiện "Xong khi" và kiểm tra đồng bộ toàn bộ hồ sơ:** rà soát các commit và 5 file hồ sơ (`bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`) theo `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`; tổng hợp `TEAM.md` và soạn nháp `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Khởi tạo repo nhóm và điền bảng thành viên ban đầu trong `TEAM.md` (commit `2a926ce`).
- Hoàn thiện bộ nhãn Người gắn nhãn 1 (20/20 ca theo nguyên nhân gốc: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3) và bảng khắc phục 5 ca đại diện (**Ca 9, 20, 18, 4, 17** — có đủ event, ngưỡng, tần suất và 1 vai trò phụ trách) trong `report/team/bang_loi.md` (commit `eefdf92`); đạt đồng thuận **20/20 = 100%** khi so với Người gắn nhãn 2 (commit `623da98`).
- Kiểm tra chéo 2 commit hoàn thiện của Hiếu (`623da98`, `68a9a6d`) và toàn bộ `report/team/`: phát hiện và sửa 2 lỗi đồng bộ — bổ sung event `input_validation_failed` vào `report/team/chi_so.md` (thành 11 event) và cập nhật Điều kiện #3 trong `report/team/ho_so_launch_v0.md`; bổ sung nhãn `[simulated]` cho `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`) trong `ho_so_launch_v0.md` và `pilot_plan.yaml`.
- Tổng hợp đầy đủ đóng góp trong `TEAM.md` và soạn nháp `report/team/group_report.md` trước mốc duyệt chéo 17:00.

## 4. Bằng chứng

- **Commit đã đẩy:**
  - `2a926ce`: `info team` (tạo repo và điền danh sách thành viên trong `TEAM.md`).
  - `eefdf92`: `CP3: gắn nhãn độc lập 20 ca lỗi (Người gắn nhãn 1) và nháp bảng khắc phục 5 ca` (`report/team/bang_loi.md`).
- **Chỉnh sửa đồng bộ và hoàn thiện cuối:** `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`, `TEAM.md`, `report/team/group_report.md`, `report/team/2A202603664_NguyenVietManhKhai.md`.
- **Phân bố 20 ca lỗi đã gắn và đối chiếu 100% với Người gắn nhãn 2:** Do người dùng 4 ca (`1, 6, 9, 14`) · Hệ thống 5 ca (`2, 7, 8, 15, 20`) · Ngữ cảnh 4 ca (`3, 10, 16, 18`) · Giới hạn hệ thống 4 ca (`4, 11, 13, 19`) · Ngầm 3 ca (`5, 12, 17`).

## 5. Công cụ AI đã dùng

- **Antigravity (trong IDE):** dùng để tóm tắt đề bài và phân công công việc 4 người theo checkpoint; trích nguyên văn 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`; hỗ trợ phân tích nguyên nhân gốc 20 ca lỗi Google PAIR và soạn bảng khắc phục 5 ca khớp với tên event của nhóm; rà soát 2 commit của Người gắn nhãn 2, phát hiện 2 lỗi đồng bộ và quét kiểm tra quy tắc nộp bài; soạn nháp `report/team/group_report.md`, cập nhật `TEAM.md` và báo cáo cá nhân.
- **Cách tự kiểm tra:**
  - Đọc lại lý do nguyên nhân gốc từng ca (đặc biệt các ca dễ lẫn `6, 8, 9, 12, 13, 15, 18, 20`) để tự bảo vệ được trước hội đồng.
  - Giữ nguyên cột `Nhãn người 2` để trống `...` ở commit `eefdf92`, không tự điền hay bịa kết quả cho tới khi Hiếu tự gắn độc lập và push riêng ở commit `623da98`.
  - Quét toàn bộ `report/team/` và `TEAM.md` để bảo đảm không có từ bị cấm, không còn dấu `?` ngoài chú thích YAML, không còn `...` chưa điền và gắn đủ nhãn `simulated`.
  - Kiểm tra lại `git diff` từng file trước khi commit và push.

## 6. Tự đánh giá

- Hoàn thành vai Người gắn nhãn 1 và nhiệm vụ theo dõi điều kiện "Xong khi" trước mốc 17:00, bảo đảm 5 file hồ sơ khớp số liệu, tên event và nhãn `simulated`.
- **Hạn chế:**
  - Chưa tạo `.venv` để chạy `src/lab13.py` trực tiếp trên máy cá nhân (đã có Quang, Đức Anh và Hiếu chạy kiểm chứng thành công trên 3 máy khác).
  - Có dùng AI hỗ trợ phân tích nhãn và soạn thảo câu chữ nên cần tự ôn kỹ lập luận các ca khó và 3 câu hỏi bắt buộc trong `RULES.md` trước phiên duyệt chéo Gate 2a.
