#Machine Learning Web App
##Team: Standalone by Muhammad Trad

### Application Structure
1. Simple application using machine learning to predict whether a youtube comment is spam or not.
2. Application Model: 
- sign up is required to access the prediction functionality and feature
- in order to perform a prediction, upfront payment is required by credit card
- for testing: enter 4242 4242 4242 4242 as card number. Enter any future exp date. Enter any 3-digit CVC. 
3. Application Configuration:
- App is based on flask authorization engine. 
- Payments are linked to stripe test functionality
5. Application run in local environment by  
cd mubilize-midterm-master  
pip install -r requirements.txt  
python app.py  
```
open with local address http://127.0.0.1:5000
