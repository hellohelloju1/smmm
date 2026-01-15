import streamlit as st
import pandas as pd
from PIL import Image

st.title("生命密码计算器")
num1, num2, num3, num4, num5, num6, num7, num8, num9 = 0,0,0,0,0,0,0,0,0
background = Image.open("blankboard.png")
onering = Image.open(r"1ring.png")
tworing = Image.open(r"2ring.png")
threering = Image.open(r"3ring.png")
fourring = Image.open(r"4ring.png")
fivering = Image.open(r"5ring.png")
sixring = Image.open(r"6ring.png")
sevenring = Image.open(r"7ring.png")

fullbdaylist = []
addtgtnums = []
fullnum, stepnum1, stepnum2,stepnum3, shengmingshu,shengrishu = 0,0,0,0,0,0
bdayyear = st.number_input("生日年", min_value=1900)
bdaymonth = st.number_input("生日月", min_value=1, max_value=12)
bdayday = st.number_input("生日日", min_value=1, max_value=31)
# st.sidebar.button("计算") or
if st.button("计算"):
    fullbday = str(bdayyear) + str(bdaymonth)+ str(bdayday)
    for index, character in enumerate(fullbday):
        fullbdaylist.append(int(character))
    # print(fullbdaylist)

    # 整个生日计算
    for each in fullbdaylist: 
        stepnum1 += each
        addtgtnums.append(each)
    #第二步

    stepnum2 = int(str(stepnum1)[0]) + int(str(stepnum1)[1])
    addtgtnums.append(int(str(stepnum1)[0]))
    addtgtnums.append(int(str(stepnum1)[1]))

    if len(str(stepnum2)) == 2:
        stepnum3 = int(str(stepnum2)[0]) + int(str(stepnum2)[1])
        addtgtnums.append(int(str(stepnum2)[0]))
        addtgtnums.append(int(str(stepnum2)[1]))
    else:
        stepnum3 = stepnum2
    # shengmingshu = stepnum3
    #生日数
    if bdayday == 11:
        addtgtnums.append(1)
        addtgtnums.append(1)
        shengmingshu = 11
    elif bdayday == 29:
        addtgtnums.append(1)
        addtgtnums.append(1)
        addtgtnums.append(2)
        shengmingshu = 2
    else:
            #

        shengmingshu = stepnum3
        addtgtnums.append(shengmingshu)
    if len(str(bdayday)) == 2:
        bdaynum = int(str(bdayday)[0]) + int(str(bdayday)[1])
        while len(str(bdaynum)) > 1:
            bdaynum = int(str(bdaynum)[0]) + int(str(bdaynum)[1])
    else:
        bdaynum = int(bdayday)
    addtgtnums.append(bdaynum)
        

    zodiacs = [(120, '摩羯座',1), (218, '水瓶座',2), (320, '双鱼座',3), (420, '白羊座',1), (521, '金牛座',2),
            (621, '双子座',3), (722, '巨蟹座',4), (823, '狮子座',5), (923, '处女座',6),(1023, '天平座',7),
            (1122, '天蝎座',8), (1222, '射手座',9), (1231, '摩羯座',1)]
    for z in zodiacs:
        if int(str(bdaymonth)+str(bdayday)) <= z[0]:
            starsign = z[1]
            addtgtnums.append(z[2])
            break




    for each in addtgtnums: 
        if each == 1:
            num1 += 1
        if each == 2:
            num2 += 1
        if each == 3:
            num3 += 1
        if each == 4:
            num4 += 1
        if each == 5:
            num5 += 1
        if each == 6:
            num6 += 1
        if each == 7:
            num7 += 1
        if each == 8:
            num8 += 1
        if each == 9:
            num9 += 1
