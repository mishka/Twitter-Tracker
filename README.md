# Twitter-Tracker
Tracks a private user's basic activity without using the Twitter API to receive notifications through Telegram.

# Dependencies
 - [requests](https://github.com/psf/requests)
 - [twitter-scraper](https://github.com/bisguzar/twitter-scraper)

# How to set it up
Edit the `CHAT_ID`, `USERNAME`, `USERID`, `TOKEN` variables accordingly.

## Creating a telegram bot
You can create a bot through [@BotFather](https://telegram.me/BotFather)

## Finding the chat ID
You can learn about your chat ID by messaging `/my_id` to the [@get_id_bot](https://telegram.me/get_id_bot) on telegram.

# Things to do
- [x] Create the `db.json` file automatically if it doesn't exist.
- [x] Use the `user ID` instead of the `username` so even if the user changes it's username, it will still be possible to track them.
- [ ] Log the activities with timestamps in a csv file so it can be used for analysis purposes later.
