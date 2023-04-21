import streamlit as st
import joblib
import numpy as np

st.title("Book recommendation system")

images = joblib.load("images.pkl")
similarity_scores = joblib.load("similarity.pkl")
pt = joblib.load("pt.pkl")

def recommend_after(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    recommendations = []
    for i in similar_items:
        recommendations.append(pt.index[i[0]])
    return recommendations

def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

def recommend(str):
    for index,row in pt.iterrows():
        if isSubstring(str.lower(),index.lower()) != -1:
            return recommend_after(index)
    return []


st.header('Find your perfect books ')

book_list = pt.index
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    book_list
)

if st.button('Show Recommendation'):
    recommended_book_names = recommend(selected_book)
    print(recommended_book_names)
    st.text(recommended_book_names[0])
    # st.image(images[recommended_book_names[0]])
    st.text(recommended_book_names[1])
    # st.image(images[recommended_book_names[1]])

    st.text(recommended_book_names[2])
    # st.image(images[recommended_book_names[2]])
    st.text(recommended_book_names[3])
    # st.image(images[recommended_book_names[3]])
    st.text(recommended_book_names[4])
    # st.image(images[recommended_book_names[4]])


