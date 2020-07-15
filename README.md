# Twitter-Tracker
Tracks a private user's basic activity without using the Twitter API to receive notifications through Telegram.

# Dependencies
 - [requests](https://github.com/psf/requests)
 - [twitter-scraper](https://github.com/bisguzar/twitter-scraper)  
   
 Notes about `twitter-scraper`; the pip package seems outdated as of 17/06/2020, so please do a manual installation from the github repo for the time being.

# How to set it up
## Variables
Edit the `CHAT_ID`, `USERNAME`, `USERID`, `TOKEN` variables accordingly.  
  
If you want to use the `USERID` instead of using the `USERNAME`, please only provide the `USERID`.

## Creating a telegram bot
You can create a bot through [@BotFather](https://telegram.me/BotFather)

## Finding the chat ID
You can learn about your chat ID by messaging `/my_id` to the [@get_id_bot](https://telegram.me/get_id_bot) on telegram.

# Things to do
- [ ] Log the activities with timestamps in a csv file so it can be used for analysis purposes later.
