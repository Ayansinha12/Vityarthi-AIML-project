overview

This script is an interactive Stock Price Prediction and Visualization Tool. It uses machine learning—specifically, Polynomial Regression—to model historical stock prices over time. By converting calendar dates into numerical values (ordinals), the script trains a model

Features

 Historical Data Preprocessing: Automatically reads the CSV dataset, handles chronological sorting, and converts standard calendar dates into mathematical ordinal values so they can be processed by the machine learning algorithm.

Non-Linear Trend Modeling: Uses Polynomial Regression (currently set to a 4th degree) instead of simple linear regression. This allows the model to curve and better capture the natural "zig-zag" fluctuations of the stock market.

Interactive User Input: Prompts the user in real-time to specify a target date of interest and a custom time window (number of days to look forward and backward).

Dynamic Data Slicing: Automatically filters the massive dataset down to the specific time range requested by the user, ensuring the resulting chart is focused and easy to read.

Comparative Visualization: Generates a dual-line graph plotting the actual historical closing prices (solid line with dots) against the model's predicted trajectory (dashed line with 'x' marks).

Targeted Point Annotation: Specifically zeroes in on the exact date the user requested, enlarging those data points on the graph and appending text labels with the exact numeric values for both the actual and predicted prices. 

Technologies Used


Python (3.x): The core programming language powering the script.

Pandas (pd): The primary data manipulation library. In this code, it is responsible for:

Reading the CSV file (pd.read_stock_data_2020_2025).

Converting strings into datetime objects (pd.to_datetime).

Mapping dates to numerical ordinals (pd.Timestamp.toordinal).

Calculating date ranges using time math (pd.Timedelta).

Filtering the dataset based on the user's date constraints.

NumPy (np): The fundamental package for scientific computing in Python. While not explicitly called for mathematical functions in this specific script, it operates under the hood alongside Pandas and Scikit-Learn to handle the arrays and matrix transformations.

Scikit-Learn (sklearn): The machine learning framework used to generate the predictions.

PolynomialFeatures: Transforms the single "Date" feature into multiple polynomial features (squaring, cubing, etc.), which allows the model to map curved trends.

LinearRegression: The algorithm that calculates the line of best fit through those newly generated polynomial features.

Matplotlib (plt): The 2D plotting library used to create the final visual output. It handles:

Drawing the standard line charts (plt.plot).

Placing the enlarged specific markers (plt.scatter).

Adding the specific price numbers next to the markers (plt.text).

Formatting the chart with labels, a title, a legend, and a grid.instruction of testing

installation & setup

1. Install Python
Ensure you have Python 3 installed on your system. You can verify this by opening your terminal or command prompt and typing:

Bash
python (3.x)
2. Install Required Libraries
You need to install the external dependencies using pip. Run the following command in your terminal:

Bash
pip install pandas numpy matplotlib scikit-learn
3. Prepare Your Dataset
Ensure you have your dataset named exactly stock_data_2000_2025.csv.

Place this CSV file in the exact same folder as your Python script.

The CSV must contain at least two column headers exactly as written: Date and Close.

Running the Project
Save your Python code into a file.

Open your terminal or command prompt and navigate to the folder containing your script and CSV file.

Execute the script by running.



Quick Test
Run your script in the terminal.

When prompted for a date, type a date that you know exists in your dataset using the exact format requested.

Verify the Output: A graph should immediately pop up displaying a 60-day window around your chosen date. Check that your specific date is clearly marked with a large dot for the actual price, an 'X' for the predicted price, and that the exact dollar amounts are written next to them
