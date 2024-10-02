# Instagram Followers Bot

This project is a Selenium-based bot designed to automate the process of following Instagram users from a specific account, with the hope of gaining follow-backs. The bot performs various interactions with the Instagram website, including logging in, searching for a target account, and following users.

## Features

- **Automated Login**: Logs in to Instagram using provided credentials.
- **Cookies and Notifications Management**: Handles cookies and notification prompts during login.
- **Search Similar Account**: Navigates to a specified account's followers list.
- **Automated Following**: Follows users from the selected account, up to a defined threshold to avoid detection.

## Technologies Used

- **Python**: Main programming language for building the bot.
- **Selenium**: Used to automate browser interactions.

## Getting Started

### Prerequisites

- **Python 3.6+**: Make sure you have Python installed.
- **Chrome Browser**: This project uses Google Chrome for automation.
- **ChromeDriver**: Ensure you have the correct version of ChromeDriver installed for your Chrome version.
- **Instagram Account**: You need an Instagram account to use this bot.
- **Selenium**: Install Selenium using pip:

  ```bash
  pip install selenium


## Code Overview
	•	InstagramBot Class: Handles the entire process from logging in, searching for followers, and following users.
	•	login_to_ig(): Logs in to Instagram, handles cookies and notification prompts.
	•	find_followers(): Navigates to the followers list of the target account.
	•	follow(): Iterates through the followers list and follows users up to a defined threshold.
	•	close_driver(): Closes the Chrome browser after the process is completed.

 ## Lessons Learned
 	•	Practiced using Selenium for browser automation and web scraping.
	•	Improved skills in handling various dynamic elements on a webpage using explicit waits.
	•	Learned techniques to avoid bot detection, such as slowing down password entry and limiting the number of actions.

 ## Future Improvements
 	•	Add functionality to unfollow accounts after a certain period if they don’t follow back.
	•	Implement more sophisticated detection avoidance mechanisms, such as randomized time delays and more diverse interactions.
	•	Introduce error handling for unexpected pop-ups and edge cases.
