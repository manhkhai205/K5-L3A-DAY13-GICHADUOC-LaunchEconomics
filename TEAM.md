# Team

## Thông tin nhóm

- Tên nhóm: `GICHADUOC`
- Lớp: `L3A`
- Repo nhóm: `K5-L3A-DAY13-GICHADUOC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/manhkhai205/K5-L3A-DAY13-GICHADUOC-LaunchEconomics · nhánh `main` · commit chốt *(cập nhật trước khi nộp)*

## Thành viên

| STT | Họ tên                | MSSV        | Email                   | GitHub | Vai trò              |
| --- | --------------------- | ----------- | ----------------------- | ------ | -------------------- |
| 1   | Nguyễn Viết Mạnh Khải | 2A202603664 | manhkhai205@gmail.com   |        | **Người gắn nhãn 1** |
| 2   | Nguyễn Đình Quang     | 2A202603620 | quang8b9b@gmail.com     |        | **Người viết code**  |
| 3   | Vũ Đức Anh            | 2A202603573 | vuducanh039@gmail.com   |        | **Người kiểm số**    |
| 4   | Nguyễn Cảnh Hiếu      | 2A202603667 | hieucoi098765@gmail.com | canhhieu02 | **Người gắn nhãn 2, kiêm giữ hồ sơ** |

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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

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
