medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv')
import pandas as pd

medical_df = pd.read_csv('medical.csv')
print(medical_df)

You're getting the urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)> error because your Python installation is having trouble verifying the SSL certificate of the GitHub server. This is a common issue when dealing with HTTPS connections. [1]

Here's how to fix it:

1. Update Your requests Library:

The requests library is often used for making HTTP requests in Python. It's possible that an outdated version of requests is causing the issue.
Solution: Update requests using pip:
pip install --upgrade requests
2. Update Your urllib3 Library:

The urllib3 library is used by requests and other libraries for handling HTTPS connections.
Solution: Update urllib3 using pip:
pip install --upgrade urllib3
3. Verify Your System's Date and Time:

Incorrect system date and time settings can sometimes cause SSL certificate verification issues.
Solution: Make sure your system's date and time are set correctly. You can use the date and time commands in your terminal to check and adjust them.
4. Install certifi:

The certifi package provides a bundle of trusted certificates that Python can use to verify SSL connections.
Solution: Install certifi using pip:
pip install certifi
5. Disable SSL Verification (Not Recommended):

Warning: This is a security risk and should only be used as a last resort.
Solution: You can temporarily disable SSL verification by setting the verify parameter to False in your urlretrieve call:
from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv', verify=False)
Important Note: Disabling SSL verification is not recommended as it can expose you to security vulnerabilities. It's best to try the other solutions first.

If none of these solutions work, you might need to:

Check your internet connection: Make sure you have a stable internet connection.
Contact your network administrator: If you're behind a firewall or proxy, you might need to configure them to allow HTTPS connections.
Let me know if you have any more questions or if you're still encountering issues. I'm here to help!

Rate this answer: 
Sources
https://community.plotly.com/t/ssl-certificate-issue-in-dash-tutorial/42819
Context Sources (1 file)