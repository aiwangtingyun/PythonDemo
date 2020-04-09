# -*- coding: utf-8 -*-
# @Time    : 2020/03/30
# @Author  : wangtingyun

import os
from urllib import request

from center.config_center import IMAGE_DIR


def get_html(url):
    pass


def get_images(html):
    pass


def get_image(url, save_path):
    image_name = os.path.basename(url)
    filename = os.path.join(save_path, image_name)
    request.urlretrieve(icon_url, filename)


if __name__ == '__main__':

    icon_url = 'https://res11-aipai-pic.weplay.cn/nobility/nobility_horse_king_ani.webp'
    get_image(icon_url, IMAGE_DIR)
