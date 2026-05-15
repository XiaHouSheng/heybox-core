import logging
import os
import time

path = "./src/main/caches/logs/"

def setUpLogger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[logging.FileHandler(path + time.strftime("%Y%m%d", time.localtime()) + ".log", "w", encoding="utf-8")
                                  ,logging.StreamHandler()
                                  ])
    return logging.getLogger(__name__)

if __name__ == "__main__":
    logger = setUpLogger()
    logger.info("这是一条INFO日志")
    logger.error("这是一条ERROR日志")
    logger.warning("这是一条WARNING日志")
