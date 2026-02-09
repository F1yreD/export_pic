import os
import shutil

# 配置文件
CONFIG = {
    "source_folder": "./source_tif",  # 源TIF图片文件夹
    "target_folder": "./output_tif",  # 目标文件夹
    "numbering_digits": 5,  # 编号位数
    "output_extension": ".psd",  # 输出文件扩展名
    "include_original_char": False,  # 是否在文件名中包含原字符
}


def copy_tif_with_config(text):
    """
    使用配置复制TIF图片
    """
    config = CONFIG

    # 创建目标文件夹
    if not os.path.exists(config["target_folder"]):
        os.makedirs(config["target_folder"])

    # 获取TIF图片文件
    tif_files = []
    for file in os.listdir(config["source_folder"]):
        if os.path.isfile(os.path.join(config["source_folder"], file)):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in ['.tif', '.tiff','.psd']:
                tif_files.append(file)

    # 创建映射
    file_map = {}
    for file in tif_files:
        filename_without_ext = os.path.splitext(file)[0]
        file_map[filename_without_ext] = file

    # 处理文字
    cleaned_text = text.replace(' ', '').replace('\n', '').replace('\r', '')
    characters = list(cleaned_text)

    # 复制图片
    for i, char in enumerate(characters, 1):
        if char in file_map:
            source_file = os.path.join(config["source_folder"], file_map[char])

            if config["include_original_char"]:
                new_filename = f"{i:0{config['numbering_digits']}d}_{char}{config['output_extension']}"
            else:
                new_filename = f"{i:0{config['numbering_digits']}d}{config['output_extension']}"

            target_file = os.path.join(config["target_folder"], new_filename)
            shutil.copy2(source_file, target_file)
            print(f"已复制: {char} -> {new_filename}")
        else:
            print(f"警告: 未找到字符 '{char}' 对应的TIF图片文件")


if __name__ == "__main__":
    # 修改配置
    CONFIG["source_folder"] = input("请输入源TIF图片文件夹路径: ").strip()
    CONFIG["target_folder"] = input("请输入目标文件夹路径: ").strip()

    # 输入文字
    text = input("请输入要处理的文字: ").strip()

    # 执行复制
    copy_tif_with_config(text)