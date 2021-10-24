"""
    Создаем окно ввода пути для папки с фотографиями
"""
from tkinter import Tk


def create_window():
    window = Tk()
    # ширина экрана
    w = 580
    # высота экрана
    h = 300
    window.title('Сортируем фотографии')
    window.geometry('{}x{}'.format(w, h))
    window.minsize(width=280, height=180)
    return window
