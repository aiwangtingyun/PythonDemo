import os

from center.config_center import ROOT_DIR
from tools.decorator_tool import singleton


@singleton
class IconCenter:

    def __init__(self):
        pass

    def res_path(self, path):
        """
        获取资源图片路径
        :param path: 图片相对路径
        :return: 资源图片的绝对路径
        """
        icon_dir = os.path.join(ROOT_DIR, "images")
        icon_path = os.path.join(icon_dir, path).replace("\\", "/")
        return icon_path
