#importing Releveant Libraries

import pandas as pd
import numpy as np
import re
from textblob import TextBlob
import streamlit as st
from PIL import Image


def finalfile(input_data):
    #importing the data
    
    raw_data = input_data
    raw_data = raw_data.loc[raw_data['Star']==1]
    raw_data.reset_index(drop = True,inplace = True)

    #preprocessing the data
    remove_caps = re.compile(r'[\W]')
    remove_special = re.compile(r'[^a-z0-9\s]')

    def normalizedtexts(text):
        cleanedtext = []
        for i in range(len(text)):
            lower = text[i].lower()
            no_caps = remove_caps.sub(r' ',lower)
            no_special = remove_special.sub(r' ',no_caps)
            cleanedtext.append(no_special) 
        return cleanedtext

    #Adding the Cleaned text to DataFrame

    raw_data['Cleaned Text'] = normalizedtexts(raw_data['Text'])

    #Creating Texblob function for Sentiment Analysis

    polar = []
    subject = []

    def textblobSIA(data_column):

        for i in range(len(data_column)):
            obj = TextBlob(data_column[i])
            sentiment = obj.sentiment
            polar.append(sentiment[0])
            subject.append(sentiment[1])

    #Adding the Polarity and Subjectivity to DataFrame
    textblobSIA(raw_data['Cleaned Text'])
    raw_data['Text_Polarity'] = polar
    raw_data['Text_Subjectivity'] = subject

    #Creating A final DataFrame Containing Positive Reviews with 1 Star Rating 
    final_df = raw_data[['Review URL', 'Star', 'Cleaned Text', 'Text_Polarity','Text_Subjectivity']]
    final_df = final_df.loc[final_df['Text_Polarity'] > 0.5]
    final_df.reset_index(drop = True,inplace = True)
        
    
    return final_df


def main():
    
    # Title of the Page
    st.title('Chrome 1 Star Review Analyzer')
    
    #Addding Image for reference
    st.subheader('Upload CSV File with matching columns')
    image = Image.open('C:/Users/Vijay Ganesh/Desktop/NextGrowth_Labs/DF_Columns.jpg')
    st.image(image, caption='DataFrame Columns Sample')
    
    #Adding the Upload button
    data_file = st.file_uploader("Upload the Review Dataset")
    if data_file is not None:
        dataframe = pd.read_csv(data_file)
        Analyzed = finalfile(dataframe)
    
        st.dataframe(Analyzed, 1000, 300)
    
        #Adding the download button
        csv = Analyzed.to_csv().encode('utf-8')
        st.download_button(label="Download the CSV",data=csv,file_name='Analyzed Chrome Reviews.csv',mime='text/csv')
    
    
if __name__ == '__main__':
    main()