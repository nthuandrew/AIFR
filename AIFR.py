import re
import time
from collections import Counter
import streamlit as st
from load_css import local_css
import pandas as pd

local_css("style.css")

#wb_origin = openpyxl.load_workbook('A1_二次標註_網路危機訊息標註_1100927_second_labeled.xlsx', data_only=1)
#wb_labeled = openpyxl.load_workbook('網路危機_A1_電腦斷句_討論標註_全_修正完成.xlsx', data_only=1)
excel_data_df1 = pd.read_excel('A1_二次標註_網路危機訊息標註_1100927_second_labeled.xlsx', sheet_name='contents')
excel_data_df2 = pd.read_excel('網路危機_A1_電腦斷句_討論標註_全_修正完成.xlsx', sheet_name='Merged')

#sheet_origin = wb_origin['contents']
#sheet_labeled = wb_labeled['Merged']

# Title = sheet_origin['G'][1].value
# TextID = sheet_origin['B'][1].value
# TextTime = sheet_origin['D'][1].value
# Author = sheet_origin['F'][1].value

Titles = excel_data_df1['Title'][:50].tolist()
TextIDs = excel_data_df1['TextID'][:50].tolist()
TextTimes = excel_data_df1['TextTime'][:50].tolist()
Authors = excel_data_df1['Author'][:50].tolist()


original_contents = excel_data_df1['Content(remove_tag)'][:50].tolist()

#sentences = sheet_labeled['D'][1:50]
#labels = sheet_labeled['H'][1:50]

sentences = excel_data_df2['Sentence'][:50].tolist()
labels = excel_data_df2['標註代碼'][:50].tolist()
# print(type(sentences[2]))
# print(type(labels[2]))


st.title("AIFR demo")

with st.sidebar:
    title = "文章標題: " + Titles[0]
    textid = "文章ID: " + str(TextIDs[0])
    texttime = "發佈時間: " + str(TextTimes[0])
    author = "文章作者: " + Authors[0]
    st.header(title)
    st.markdown(textid)
    st.markdown(texttime)
    st.markdown(author)

col1, col2 = st.columns([20, 30])
with col1:
    st.header("Content")
    st.markdown(original_contents[0])

with col2:
    st.header("The sentence")
    for i in range(len(sentences)):
        lab = labels[i]
        sen = sentences[i]
        if lab == 0 or lab == 7:
            s = "<div><span class='highlight zero'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("無標註")
        elif lab == 1:
            s = "<div><span class='highlight one'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("自殺與憂鬱(認知或情緒)")   
        elif lab == 2:
            s = "<div><span class='highlight two'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("無助或無望(認知或情緒)") 
        elif lab == 3:
            s = "<div><span class='highlight three'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("正向文字(認知或情緒)") 
        elif lab == 4:
            s = "<div><span class='highlight four'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("其他負向文字(情緒)") 
        elif lab == 5:
            s = "<div><span class='highlight five'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("生理反應或醫療狀況(認知或行為)") 
        elif lab == 6:
            s = "<div><span class='highlight six'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            st.caption("自殺行為(行為)") 
        st.caption('\n')

# with col3:
#     st.header("Label")
#     for i in range(len(sentences)):
#         lab = labels[i].value
#         if lab == 0 or lab == 7:
#             st.markdown("無標註")
#         elif lab == 1:
#             st.markdown("自殺與憂鬱(認知或情緒)")   
#         elif lab == 2:
#             st.markdown("無助或無望(認知或情緒)") 
#         elif lab == 3:
#             st.markdown("正向文字(認知或情緒)") 
#         elif lab == 4:
#             st.markdown("其他負向文字(情緒)") 
#         elif lab == 5:
#             st.markdown("生理反應或醫療狀況(認知或行為)") 
#         elif lab == 6:
#             st.markdown("自殺行為(行為)") 
#         st.caption('\n')
