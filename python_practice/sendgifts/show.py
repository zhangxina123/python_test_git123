# from gift import have_gift
import gift


# 展示礼物、
def show():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物啦，好开心")
    else:
        print("没有礼物")
