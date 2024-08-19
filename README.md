This is a Udemy project on using Selenium for scripting and web scraping

The goal of this project is to increase the accounts you follow, in hopes that they will follow you back.

The steps to do this are as follows:
1. Establish your driver (launch IG)
2. Decline any cookies. Make sure to use explicit wait as this sometimes takes a while!
3. Log in to your IG account. Make sure to type the password slowly to prevent triggering bot detection.
4. Click no to the notificaiton request. Again, make sure to use explicit wait as this sometimes takes a while!
5. Launch the new similar accunt. Instead of clicking search (was difficult), just type in the URL and make a GET request
6. Click on the followers
7. Create a list of buttons that you can press. If you already follow the account, skip this button, and go on to the next. Do this for up to X amount of followed accounts.