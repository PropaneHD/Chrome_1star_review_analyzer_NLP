
# Chrome 1 Star Positive Review Indentifier


Upon uploading a Chrome play store reviews dataset, The app will transform the dataset and 
apply the TextBlob sentiment analysis to find out the reviews that are postive but given 1 Star.

I used to 2 Pre-trained models, TextBlob and VADER. Taking the final dataframe as excel output
to maually check the accuracy of the models by creating a ground truth. By doing this I was able 
to find out that TextBlob did well with the given Data compared to VADER. With the TextBlob 
model I was able to come up with 91% Accurate predictions of  1 Star Positive Review. There is 
still scope for fine tuning the model and data to achieve better results. 

## Demo

Live Link: https://chrome-1star-review-analyzer.herokuapp.com/
## Deployment

This project was deployed on Heroku (PAAS). The project can files can uploaded using the Github 
repository link or using the Heroku CLI. [Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) for the Deployment.


For running it in local machine use this code. 
```bash
  streamlit run "projectdirectory/WebApp.py"
```


## Installation

The project was made with Python Jupyter notebook. All the packages required to run the app 
can be install typing the following command. 

```bash
  pip install -r requirements.txt
```
    
