import os

def format_size(size):
    """根据文件大小选择合适的单位显示"""
    if size < 1024:
        return f"{size:.2f} B"  # 更精确地处理小于1KB的情况
    elif size < 1024**2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024**3:
        return f"{size / (1024**2):.2f} MB"
    else:
        return f"{size / (1024**3):.2f} GB"

def get_size(start_path):
    """计算给定路径下所有文件和文件夹的总大小"""
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):  # 排除符号链接
                total_size += os.path.getsize(fp)
    return total_size

def analyze_folder(path):
    """分析并打印指定路径下的文件夹及其文件大小，并计算当前文件夹的总大小"""
    print(f"正在分析: {path}")
    total_folder_size = 0
    try:
        # 使用os.scandir()，比os.listdir()更高效
        for entry in os.scandir(path):
            if entry.is_dir():  # 如果是目录
                size = get_size(entry.path)
                total_folder_size += size
                print(f"文件夹: {entry.name}, 大小: {format_size(size)}")
            elif entry.is_file():  # 如果是文件
                size = entry.stat().st_size
                total_folder_size += size
                print(f"文件: {entry.name}, 大小: {format_size(size)}, 类型: {os.path.splitext(entry.name)[1]}")
        print(f"当前文件夹总大小: {format_size(total_folder_size)}")
    except FileNotFoundError:
        print("系统找不到指定的路径。")
    except PermissionError:
        print("权限不足，无法访问某些文件或文件夹。")

def main():
    path = input("请输入要分析的目录路径: ")
    analyze_folder(path)

if __name__ == "__main__":
    main()
