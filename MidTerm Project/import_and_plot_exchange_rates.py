import requests
import pandas as pd

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

START = 0

def get_currency_exchange_rate(from_currency : str, to_currency : str) -> float:

  API_KEY = "YSGOXVK6P42SHUEP"

  request_url =  f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&interval=5min&apikey=YSGOXVK6P42SHUEP'

  api_response = requests.get(request_url)

  api_resp_json = api_response.json()

  return api_resp_json



# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    # time.sleep(10)
    # exchange_rate_response = float(get_currency_exchange_rate(from_currency="CAD", 
    #                                     to_currency="INR"
    #                                     )['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    time.sleep(4)
    exchange_rate_response = 60 + random.random() / 7

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(exchange_rate_response)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]



    #Moving Averages Calculations
    moving_averages = []
  
    # Insert first exponential average in the list
    moving_averages.append(ys[0])

    x = 0.9
  
    i_ = 0

    # Loop through the array elements
    while i_ < len(ys):
      
        # Calculate the exponential
        # average by using the formula
        window_average = round((x*ys[i_])+
                              (1-x)*moving_averages[-1], 2)
          
        # Store the cumulative average
        # of current window in moving average list
        moving_averages.append(window_average)
          
        # Shift window to right by one position
        i_ += 1

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    print(moving_averages)

    ax.plot(xs, moving_averages[:len(xs)])

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('CAD v/s INR exchange rate over Time')
    plt.ylabel('CAD TO INR')



def main():
    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)

    plt.show()



if __name__ == '__main__':
   
   main()
   