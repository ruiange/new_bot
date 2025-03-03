import os
import requests  # 确保已安装 requests 库
from tqdm import tqdm  # 用于显示进度条

def download(url):
    # 获取项目根目录
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # 获取项目根目录
    file_dir = os.path.join(root_dir, 'file')  # 拼接出 file 文件夹的路径

    # 如果 file 目录不存在，则创建该目录
    os.makedirs(file_dir, exist_ok=True)

    # 从 URL 中提取文件名
    filename = os.path.basename(url)
    file_path = os.path.join(file_dir, filename)

    # 下载文件，使用流式请求
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 对于错误的响应抛出异常

    # 获取文件大小
    total_size = int(response.headers.get('content-length', 0))

    # 使用tqdm创建进度条
    with open(file_path, 'wb') as file, \
         tqdm(desc=filename,
              total=total_size,
              unit='iB',
              unit_scale=True,
              unit_divisor=1024) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

    # 返回下载文件的绝对路径
    return os.path.abspath(file_path)


