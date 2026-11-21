# Team

## Thông tin nhóm

- Tên nhóm: `GICHADUOC`
- Lớp: `L3A`
- Repo nhóm: `K5-L3A-DAY13-GICHADUOC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/manhkhai205/K5-L3A-DAY13-GICHADUOC-LaunchEconomics · nhánh `main` · commit chốt _(cập nhật trước khi nộp)_

## Thành viên

| STT | Họ tên                | MSSV        | Email                   | GitHub      | Vai trò                              |
| --- | --------------------- | ----------- | ----------------------- | ----------- | ------------------------------------ |
| 1   | Nguyễn Viết Mạnh Khải | 2A202603664 | manhkhai205@gmail.com   | manhkhai205 | **Người gắn nhãn 1**                 |
| 2   | Nguyễn Đình Quang     | 2A202603620 | quang8b9b@gmail.com     | Quang-safjl | **Người viết code**                  |
| 3   | Vũ Đức Anh            | 2A202603573 | vuducanh039@gmail.com   | ducanh005   | **Người kiểm số**                    |
| 4   | Nguyễn Cảnh Hiếu      | 2A202603667 | hieucoi098765@gmail.com | canhhieu02  | **Người gắn nhãn 2, kiêm giữ hồ sơ** |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Viết Mạnh Khải - 2A202603664

### Phần việc phụ trách

- Khởi tạo, quản trị repo nhóm `K5-L3A-DAY13-GICHADUOC-LaunchEconomics` và điền thông tin thành viên ban đầu trong `TEAM.md`.
- **Người gắn nhãn 1 (CP3):** gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, so nhãn với Người gắn nhãn 2 và xây dựng bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`.
- **Theo dõi điều kiện "Xong khi" và kiểm tra đồng bộ hồ sơ:** rà soát toàn bộ `report/team/` theo `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`; tổng hợp `TEAM.md` và soạn nháp `report/team/group_report.md`.

### Đóng góp cụ thể

- Hoàn thiện bộ nhãn Người gắn nhãn 1 (20/20 ca theo nguyên nhân gốc) và bảng khắc phục 5 ca đại diện (Ca 9, 20, 18, 4, 17 — có event, ngưỡng, tần suất và 1 vai trò phụ trách) trong `report/team/bang_loi.md`, đạt đồng thuận **20/20 = 100%** với Người gắn nhãn 2.
- Kiểm tra chéo 2 commit của Hiếu (`623da98`, `68a9a6d`) và vá 2 điểm đồng bộ: bổ sung event `input_validation_failed` vào `report/team/chi_so.md` (11 event), cập nhật Điều kiện #3 trong `ho_so_launch_v0.md`, và bổ sung nhãn `[simulated]` cho `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`) trong `ho_so_launch_v0.md` và `pilot_plan.yaml`.
- Hoàn thiện báo cáo cá nhân, bổ sung đóng góp vào `TEAM.md` và soạn nháp `report/team/group_report.md` trước 17:00.

### Bằng chứng

- Commit `2a926ce` (`info team`) và `eefdf92` (`CP3: gắn nhãn độc lập 20 ca lỗi (Người gắn nhãn 1) và nháp bảng khắc phục 5 ca`).
- Các file `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`, `report/team/group_report.md`, `report/team/2A202603664_NguyenVietManhKhai.md`.

## Nguyễn Đình Quang - 2A202603620

### Phần việc phụ trách

- **Người viết code:** cài đặt môi trường Python, viết và chạy `src/lab13.py` hoàn thành phần tính toán cho CP1 (A1–A4), CP2 (B1–B4) và CP4 (D1), xuất số liệu cho các thành viên hoàn thiện bảng biểu và hồ sơ.

### Đóng góp cụ thể

