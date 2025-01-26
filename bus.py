import sys
import time
import os

def marquee_text_multiple_lines(lines, width=30, delay=0.1):
    # Thêm khoảng trống hai bên cho từng dòng
    padded_lines = [" " * width + line + " " * width for line in lines]

    # Số bước cần di chuyển (tính theo dòng dài nhất)
    steps = max(len(padded_line) - width + 1 for padded_line in padded_lines)

    for i in range(steps):
        # Hiển thị từng dòng với đoạn hiển thị
        for line in padded_lines:
            part = line[i:i+width]  # Lấy đoạn văn bản hiển thị
            sys.stdout.write(part + "\n")  # Hiển thị từng dòng
        sys.stdout.write("\033[F" * len(lines))  # Đưa con trỏ lên trên để viết đè
        sys.stdout.flush()
        time.sleep(delay)
    print("\n" * len(lines))  # Xuống dòng sau khi hoàn thành
for i in range(99):
 os.system('cls' if os.name == 'nt' else 'clear')
 marquee_text_multiple_lines(
    [
        "                          __",
        " .-----------------------'  |",
        "/| _ .---. .---. .---. .---.|",
        "|j||||___| |___| |___| |___||",
        "|=|||=======================|",
        "[_|j||(O)\__________|(O)\___]"
    ],
    width=30,
    delay=0.1
)