# *_* coding：UTF-8 *_*
# 开发团队：
# 开发人员：知 仁
# 开发时间：2020/9/28 8:33
# 文件名称：zr_01_寻找坐标点.py
# 开发工具：PyCharm

from PIL import Image, ImageDraw
import random


def test_dot():
    """
    输出图像中的像素值、验证
    :return:
    """
    for i in range(img.width):
        for j in range(img.height):
            # print("像素值：", img.getpixel((i, j)))

            # if 10 < img.getpixel((i, j)) < 240:
            #     print("像素值：", img.getpixel((i, j)))

            if img.getpixel((i, j)) != img.getpixel((i-img.width, j-img.height)):
                print("计算错误！")


def test_dot_y_axis(img_x_axis):
    """
    打印某列中满足像素值得所有点
    :param img_x_axis: 列
    :return:
    """
    print("*" * 50)
    print("列出（%d, x)中所有黑点坐标：" % img_x_axis)
    for i in range(img.height):
        if img.getpixel((img_x_axis, i)) > 240:
            print("（%d, %d)的像素值为：%d" % (img_x_axis, i, img.getpixel((img_x_axis, i))))


def test_dot_x_axis(img_y_axis):
    """
    打印某行中满足像素值得所有点
    :param img_y_axis: 行
    :return:
    """
    print("*" * 50)
    print("列出（x, %d)中所有黑点坐标：" % img_y_axis)
    for i in range(img.width):
        if img.getpixel((i, img_y_axis)) > 240:
            print("测试坐标（%d, %d)的像素值为：%d" % (i, img_y_axis, img.getpixel((i, img_y_axis))))


def find_left_dot(image):
    """
    寻找最左侧点
    :return:
    """
    i_last = image.width
    left_list = list()
    for i in range(image.width):  # 从左往右，从上往下遍历像素
        if i > i_last:
            # print(left_list)
            return left_list
        for j in range(image.height):
            if image.getpixel((i, j)) > 240:
                i_last = i
                print("左侧坐标为：(%d, %d)    像素值为：%d" % (i, j, image.getpixel((i, j))))
                left_list.append((i, j))


def find_up_dot(image):
    """
    寻找最上侧点
    :return:
    """
    i_last = image.height
    up_list = list()
    for i in range(image.height):  # 从上往下，从左往右遍历像素值
        if i > i_last:
            return up_list
        for j in range(image.width):
            # print("像素值：", img.getpixel((j, i)))
            if image.getpixel((j, i)) > 240:
                i_last = i
                print("上侧坐标为：(%d, %d)    像素值为：%d" % (j, i, image.getpixel((j, i))))
                up_list.append((j, i))


def find_right_dot(image):
    """
    寻找最右侧点
    :return:
    """
    i_last = image.width
    right_list = list()
    for i in range(image.width):  # 从右往左，从上往下遍历像素值
        if i > i_last:
            return right_list
        for j in range(image.height):
            if img.getpixel((-i - 1, j)) > 240:
                i_last = i
                print("右侧坐标为：(%d, %d)    像素值为：%d" % (-i - 1 + image.width, j, image.getpixel((-i - 1, j))))
                right_list.append((-i - 1 + image.width, j))


def draw_triangle(image, left_list, up_list, right_list):
    """
    随机选点，画三角形
    :param left_list:
    :param up_list:
    :param right_list:
    :return:
    """
    draw = ImageDraw.Draw(image)  # 实例化一个对象
    x1, y1 = left_list[random.randint(0, len(left_list) - 1)]
    x2, y2 = up_list[random.randint(0, len(up_list) - 1)]
    x3, y3 = right_list[random.randint(0, len(right_list) - 1)]
    draw.line((x1, y1, x2, y2), fill=255, width=2)  # 线的起点和终点，线宽
    draw.line((x2, y2, x3, y3), fill=255, width=2)  # 线的起点和终点，线宽
    draw.line((x3, y3, x1, y1), fill=255, width=2)  # 线的起点和终点，线宽


# 主函数
if __name__ == "__main__":

    img = Image.open('picture.jpg')

    # 显示图形信息
    print("图片格式", img.format)
    print("相片大小：", img.size)

    # test_dot()

    # 寻找最左、上、右侧点
    list_left = find_left_dot(img)
    list_up = find_up_dot(img)
    list_right = find_right_dot(img)

    # 画三角形
    draw_triangle(img, list_left, list_up, list_right)

    # test_dot_y_axis(200)
    # test_dot_x_axis(100)

    # 显示图片
    img.show()
