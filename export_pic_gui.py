import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# config
CONFIG = {
    "source_folder": "",
    "target_folder": "",
    "numbering_digits": 5,
    "output_extension": ".psd",
    "include_original_char": False,
}

# cmd
def copy_tif_with_config(text, log_func):
    config = CONFIG

    if not os.path.exists(config["target_folder"]):
        os.makedirs(config["target_folder"])

    tif_files = []
    for file in os.listdir(config["source_folder"]):
        full = os.path.join(config["source_folder"], file)
        if os.path.isfile(full):
            ext = os.path.splitext(file)[1].lower()
            if ext in [".tif", ".tiff", ".psd"]:
                tif_files.append(file)

    file_map = {
        os.path.splitext(f)[0]: f for f in tif_files
    }

    cleaned_text = text.replace(" ", "").replace("\n", "").replace("\r", "")
    characters = list(cleaned_text)

    for i, char in enumerate(characters, 1):
        if char in file_map:
            src = os.path.join(config["source_folder"], file_map[char])

            if config["include_original_char"]:
                name = f"{i:0{config['numbering_digits']}d}_{char}{config['output_extension']}"
            else:
                name = f"{i:0{config['numbering_digits']}d}{config['output_extension']}"

            dst = os.path.join(config["target_folder"], name)
            shutil.copy2(src, dst)
            log_func(f"已复制: {char} -> {name}")
        else:
            log_func(f"⚠ 未找到字符 '{char}' 对应文件")

# gui
def choose_source():
    path = filedialog.askdirectory()
    if path:
        src_var.set(path)

def choose_target():
    path = filedialog.askdirectory()
    if path:
        tgt_var.set(path)

def run_task():
    CONFIG["source_folder"] = src_var.get()
    CONFIG["target_folder"] = tgt_var.get()

    if not CONFIG["source_folder"] or not CONFIG["target_folder"]:
        messagebox.showerror("错误", "请先选择源文件夹和目标文件夹")
        return

    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("错误", "请输入要处理的文字")
        return

    log_box.delete("1.0", tk.END)
    copy_tif_with_config(text, log)

def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

# ================= 主窗口 =================
root = tk.Tk()
root.title("TIF 批量导出工具")
root.geometry("600x500")

src_var = tk.StringVar()
tgt_var = tk.StringVar()

tk.Label(root, text="源 TIF 文件夹").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=src_var).pack(fill="x", padx=10)
tk.Button(root, text="选择源文件夹", command=choose_source).pack(padx=10, pady=2)

tk.Label(root, text="目标输出文件夹").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=tgt_var).pack(fill="x", padx=10)
tk.Button(root, text="选择目标文件夹", command=choose_target).pack(padx=10, pady=2)

tk.Label(root, text="输入文字").pack(anchor="w", padx=10, pady=(10, 0))
text_input = tk.Text(root, height=5)
text_input.pack(fill="x", padx=10)

tk.Button(root, text="开始处理", height=2, command=run_task).pack(pady=10)

tk.Label(root, text="日志输出").pack(anchor="w", padx=10)
log_box = scrolledtext.ScrolledText(root, height=10)
log_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

root.mainloop()
