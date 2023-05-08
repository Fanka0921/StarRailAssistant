import win32gui
import win32print
import win32con
import time
import orjson
from tool.config import modify_json_file


print("3秒后开始获取,请确保你的游戏置顶")
time.sleep(3)
hwnd = win32gui.GetForegroundWindow()  # 根据当前活动窗口获取句柄
print(hwnd)
Text = win32gui.GetWindowText(hwnd)
print(Text)

# 获取活动窗口的大小
window_rect = win32gui.GetWindowRect(hwnd)
width = window_rect[2] - window_rect[0]
height = window_rect[3] - window_rect[1]

# 获取当前显示器的缩放比例
dc = win32gui.GetWindowDC(hwnd)
dpi_x = win32print.GetDeviceCaps(dc, win32con.LOGPIXELSX)
dpi_y = win32print.GetDeviceCaps(dc, win32con.LOGPIXELSY)
win32gui.ReleaseDC(hwnd, dc)
scale_x = dpi_x / 96
scale_y = dpi_y / 96

# 计算出真实分辨率
real_width = int(width * scale_x)
real_height = int(height * scale_y)

print(f"Real resolution: {real_width} x {real_height}")

print(f"real_width的值为:{real_width},已经成功应用,现在可以运行脚本了")

modify_json_file('config.json', 'real_width', real_width)