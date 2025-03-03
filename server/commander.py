import logging

from server.send_file import send_file_message
from utils.download import download


def bot_commander(wcf, msg):
    logging.info("命令监听已启动，等待新命令...")
    if "douyin" in msg.content:
        logging.info(msg.content)
        file_path = download('https://9yin.woniu.com/static/web201588/video/201908.mp4')
        logging.info("下载完成: %s", file_path)
        # 等待1秒执行
        send_file_message(wcf, msg.roomid, file_path)
