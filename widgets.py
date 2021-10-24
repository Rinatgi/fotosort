"""
    Создаем виджеты для нашего скрипта

"""
from tkinter import Button, Label, Entry, filedialog, StringVar
from fotosearch import receive_path


def create_widgets(window):
    global visible_photo_path, visible_sort_path
    default_text = StringVar(window, value='Путь к Вашим фотографиям для сортировки')
    default_text_save = StringVar(window, value='Путь куда будут отсортированы фаши фотографии')
    text_of_sort = Label(window, text='Выберите путь к вашим фотографиям:')
    text_of_save = Label(window, text='Выберите папку ,куда отсортировать фотографий:')
    button_choice_photo = Button(window,
                                 text='Выбрать папку',
                                 width=14,
                                 height=1,
                                 command=correction_photo_path
                                 )
    button_choice_sort = Button(window,
                                text='Выбрать папку',
                                width=14,
                                height=1,
                                command=correction_sort_path
                                )
    button_start = Button(window,
                          text='Сортировать',
                          width=10,
                          height=1,
                          command=start_sort
                          )
    visible_photo_path = Entry(window,
                               textvariable=default_text,
                               width=70,
                               #state=state
                               )
    visible_sort_path = Entry(window,
                              textvariable=default_text_save,
                              width=70,
                              #state=state
                              )
    text_of_sort.place(x=30, y=10)
    text_of_save.place(x=30, y=110)
    button_choice_photo.place(x=467, y=37)
    button_choice_sort.place(x=467, y=147)
    button_start.place(x=450, y=250)
    visible_photo_path.place(x=30, y=40)
    visible_sort_path.place(x=30, y=150)


def correction_photo_path():
    directory_open = filedialog.askdirectory()
    visible_photo_path.delete(0, 'end')
    visible_photo_path.insert(0, directory_open)


def correction_sort_path():
    directory_save= filedialog.askdirectory()
    visible_sort_path.delete(0, 'end')
    visible_sort_path.insert(0, directory_save)


def start_sort():
    receive_path()

