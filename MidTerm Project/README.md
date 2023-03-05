# Real Time Import for Exchange Rate and Plot

This project aims to visusalize the exchange rates in real time.
In this project we're using Alpha Vantage API inorder to import the real time recurring exchange rate date for CAD to INR.

We're using requests libraries HTTPS GET menthod inorder ot fetch the data from the alha vantage endpoint API.
This requests is being authorized through an API Key. 

Please Note : For this project we're using a free version of API keys which might expire after certain number of GET requests.

Project Structure:
    MidTerm Project \
                    import_and_plot_exchange_rate.py 
                    Real Time Graph \
                                     Exchange_rate_plot_recording.gif


The source code for fetching and plotting the sxchangge rate is present in => import_and_plot_exchange_rate.py
The recordign for a real time plot can be found in => Real Time Graph \ Exchange_rate_plot_recording.gif


Standalone test run for fetching the exchange rate data can be found here in Jupyter Notebook : Test_Aplha_Vantage_API_Response.ipynb



Tech Stack Used:
    Python3
    Libraries Used :
        Requests 
        Matplotlib
        datetime
        Matplotlib.Animation
        Pandas


Contributors : 
- Abbas Ismail
- Megha Chauhan
- Karthi Kuthalingam
- Gitik Kaushik
- Enrique Gonzalez Zepeda