#     st.write(pd.DataFrame({
#     '数字1的个数：': [num1],
#     '数字2的个数：': [num2],
#     '数字3的个数：': [num3],
#     '数字4的个数：': [num4],
#     '数字5的个数：': [num5],
#     '数字6的个数：': [num6],
#     '数字7的个数：': [num7],
#     '数字8的个数：': [num8],
#     '数字9的个数：': [num9],
# }),columns=('col %d' % i for i in range(20)))
    # num1show = "", 

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="生命数", value=shengmingshu)
    with col2:
        st.metric(label="星座", value=starsign)
    with col3:
        st.metric(label="星座数", value=z[2])

    st.divider()
    tempringname = Image.open(f"{num1}ring.png")
    background.paste(tempringname, (35,30), mask = tempringname)
    tempringname = Image.open(f"{num2}ring.png")
    background.paste(tempringname, (35,300), mask = tempringname)
    tempringname = Image.open(f"{num3}ring.png")
    background.paste(tempringname, (35,565), mask = tempringname)
    tempringname = Image.open(f"{num4}ring.png")
    background.paste(tempringname, (300,30), mask = tempringname)
    tempringname = Image.open(f"{num5}ring.png")
    background.paste(tempringname, (300,300), mask = tempringname)
    tempringname = Image.open(f"{num6}ring.png")
    background.paste(tempringname, (300,565), mask = tempringname)
    tempringname = Image.open(f"{num7}ring.png")
    background.paste(tempringname, (565,30), mask = tempringname)
    tempringname = Image.open(f"{num8}ring.png")
    background.paste(tempringname, (565,300), mask = tempringname)
    tempringname = Image.open(f"{num9}ring.png")
    background.paste(tempringname, (565,565), mask = tempringname)
    lianxian = []
    verticalline = Image.open("verticalline.png")
    horizontalline =Image.open("horizontalline.png")
    leanrightline = Image.open("leanrightline.png")
    leanleftline = leanrightline.transpose(Image.FLIP_LEFT_RIGHT)
    leanrightfuxian = Image.open("leanrightfuxian.png")
    leanleftfuxion = leanrightfuxian.transpose(Image.FLIP_LEFT_RIGHT)
    if num1 and num2 and num3 :
        lianxian.append("一二三连线")
        background.paste(horizontalline, (85,55), mask = horizontalline)
    if num4  and num5  and num6 :
        lianxian.append("四五六连线")
        background.paste(horizontalline, (350,55), mask = horizontalline)
    if num7  and num8  and num9 :
        lianxian.append("七八九连线")
        background.paste(horizontalline, (610,55), mask = horizontalline)
    if num1  and num4  and num7 :
        lianxian.append("一四七连线")
        background.paste(verticalline, (40,80), mask = verticalline)
    if num2  and num5  and num8 :
        lianxian.append("二五八连线")
        background.paste(verticalline, (40,350), mask = verticalline)
    if num3  and num6  and num9 :
        lianxian.append("三六九连线")
        background.paste(verticalline, (40,600), mask = verticalline)
    if num1  and num5  and num9 :
        lianxian.append("一五九连线")
        background.paste(leanleftline, (50,50), mask = leanleftline)
    if num3  and num5  and num7 :
        lianxian.append("三五七连线")
        background.paste(leanrightline, (50,50), mask = leanrightline)
    if num2  and num4:
        lianxian.append("二四辅线")
        background.paste(leanrightfuxian, (90,90), mask = leanrightfuxian)
    if num6  and num8:
        lianxian.append("六八辅线")
        background.paste(leanrightfuxian, (360,360), mask = leanrightfuxian)
    if num4  and num8:
        lianxian.append("四八辅线")
        background.paste(leanleftfuxion, (360,90), mask = leanleftfuxion)
    if num2  and num6:
        lianxian.append("二六辅线")
        background.paste(leanleftfuxion, (90,360), mask = leanleftfuxion)
    #display image

    st.image(background)
    from io import BytesIO
    buf = BytesIO()
    background.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
    label="下载",
    data=byte_im,
    file_name=f"命盘{bdayyear}{bdaymonth}{bdayday}.png",
    mime="image/png",
    icon=":material/download:",
)
    st.divider()
    st.text("连线列表：")
    st.header(str(lianxian).replace("[","").replace("]","").replace("'",""))
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="数字1的个数", value=num1)
        st.metric(label="数字2的个数", value=num2)
        st.metric(label="数字3的个数", value=num3)
    with col2:
        st.metric(label="数字4的个数", value=num4)
        st.metric(label="数字5的个数", value=num5)
        st.metric(label="数字6的个数", value=num6)
    with col3:
        st.metric(label="数字7的个数", value=num7)
        st.metric(label="数字8的个数", value=num8)
        st.metric(label="数字9的个数", value=num9)
