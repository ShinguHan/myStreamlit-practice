import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="PuKu Jaja")

with st.form("Scrapper"):
    st.markdown("<h1 style = 'text-aligh:center;'>Web Scrapper</h1>", unsafe_allow_html=True)
    keyword=st.text_input('Search')
    # st.image("https://images.unsplash.com/photo-1561567131-f7d83083aee0")
    search = st.form_submit_button("Search")

placeholder = st.empty()
if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content,'html.parser')
    rows = soup.find_all("div", class_='ripi6')
    col1, col2 = placeholder.columns(2)

    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        # print(len(figures))
        for i in range(2):
            img = figures[i].find("img", class_='tB6UZ a5VGX')
            anchor = figures[i].find("a", class_="rEAWd")
            if i == 0:
               col1.image(img["srcset"].split('?')[0])
               btn = col1.button("Download",key=str(index)+str(i))
               if btn:
                   
                   url = "https://unsplash.com/s" + anchor["href"]
                   print(url)
                   print("btn pressed")
                #    webbrowser.open_new_tab("https://unsplash.com/s" + anchor["href"])

            else:
               col2.image(img["srcset"].split('?')[0])
               btn = col2.button("Download",key=str(index)+str(i))
               anchor = figures[i].find("a", class_="rEAWd")
            #    if btn:
                #    webbrowser.open_new_tab("https://unsplash.com/s" + anchor["href"])

            
                # print(img.prettify())
                # print(img["srcset"].split('?'))
                # print('\n\n\n')

        # print(soup)
        # st.write(soup)