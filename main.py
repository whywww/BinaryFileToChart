# -*- coding: UTF-8 -*-

"""
    Author: Weihaoyu
    Purpose:Chart project
    Created: 2017-12-7
"""
import matplotlib.pyplot as plt
import tkFileDialog
import numpy as np

'''
function process(x):
a math function with the parameter x
here we return cos(x)
'''


def process(x):
    np_x = np.array(x)
    return np.cos(np_x)


'''
function read_file_to_list(x, y):
it opens a file and read it by every certain bytes to list x and y
it returns x and y list
'''


def read_file_to_list(x, y):
    filename = tkFileDialog.askopenfilename(initialdir='C:/Desktop')
    input_file = open(filename, 'rb')
    try:
        while True:
            binary_chunk = input_file.read(8)  # read the file every 8 bytes
            # print binary_chunk
            if not binary_chunk:
                break
            x.append(int(binary_chunk, base=2))
            y.append(int(binary_chunk, base=2))
    finally:
        input_file.close()
    return x, y


'''
function draw_chart(y1, y2):
it uses parameters y1 and y2 as y coordinate to draw two subplots
x automatically increases by one pixel
'''


def draw_chart(x, y):
    plt.figure()

    plt.subplot(211)  # the first subplot
    plt.ylabel("original decimal value")
    plt.plot(x, 'm', linewidth=1.0)

    plt.subplot(212)  # the second subplot
    plt.ylabel("processed decimal value")
    plt.plot(y, 'c', linewidth=1.0)

    plt.show()


if __name__ == "__main__":
    original = []  # y coordinate of the first original subplot
    processed = []  # y coordinate of the second processed subplot

    (original, processed) = read_file_to_list(original, processed)
    processed = process(processed)  # process the y coordinate of the second plot(y2)
    draw_chart(original, processed)  # draw the chart








