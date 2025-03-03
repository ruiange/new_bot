import logging
import time

from server.send_file import send_file_message
from utils.download import download


def bot_commander(wcf, msg):
    logging.info("命令监听已启动，等待新命令...")
    if "douyin" in msg.content:
        logging.info(msg.content)
        file_path = download('http://101.126.92.189:8090/api/download?url=https://v.douyin.com/i5kLmruj/&prefix=true&with_watermark=true')
        logging.info("下载完成: %s", file_path)
        # 等待1秒执行
        time.sleep(1)
        send_file_message(wcf, msg.roomid, file_path)