- Viết 3 hàm xác suất A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), qua đủ 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Viết `mo_hinh(...)` đọc `logix_requests.csv` với `keep_default_na=False`, tính mọi lần chạy kể cả lần lỗi ở tử số và đếm `thanh_cong` ở mẫu số; tách CPS theo 4 loại và pivot tỉ lệ `ok` theo `attempt` (A3), thêm hàm `chi_phi_co_dinh` 40 triệu đ/tháng (A4).
- Viết vòng lặp 9 kịch bản độ nhạy (B1), đổi cặp (B2), chi phí cả hệ thống theo giới hạn `k = 1/2/3` (B3), kịch bản xem lại 100% và điểm hoà vốn (B4); viết `co_mau(p1, p2)`, tính design effect, cỡ mẫu hiệu dụng cho 5 phương án và power bằng `statsmodels` (D1).

### Bằng chứng

- Các commit `bd2e97b` (`CP1-CP2-CP4: lab13.py tinh chi phi, do nhay, co mau`), `ef85754` (`Sua dong in A1, them A4 chi phi co dinh`), `22c79fb`, `0c2858c` (`Bao cao ca nhan Nguyen Dinh Quang`).
- Các file `src/lab13.py` và `report/team/2A202603620_NguyenDinhQuang.md` cùng số liệu khớp đối chiếu A1–A4, B1–B4, D1 (CPS `4.472 đ` [simulated], `quoc_te` `22.515 đ = 1,88×` [simulated], tối ưu hệ thống `k = 2` đạt `6.901.220 đ` [simulated], cỡ mẫu `1.251/nhóm`, power `0,64` ở mức 5 điểm với `n = 859`).

## Vũ Đức Anh - 2A202603573

### Phần việc phụ trách

- **Người kiểm số:** đối chiếu kết quả từ `src/lab13.py`, tính tay kiểm chứng mẫu trên CSV, hoàn thiện `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md` và kiểm tra tính nhất quán của `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Kiểm chứng toàn bộ kết quả A1–A4, B1–B4, D1 trong `src/lab13.py` và các tỉ lệ phạm vi `noi_dia + hang_nang` (`92,26% · 21,09% · 3,97%`) trong `report/team/ho_so_launch_v0.md`.
- Điền đầy đủ bảng A1–A4, B1–B4 trong `report/team/bang_chi_phi.md` kèm nhãn `simulated` và so sánh cả hệ thống (`5.865 đ/yc = 0,49×`).
- Hoàn thiện kế hoạch pilot trong `report/team/pilot_plan.yaml` (cỡ mẫu `m >= 299`, `DE = 6,96`, power `0,64` ở mức 5 điểm, 3 luật dừng đủ 4 vế) và đặc tả chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế trong `report/team/chi_so.md`.

### Bằng chứng

- Commit `0cf3f47` (`CP1-CP2: hoan thanh bang_chi_phi.md (Nguoi kiem so)`).
- Các file `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/2A202603573_VuDucAnh.md` và tính tay kiểm chứng ca `RF-70012` (`8.406,01 đ`, `có phần simulated`).

## Nguyễn Cảnh Hiếu - 2A202603667

### Phần việc phụ trách

- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền dần `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn độc lập 20 ca lỗi ở CP3 và hoàn thiện phần so nhãn trong `report/team/bang_loi.md`; đối chiếu số giữa hồ sơ và các file của nhóm.

### Đóng góp cụ thể

- Hoàn thiện hồ sơ launch v0: đủ 7 mục, mỗi mục có con số chính, trạng thái và vai trò phụ trách. Đề xuất **Go có điều kiện** cho `noi_dia` + `hang_nang`, nêu hai con số bất lợi (xem lại 100% là 0,98–1,03× [simulated]; power 0,64) và 5 điều kiện có người phụ trách, ngày kiểm tra.
- Gắn độc lập 20/20 ca lỗi. Đồng thuận với Người gắn nhãn 1 là **20/20 = 100%**. Viết quy tắc phân biệt cho 6 ca phân vân (6, 8, 9, 13, 18, 20).
- Chạy lại `src/lab13.py` trên máy thứ hai (ba phép thử ĐẠT) và đối chiếu số trong hồ sơ với `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`.

### Bằng chứng

- Commit `22dca68`, `e8d0e05`, `cd139cc`, `68a9a6d` (hồ sơ) và `623da98` (`bang_loi.md`).
- Các file `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (cột "Nhãn người 2", tỉ lệ đồng thuận, quy tắc phân biệt), `report/team/2A202603667_NguyenCanhHieu.md`.
