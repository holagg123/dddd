import numpy as np
import pandas as pd
import streamlit as st

st.title("習近平的蜜汁沼澤")
ascii_art = """
⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠄⠄⠄______ ⠄ ⠄⠈⡀⠭⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿
⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻
"""
st.code(ascii_art)
arry1=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
st.write(arry1)
arry2=pd.DataFrame([[12,56,78], [45, 67, 89], [23, 34, 45]], columns=['A', 'B', 'C'], index=['a', 'b', 'c'])
st.write(arry2)

C1=st.checkbox("遠")
if C1:
    st.info("習遠平")
else:
    st.info("習近平")

c3=st.columns(3)
txt=" "
with c3[0]:
    r11=st.checkbox("A")
    if r11:
        txt+="平近"
with c3[1]:
    r12=st.checkbox("B")
    if r12:
        txt+="MD"
with c3[2]:
    r13=st.checkbox("C")
    if r13:
        txt+="平"
st.info(txt)

st.write("## 果汁")
b1=st.radio("選擇果汁", ["蘋果汁", "橙汁", "葡萄汁"])
st.info(b1)

b2=st.radio("選擇果汁", ["蘋果汁", "橙汁", "葡萄汁"], index=1)
st.info(b2)

st.write("## 甜度")
n1=st.slider("選擇甜度", 1.0, 10.0, 5.0, step=0.5)
st.info(n1)

st.sidebar.write("## 下拉選單")
city=st.sidebar.selectbox("選擇城市", ["北京", "上海", "廣州", "深圳"])
if city == "北京":
    st.sidebar.info("你選擇了北京")
elif city == "上海":
    st.sidebar.info("你選擇了上海")
elif city == "廣州":
    st.sidebar.info("你選擇了廣州")
elif city == "深圳":
    st.sidebar.info("你選擇了深圳")
else:
    st.info("你沒有選擇")

st.write("加法")
a=st.number_input("輸入第一個數字", value=0)
b=st.number_input("輸入第二個數字", value=0)
if st.button("計算"):
    st.write("### ",a+b)