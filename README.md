# Kamehameha Schools (Applications Engineer) | Take Home Assignment

Please read the following instructions carefully. 

Please fork this repo, complete the assignment, and once you are finished, send a link to your repo to: @Kabui2021

## Getting Started

1. Fork this repo.

![fork_repo](https://user-images.githubusercontent.com/45079557/160927612-a7fed5a9-55a4-4910-a19d-13d867417084.jpg)

2. Clone your fork to your local machine.

3. Install dependencies using: `pip3 install -r requirements.txt`

4. In the project directory, run `python app.py` to start the Flask application

## Task
Create an API endpoint using the Flask library that calculates the beta for each of the FAANG stocks. The response of the GET request should be formatted similar to JSON response below:

```json
{
    "FB": ...,
    "AAPL": ...,
    "AMZN": ...,
    "NFLX": ...,
    "GOOG": ...
}
```

## Data
You should use daily adjusted close data for your beta calculation. A free data provider that you can use is the yfinance library.

## Tests
Write the appropriate amount of tests to thoroughly cover your endpoint's code.

## Share
Add @Kabui2021 as a contributor to your project when you are finished.

## How your code will be evaluated
Your code will be evaluated on the following criteria:
* Correctness: Is the code completed? Does it function has instructed?
* Quality: Is the code readable and well structured?
* Tests: Do your tests cover the code well?



