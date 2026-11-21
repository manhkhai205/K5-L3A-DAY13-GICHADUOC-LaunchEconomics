"""Lab 13 - Định giá agent và lập kế hoạch pilot (LogiX-VN, Gate 2a).

Chạy trong thư mục src/:  python lab13.py
Mọi số tính từ cột *_simulated đều phải ghi nhãn [simulated] trong báo cáo.
"""
import math
from statistics import NormalDist

import pandas as pd

# ---------------------------------------------------------------------------
# Giả định chung (docs/du_lieu_va_cong_thuc.md)
# ---------------------------------------------------------------------------
GIA_VAO = 26          # đ / 1.000 token vào
GIA_RA = 130          # đ / 1.000 token ra
GIA_TOOL = 15         # đ / lần gọi tool
LUONG_PHUT = 2000     # đ / phút nhân viên
BASELINE_NGUOI = 12000  # đ / yêu cầu nhân viên tự làm (6 phút)


# ---------------------------------------------------------------------------
# CP1 · A1: ba hàm xác suất
# ---------------------------------------------------------------------------
def so_lan_chay_ky_vong(p, k=None):
    """E[N]: số lần chạy kỳ vọng cho một yêu cầu."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """P_k: xác suất thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính theo bội số chi phí một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9
    print("A1: qua ca 3 phep thu (1.20 · 1.25 · 1.25)")


# ---------------------------------------------------------------------------
# CP1 · A2: mô hình chi phí mỗi việc thành công
# ---------------------------------------------------------------------------
def _so(series):
    return pd.to_numeric(series, errors="coerce").fillna(0)


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    reqs = reqs.copy()
    r = runs[runs["request_id"].isin(reqs["request_id"])].copy()
    attempt = _so(r["attempt"])

    if max_lan_chay is not None:
        r = r[attempt <= max_lan_chay]
        attempt = _so(r["attempt"])
        vuot = _so(reqs["so_lan_chay"]) > max_lan_chay
        reqs.loc[vuot, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[vuot, ["phut_xem_lai_simulated", "phut_lam_lai_simulated"]] = 0

    token_moi_lan = (_so(r["tokens_in"]) / 1000 * gia_vao
                     + _so(r["tokens_out"]) / 1000 * gia_ra)
    tool_moi_lan = _so(r["tool_calls"]) * gia_tool

    token = token_moi_lan.sum()
    tool = tool_moi_lan.sum()
    chay_lai = (token_moi_lan + tool_moi_lan)[attempt > 1].sum()
    xem_lai = (_so(reqs["phut_xem_lai_simulated"]) * luong_phut * he_so_xem_lai).sum()
    lam_lai = (_so(reqs["phut_lam_lai_simulated"]) * luong_phut * he_so_lam_lai).sum()
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs["ket_qua"] == "thanh_cong").sum())

    return {
        "token": token,
        "tool": tool,
        "chay_lai": chay_lai,
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": tong / thanh_cong if thanh_cong else float("nan"),
        "hoa_don_moi_yc": (token + tool) / len(reqs) if len(reqs) else float("nan"),
        "so_yc": len(reqs),
        "so_lan_chay": len(r),
    }


def in_mo_hinh(kq):
    print(f"  Token            {kq['token']:>12,.0f} đ  [trace]")
    print(f"  Tool             {kq['tool']:>12,.0f} đ  [trace]")
    print(f"  Chay lai (l2,3)  {kq['chay_lai']:>12,.0f} đ  [trace]")
    print(f"  Xem lai          {kq['xem_lai']:>12,.0f} đ  [simulated]")
    print(f"  Lam lai          {kq['lam_lai']:>12,.0f} đ  [simulated]")
    print(f"  Tong             {kq['tong']:>12,.0f} đ  [co simulated]")
    print(f"  Viec thanh cong  {kq['thanh_cong']:>12,}")
    print(f"  CPS              {kq['cps']:>12,.0f} đ  [simulated]")
    print(f"  Hoa don/yeu cau  {kq['hoa_don_moi_yc']:>12,.1f} đ  [trace]")


# ---------------------------------------------------------------------------
# CP1 · A3: tách theo loại
# ---------------------------------------------------------------------------
def theo_loai(runs, reqs):
    print("\nA3: theo loai")
    print(f"  {'loai':<10}{'yc':>6}{'ti le TC':>10}{'lan/yc':>8}{'CPS [sim]':>12}{'x12k':>7}")
    for loai in ["noi_dia", "hang_nang", "quoc_te", "doi_tac"]:
        sub = reqs[reqs["loai"] == loai]
        kq = mo_hinh(runs, sub)
        print(f"  {loai:<10}{len(sub):>6}{kq['thanh_cong'] / len(sub):>10.1%}"
              f"{kq['so_lan_chay'] / len(sub):>8.2f}{kq['cps']:>12,.0f}"
              f"{kq['cps'] / BASELINE_NGUOI:>6.2f}x")

    # Chạy lại có giúp không: tỉ lệ ok theo attempt và loai
    m = runs.merge(reqs[["request_id", "loai"]], on="request_id")
    m["ok"] = (m["status"] == "ok").astype(float)
    print("\n  Ti le ok (%) theo attempt x loai:")
    print(m.pivot_table(index="attempt", columns="loai", values="ok", aggfunc="mean")
          .mul(100).round(1).to_string())


