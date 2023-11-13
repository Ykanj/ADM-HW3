import pandas as pd
import re
import time
from tqdm import tqdm
from currency_converter import CurrencyConverter
c = CurrencyConverter()

# we import in our dataframe and drop the first column which excel converts into an index column (giving us 2)
degrees = pd.read_csv(r"C:\Users\youse\Desktop\ADM Hw3\Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

# we create a column for our new corrected fee which we will report in euros 
degrees["corrected fee (EUR)"] = ""

# we write a function to find values in our fees column, we used regex to find any currency symbol if followed by digits,
# or any digit, or any sequence of digits from the first comma to the first decimal, or just until the first decimal. we
# then stripped and replaced all symbols and punctuation with blank spaces to process, I also checked whether the value we 
# is equal to 2023 2024 2025 whcich are present in some cells as years. If the cell asks to consult the website for info, or
# if no digits are found in the string, or if the value reported is less than 50 (which is usually a mistake and not actually a fee), 
# i returned 0, otherwise I found specific refrences to each currency used in the database and converted based on that, otherwise the 
# fee was reported in euros and kept as is. For the conversion I used a library called currency_converter which takes daily uptdated rates
# from the European Central Bank. 
def currency_format(text, country):
    text = str(text)
    print(text)
    if "Please see the university website for further information on fees for this course." in text or text == "" or text == "nan" or text is None:
        return 0.0
    else:
        numbers = re.findall(r"(?:[£$€]\s*)?\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?", text)
        numbers = [float(number.replace(",", "").replace("£", "").replace("$", "").replace("€", "").replace(".", "")) for number in numbers if number not in ["2023", "2024", "2025"]]
        amount = max(numbers) if numbers else None

        if amount is None:
            return 0.0
        else:
            if amount < 10:
                return None     
            if "SEK" in text:
                fee = c.convert(amount, "SEK", "EUR")
            elif "CZK" in text:
                fee = c.convert(amount, "CZK", "EUR")
            elif "HK" in text:
                fee = c.convert(amount, "HKD", "EUR")
            elif "USD" in text:
                fee = c.convert(amount, "USD", "EUR")
            elif "JPY" in text:
                fee = c.convert(amount, "JPY", "EUR")
            elif country == "United Kingdom":
                fee = c.convert(amount, "GBP", "EUR")
            else:
                fee = amount
            print(int(fee))
            if int(fee) < 50:
                return 0.0
            else:
                # there are cases where €30.000,00 was read as 300000 instead of 30000, considering that no fee would ever reach above
                # €200000, in case it reached above, it was divided by 10
                if fee > 200000:
                    return (round(fee, 1)/10)
                else: 
                    return round(fee, 1)

for i in tqdm(range(len(degrees))):
    degrees.loc[i, "corrected fee (EUR)"] = currency_format(degrees.loc[i, "fees"], degrees.loc[i, "country"])

degrees.to_csv(r"c:\Users\youse\Desktop\ADM Hw3\Parsed_database.csv")

