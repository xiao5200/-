"""
该脚本用于分析指定目录中文件和文件夹的大小。

函数:
- format_size(size): 将文件大小格式化为带有适当单位（B、KB、MB、GB）的可读字符串。
- get_size(start_path): 计算给定路径中所有文件和文件夹的总大小。
- analyze_folder(path): 分析并打印指定路径中每个文件和文件夹的大小，并计算当前文件夹的总大小。
- main(): 提示用户输入目录路径，并调用 analyze_folder 函数进行分析。

用法:
运行脚本并在提示时输入要分析的目录路径。

异常:
- FileNotFoundError: 当指定路径未找到时引发。
- PermissionError: 当访问某些文件或文件夹的权限不足时引发。
