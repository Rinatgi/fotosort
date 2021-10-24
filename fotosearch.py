"""
    здесь сортируем наши фотографии
"""


import os
from datetime import datetime
import shutil
import widgets


def receive_path():
    path_photo = widgets.visible_photo_path.get()
    path_sort = widgets.visible_sort_path.get()
    os.chdir(path_photo)
    for image in os.listdir(path_photo):
        image_path = os.path.join(path_photo, image)
        date_change = os.path.getmtime(image_path)
        year_create = datetime.fromtimestamp(date_change).strftime("%Y")
        month_create = datetime.fromtimestamp(date_change).strftime("%m")
        new_path_sort = os.path.join(path_sort, year_create)
        os.chdir(path_sort)
        if not os.path.exists(new_path_sort):
            os.mkdir(year_create)

        os.chdir(new_path_sort)

        if not os.path.isdir(month_create):
            os.mkdir(month_create)

        new_path = os.path.join(new_path_sort, month_create)

        print(new_path)
        print(image)
        shutil.move(image_path, new_path)



