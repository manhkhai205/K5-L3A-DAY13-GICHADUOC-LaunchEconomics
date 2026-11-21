# Báo cáo cá nhân — NguyenCanhHieu-2A202603667

## 1. Thông tin thành viên

- Họ tên: Nguyễn Cảnh Hiếu
- MSSV: `2A202603667`
- Email: `hieucoi098765@gmail.com`
- Vai trong nhóm: **Người gắn nhãn 2, kiêm giữ hồ sơ**

## 2. Phần việc phụ trách

- **Giữ hồ sơ:** điền dần `report/team/ho_so_launch_v0.md` từ đầu buổi, theo từng checkpoint. Bảy mục, mỗi mục có con số chính, trạng thái và một vai trò phụ trách; dòng cuối là đề xuất.
- **Gắn nhãn 2 (CP3):** gắn độc lập 20 ca lỗi theo năm loại của Google PAIR, so với bộ nhãn của Người gắn nhãn 1, tính tỉ lệ đồng thuận và ghi quy tắc phân biệt trong `report/team/bang_loi.md`.
- **Kiểm tra nhất quán:** đối chiếu số trong hồ sơ với `src/lab13.py`, `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và `bang_loi.md` trước khi đưa vào hồ sơ.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0, đủ 7 mục và đề xuất:**
  - Mục 1, 3, 4 (CP1, E1): 4.472 đ/việc = 16,3× hoá đơn token; phạm vi `noi_dia` + `hang_nang` 0,38× (đã cộng cố định), cả hệ thống 0,49×; lý do loại `quoc_te` (1,88×) và `doi_tac` (0,85×); ba chỉ số trong đợt chạy thử 82,83% · 27,12% · 4,25% (phạm vi: 92,26% · 21,09% · 3,97%). Mọi số từ cột `_simulated` đều có nhãn `simulated`.
  - Mục 2, 7 (CP2): ba yếu tố nhạy nhất (làm lại +51,8%, xem lại +40,7%, lương +23,1%); ba rủi ro kinh tế khớp với E2 trong `chi_so.md`.
  - Mục 6 (CP4): tóm tắt `pilot_plan.yaml`: chia theo nhân viên 20 + 20, MDE 6 điểm, power 0,64 nếu tác động thật là 5 điểm, ba luật dừng.
  - Mục 5 và đề xuất (CP3, CP5): đồng thuận 20/20; đề xuất **Go có điều kiện** cho `noi_dia` + `hang_nang`, nêu hai con số bất lợi (xem lại 100% là 0,98–1,03×; power 0,64) và 5 điều kiện, mỗi điều kiện có vai trò phụ trách và ngày kiểm tra.
- **Nhãn lỗi:** tự gắn 20/20 ca trong 8 phút, không trao đổi với Người gắn nhãn 1. Khi gắn, đánh dấu 6 ca phân vân (6, 8, 9, 13, 18, 20) kèm lý do theo nguyên nhân gốc. Sau khi so: đồng thuận **20/20 = 100%**. Lý do của 6 ca này được dùng làm quy tắc phân biệt trong `bang_loi.md`.
- **Chạy lại code trên máy thứ hai:** cài môi trường và chạy `python lab13.py` trên máy của mình (khác máy Người viết code). Ba phép thử ĐẠT; số A2, A3, B, D1 khớp với số nhóm đã ghi.

## 4. Bằng chứng

- **Commit đã đẩy:**
  - `22dca68`: hồ sơ mục 1, 3, 4
  - `e8d0e05`: hồ sơ mục 2, 7
  - `cd139cc`: dòng Nhóm/Lớp, hồ sơ mục 6
  - `623da98`: cột "Nhãn người 2", đồng thuận 20/20, quy tắc cho 6 ca phân vân trong `bang_loi.md`
  - `68a9a6d`: hồ sơ mục 5 và đề xuất Go có điều kiện
- **File phụ trách:** `report/team/ho_so_launch_v0.md`, cột "Nhãn người 2" và phần quy tắc trong `report/team/bang_loi.md`, `report/team/2A202603667_NguyenCanhHieu.md`, phần của mình trong `TEAM.md`.
- **Ví dụ đối chiếu:** mục 3 ghi 0,38× theo A4: `3.072.513 ÷ 900 = 3.414 đ` biến đổi, cộng cố định `40.000.000 ÷ 33.750 = 1.185 đ`, ra `4.599 đ ÷ 12.000 = 0,38×` [simulated]. Số này khớp với bảng A4 trong `bang_chi_phi.md` và output của `lab13.py`.

## 5. Công cụ AI đã dùng

- **Claude Code (trong VS Code)**, dùng để:
  - tổng hợp các file đề (README, CHECKPOINTS, RUBRIC, RULES, SUBMISSION, hướng dẫn chi tiết) thành hướng dẫn làm bài và checklist cá nhân theo checkpoint;
  - viết script Python riêng, ngoài repo, tính lại A2, A3, A4 và ba chỉ số E1 trực tiếp từ hai file CSV để đối chiếu;
  - trích danh sách 20 ca lỗi từ file đề `.docx`;
  - soạn câu chữ cho các mục hồ sơ và đề xuất, dựa trên số trong các file của nhóm;
  - ghép hai bộ nhãn vào `bang_loi.md`, kiểm tra quy tắc và thao tác git (pull, commit, push từng file).
- **Không dùng AI để gắn nhãn.** 20 nhãn của Người gắn nhãn 2 do tôi tự gắn trước khi xem nhãn của Người gắn nhãn 1. AI chỉ chép nguyên văn vào bảng và không nhận xét đúng sai trước khi so.
- **Cách tự kiểm tra:**
  - so mọi con số trong hồ sơ với output `python lab13.py` của nhóm và với `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`;
  - kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load` và kiểm tra không còn dấu `?`;
  - quét `report/team/` để chắc không còn chỗ trống `...` và không có từ bị cấm;
  - đọc lại từng mục để chắc mỗi mục có con số, trạng thái hợp lệ và một vai trò phụ trách.

## 6. Tự đánh giá

- Hoàn thành hai vai đúng tiến độ. Hồ sơ đủ 7 mục và có đề xuất trước giờ duyệt chéo. Số trong hồ sơ khớp với các file nguồn của nhóm, và mọi số giả lập đều có nhãn `simulated`.
- Bộ nhãn độc lập đạt đồng thuận 20/20 với Người gắn nhãn 1.
- **Hạn chế:**
  - Phần câu chữ của hồ sơ được soạn với hỗ trợ của AI.
  - Ba chỉ số E1 hiện mới được tính bằng script riêng và công thức trong `chi_so.md`, chưa có trong `lab13.py`.
  - Hai ngày kiểm tra 2026-12-01 trong đề xuất do nhóm tự đặt, vì đề bài không cho ngày bắt đầu pilot.