# ---------------------------------------------------------------------------
# CP2 · B: độ nhạy
# ---------------------------------------------------------------------------
def do_nhay(runs, reqs):
    goc = mo_hinh(runs, reqs)["cps"]
    kich_ban = {
        "Gia token x2":       dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
        "Gia token x0.5":     dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        "Xem lai x2":         dict(he_so_xem_lai=2),
        "Xem lai x0.5":       dict(he_so_xem_lai=0.5),
        "Lam lai x2":         dict(he_so_lam_lai=2),
        "Lam lai x0.5":       dict(he_so_lam_lai=0.5),
        "Luong +25%":         dict(luong_phut=LUONG_PHUT * 1.25),
        "Toi da 2 lan chay":  dict(max_lan_chay=2),
        "Chi 1 lan chay":     dict(max_lan_chay=1),
    }
    print(f"\nB1: do nhay (goc {goc:,.0f} đ) [simulated]")
    for ten, ts in kich_ban.items():
        cps = mo_hinh(runs, reqs, **ts)["cps"]
        print(f"  {ten:<20}{cps:>10,.0f} đ  {(cps / goc - 1):+.1%}")

    cps2 = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2)["cps"]
    print(f"\nB2: token x2 + xem lai x2 -> {cps2:,.0f} đ ({cps2 / goc - 1:+.1%}) [simulated]")

    print("\nB3: gioi han chay va chi phi he thong [simulated]")
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = kq["so_yc"] - kq["thanh_cong"]
        he_thong = kq["tong"] + BASELINE_NGUOI * khong_tc
        print(f"  k={k}: tong {kq['tong']:,.0f} đ | khong TC {khong_tc} | "
              f"he thong {he_thong:,.0f} đ | CPS {kq['cps']:,.0f} đ")

    # B4: xem lại 100% cho noi_dia + hang_nang
    sub = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    r = runs[runs["request_id"].isin(sub["request_id"])]
    so_ok = r.loc[r["status"] == "ok", "request_id"].nunique()
    so_lam_lai = int((sub["ket_qua"] == "lam_lai").sum())
    token_tool = (_so(r["tokens_in"]) / 1000 * GIA_VAO + _so(r["tokens_out"]) / 1000 * GIA_RA
                  + _so(r["tool_calls"]) * GIA_TOOL).sum()
    thanh_cong = so_ok - so_lam_lai
    print(f"\nB4: xem lai 100% (noi_dia + hang_nang, {len(sub)} yc) [simulated]")
    print(f"  yc co it nhat 1 lan ok: {so_ok}, ca lam_lai: {so_lam_lai}, "
          f"token+tool: {token_tool:,.0f} đ, thanh cong: {thanh_cong}")
    for phut_lam_lai in [9, 15.3]:
        tong = so_ok * 5 * LUONG_PHUT + so_lam_lai * phut_lam_lai * LUONG_PHUT + token_tool
        cps = tong / thanh_cong
        hoa_von = (BASELINE_NGUOI * thanh_cong - so_lam_lai * phut_lam_lai * LUONG_PHUT
                   - token_tool) / (so_ok * LUONG_PHUT)
        print(f"  lam lai {phut_lam_lai} phut: tong {tong:,.0f} đ -> {cps:,.0f} đ "
              f"= {cps / BASELINE_NGUOI:.2f}x | hoa von khi xem lai <= {hoa_von:.1f} phut")


# ---------------------------------------------------------------------------
# CP4 · D1: cỡ mẫu
# ---------------------------------------------------------------------------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def design_effect(m, icc):
    return 1 + (m - 1) * icc


def ke_hoach_mau(icc=0.02):
    print("\nD1: co mau (baseline 0.70, +5 diem, ICC 0.02)")
    n = co_mau(0.70, 0.75)
    print(f"  a. Theo yeu cau: {n} moi nhom")
    de = design_effect(75, icc)
    n_nv = math.ceil(n * de)
    print(f"  b. Theo nhan vien m=75: DE {de:.2f} -> {n_nv} moi nhom -> "
          f"{math.ceil(n_nv / 75)} nguoi/nhom, tong {2 * math.ceil(n_nv / 75)} > 40: khong du")
    print(f"  c. 20 nhan vien/nhom: toi da {20 / icc:,.0f} < {n}: khong dat")
    print(f"  d. 6 depot/nhom: toi da {6 / icc:,.0f}")
    n6 = co_mau(0.70, 0.76)
    m = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    print(f"  e. Chenh 6 diem ({n6}/nhom), 20 nguoi: m >= {m} (DE {design_effect(m, icc):.2f})")
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        pw = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70),
                                    nobs1=n6, alpha=0.05)
        print(f"  Power voi muc 5 diem, n={n6}: {pw:.2f}")
    except ImportError:
        print("  (chua cai statsmodels nen bo qua phan power)")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    kiem_tra_dap_an_biet_truoc()

    runs = pd.read_csv("logix_runs.csv", keep_default_na=False)
    reqs = pd.read_csv("logix_requests.csv", keep_default_na=False)

    print("\nA2: toan bo mau")
    in_mo_hinh(mo_hinh(runs, reqs))
    theo_loai(runs, reqs)
    do_nhay(runs, reqs)
    ke_hoach_mau()