# 🖼️ Waifu2x Slim – Offline Image Enhancement

Repo này là bản tối giản chỉ giữ lại phần **inference** của [nunif/waifu2x](https://github.com/nagadomi/nunif).  
Mục tiêu: **chạy offline bằng Python API** để xử lý ảnh (upscale + denoise) phục vụ OCR và làm rõ chữ/tài liệu.

---

## 🚀 Cài đặt

### 1. Clone repo
```bash
git clone https://github.com/MinhKhanh-EternAI/nunif.git
cd nunif
```

```bash
pip install -r requirements-min.txt
```

---

## Tham số chính

- **`model_type`**  
  - `art` → tranh, chữ, anime  
  - `art_scan` → tài liệu scan  
  - `photo` → ảnh chụp  

- **`method`**  
  - `scale` → chỉ phóng to  
  - `noise` → chỉ khử nhiễu  
  - `noise_scale` → khử nhiễu + phóng to  
  - `auto_scale` → tự chọn scale  

- **`noise_level`**  
  - `-1` = None  
  - `0` = Low  
  - `1` = Medium  
  - `2` = High  
  - `3` = Highest  

- **`scale`**: hệ số phóng to (`1.6`, `2`, `4`)  

- **`input/output`**  
  - `input` = đường dẫn ảnh gốc  
  - `output` = đường dẫn lưu ảnh sau xử lý  

---

## Bản quyền

Dựa trên dự án gốc [waifu2x](https://github.com/nagadomi/waifu2x) của **nagadomi**.  
Bản quyền thuộc về tác giả gốc và cộng đồng đóng góp.  

Repo này chỉ giữ lại phần inference, các phần training, web, GUI đã được lược bỏ.
