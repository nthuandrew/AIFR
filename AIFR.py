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

Titles = excel_data_df1['Title'][:].tolist()
TextIDs = excel_data_df1['TextID'][:].tolist()
TextTimes = excel_data_df1['TextTime'][:].tolist()
Authors = excel_data_df1['Author'][:].tolist()


original_contents = excel_data_df1['Content(remove_tag)'][:].tolist()


sentences = excel_data_df2['Sentence'][:].tolist()
labels = excel_data_df2['標註代碼'][:].tolist()


st.title("AIFR demo")

article = st.selectbox('Choose an article', Titles)

key_i = Titles.index(article)

global_stastic = [0]*7

with st.sidebar:
    title = "文章標題: " + Titles[key_i]
    textid = "文章ID: " + str(TextIDs[key_i])
    texttime = "發佈時間: " + str(TextTimes[key_i])
    author = "文章作者: " + Authors[key_i]
    st.header(title)
    st.markdown(textid)
    st.markdown(texttime)
    st.markdown(author)
    to_show = st.checkbox('是否呈現標註結果分類文字')
    st.subheader("標註分類與統計： ")
    container_total = st.container()
    for i in range(7):
        if i == 0:
            container0 = st.container()
        elif i == 1:
            container1 = st.container()
        elif i == 2:
            container2 = st.container()
        elif i == 3:
            container3 = st.container()
        elif i == 4:
            container4 = st.container() 
        elif i == 5:
            container5 = st.container()
        else:
            container6 = st.container()
            for j in range(3):
                st.markdown("\n")         

col2, col1 = st.columns([30, 40])
with col1:
    st.header("Content")
    st.markdown(original_contents[key_i])

with col2:
    st.header("Labeled Sentences")
    New_titles = excel_data_df2['Title'][:].tolist()
    # print(len(New_titles), New_titles[:10])
    now_title_id = New_titles.index(article)
    now_title_end = now_title_id
    for single_title in New_titles[now_title_id:]:
        if single_title == article:
            now_title_end += 1
        else:
            break
    now_sentences = sentences[now_title_id:now_title_end]
    now_labels = labels[now_title_id:now_title_end]
    # print(len(now_sentences))
    tem_stastic = [0]*7
    for i in range(len(now_sentences)):
        lab = now_labels[i]
        sen = str(now_sentences[i])
        if lab == 0 or lab == 7:
            s = "<div><span class='highlight zero'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("無標註")
            tem_stastic[6] += 1 
        elif lab == 1:
            s = "<div><span class='highlight one'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("自殺與憂鬱(認知或情緒)")
            tem_stastic[1] += 1  
        elif lab == 2:
            s = "<div><span class='highlight two'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("無助或無望(認知或情緒)")
            tem_stastic[2] += 1
        elif lab == 3:
            s = "<div><span class='highlight three'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("正向文字(認知或情緒)")
            tem_stastic[3] += 1 
        elif lab == 4:
            s = "<div><span class='highlight four'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("其他負向文字(情緒)")
            tem_stastic[4] += 1
        elif lab == 5:
            s = "<div><span class='highlight five'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:            
                st.caption("生理反應或醫療狀況(認知或行為)") 
            tem_stastic[5] += 1
        elif lab == 6:
            s = "<div><span class='highlight six'>" + sen + "</span></div>"
            st.markdown(s, unsafe_allow_html=1)
            if to_show:
                st.caption("自殺行為(行為)")
            tem_stastic[0] += 1
    s0 = "<span class='highlight six'>" + "自殺行為(行為)‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[0]) + "</span>" + "句</span></div>"
    s1 = "<span class='highlight one'>" + "自殺與憂鬱(認知或情緒)‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[1]) + "</span>" + "句</span></div>"    
    s2 = "<span class='highlight two'>" + "無助或無望(認知或情緒)‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[2]) + "</span>" + "句</span></div>"
    s3 = "<span class='highlight three'>" + "正向文字(認知或情緒)‧‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[3]) + "</span>" + "句</span></div>"
    s4 = "<span class='highlight four'>" + "其他負向文字(情緒)‧‧‧‧‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[4]) + "</span>" + "句</span></div>"
    s5 = "<span class='highlight five'>" + "生理反應或醫療狀況(認知或行為)‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[5]) + "</span>" + "句</span></div>"
    s6 = "<span class='highlight zero'>" + "無標註‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧‧" + "<span class='highlight bold'>" + str(tem_stastic[6]) + "</span>" + "句</span></div>"
    total = str(sum(tem_stastic))
    s_total = "總句數： " + total + "句"
    container_total.text(s_total)
    container0.caption(s0, unsafe_allow_html=1)
    container1.caption(s1, unsafe_allow_html=1)
    container2.caption(s2, unsafe_allow_html=1)
    container3.caption(s3, unsafe_allow_html=1)
    container4.caption(s4, unsafe_allow_html=1)
    container5.caption(s5, unsafe_allow_html=1)
    container6.caption(s6, unsafe_allow_html=1)
