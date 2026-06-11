# AI-Elearning-2

Source code cho bài **EL02 - The Dining Philosophers Problem**.

## Mô hình bài toán

Bài toán được mô hình hóa dưới dạng CSP:

- Biến: `P1, P2, ..., Pn`, mỗi biến là một nhà triết học.
- Miền giá trị: `{Thinking, Eating}`.
- Ràng buộc: hai triết gia ngồi cạnh nhau không được cùng ở trạng thái `Eating`.
- Bàn tròn: `Pn` cũng ngồi cạnh `P1`.

## Cách chạy chương trình

Chạy với số triết gia mặc định `n = 5`:

```powershell
python src/main.py
```

Chạy với số triết gia khác:

```powershell
python src/main.py --philosophers 7
```

Hiển thị thêm trace kiểm tra ràng buộc:

```powershell
python src/main.py --trace
```

Nếu Windows chưa nhận lệnh `python`, có thể dùng:

```powershell
py -3 src/main.py
py -3 src/main.py --trace
```

## Cách chạy test

```powershell
python -m unittest discover -s test
```

Hoặc trên Windows:

```powershell
py -3 -m unittest discover -s test
```

## Kết quả mẫu với n = 5

Một nghiệm hợp lệ:

```text
P1 = Eating
P2 = Thinking
P3 = Eating
P4 = Thinking
P5 = Thinking
```

Nghiệm này hợp lệ vì không có hai triết gia ngồi cạnh nhau cùng `Eating`.

## Cấu trúc source

- `src/model.py`: tạo biến, miền giá trị, danh sách kề vòng tròn và kiểm tra ràng buộc.
- `src/solver.py`: giải bài toán và tìm complete assignment hợp lệ.
- `src/main.py`: file chạy chính.
- `test/test_solver.py`: kiểm thử mô hình, ràng buộc và nghiệm.
