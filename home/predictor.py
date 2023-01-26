import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class Predictor:
    def __init__(self):
        urls_data = pd.read_csv("urldata.csv")
        
        url_list = urls_data["url"]
        y = urls_data["label"]

        self.Vectorizer = TfidfVectorizer()
        X = self.Vectorizer.fit_transform(url_list)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)	
        self.Logit = LogisticRegression()
        self.Logit.fit(X_train, y_train)
        
        
        
        test_pred = ["google.com/search=jcharistech",
                    "google.com/search=faizanahmad",
                    "pakistanifacebookforever.com/getpassword.php/", 
                    "www.radsport-voggel.de/wp-admin/includes/log.exe", 
                    "ahrenhei.without-transfer.ru/nethost.exe ",
                    "www.itidea.it/centroesteticosothys/img/_notes/gum.exe"]
        test_pred = self.Vectorizer.transform(test_pred)
        test_pred_res = self.Logit.predict(test_pred)
        

        print('\n\n\nhtpekmnfn j,exfkrb ', test_pred_res, '\n\n\n')


        
        
    def predict_url(self, *urls):
        X_predict = self.Vectorizer.transform(urls)
        New_predict = self.Logit.predict(X_predict)
        return New_predict



