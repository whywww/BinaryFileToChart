### Chart系统

##### 环境配置：

python2.7

安装matplotlib库：`pip install matplotlib`

安装numpy库：`pip install numpy`

##### 系统功能：

本系统的主要功能为读入用户在对话框中选择的含有二进制数据的文件，将每8个字节分割为一小段，并将这段二进制数转换为十进制数，根据此数据以及经过数学变换的数据绘制在两个通道，也就是两张子图中：

子图一中，纵坐标为原始数据，即每个生成的十进制数；横坐标自动递增一个像素，最后将点连接起来。

子图二中，纵坐标根据文件的原始数据做数学变换处理，此处选用cos函数做数据变换，即将纵坐标，横坐标与子图一相同，自动递增一个像素，最后将点连接起来。

以上两张图的颜色均可以自定义，也可以更换数学变换的处理方式。

用户也可以对两张子图进行交互操作：

拖动数据查找功能：用户可以拖拽图像上下左右移动，当鼠标焦点移动到某点时，可以显示该点的横纵坐标值。

放大和缩小查看图像：用户可以通过放大镜可以放大和缩小图像的局域或整体部分，并可以回退上一步以及撤销操作，或直接返回到初始状态。

压缩和扩展显示数据：用户可以通过调整子图的大小来进行压缩和扩展的操作。在压缩扩展时，横纵坐标的值会自动变换适应图片数据。

保存图片功能：用户可以点击保存按钮，将图片直接保存至电脑，并可以选择保存路径。

##### 数据介绍：

*main:*

`original`,`processed`分别为两个通道的纵坐标列表：

*read_file_to_list()：*

`filename`保存读入文件名

`input_file`保存读入的二进制文件内容

*process()：*

`np_x`为numpy型数组，用来保存参数x列表

##### 处理算法介绍：

*main:*

*main()**：***

主函数中，定义了两个列表变量来保存两个通道的纵坐标值，接着调用了三个函数：`read_file_to_list(x,y)`将文件读入到这两个列表中；`process(x)`进行cos函数数学处理；`draw_chart(x, y)`进行绘图操作。

```python
	original = []  # y coordinate of the first original subplot
    processed = []  # y coordinate of the second processed subplot

    (original, processed) = read_file_to_list(original, processed)
    processed = process(processed)  # process the y coordinate of the second plot(y2)
    draw_chart(original, processed)  # draw the chart
```

*read_file_to_list(x, y):*

首先，这个函数中，读入了用户所选择的文件，首先将全部文件读入至`input_file`中，然后以while循环的方式从`input_file`中每8个字节为单位读取二进制数至`binary_chunck`中，每读到一个8字节数，就将它加入两个参数`x`,`y`列表中。最后将两个列表返回。

```python
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
```

*process(x):*

这个函数主要处理数学运算，以`x`列表为参数，将其转化为numpy的array型数组，方便进行数学运算。返回处理后的数组。

```python
'''
function process(x):
a math function with the parameter x
here we return cos(x)
'''

def process(x):
    np_x = np.array(x)
    return np.cos(np_x)
```

*draw_chart(x,y):*

这个函数主要进行绘图功能，运用了python中的matplotlib库绘图，以之前处理过的两个纵坐标列表为参数，分别绘制在两个subplot子图中，第一张子图的纵坐标为原始数据，第二张子图的纵坐标为处理后的数据，横坐标自动递增一个像素。

```python
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
```

