# Twitter-Tracker
Tracks a private user's basic activity without using the Twitter API to receive notifications through Telegram.

# Requirements
 - [requests](https://github.com/psf/requests)
 - [twitter-scraper](https://github.com/bisguzar/twitter-scraper)

# How to set it up
Edit the `CHAT_ID`, `USERNAME, USERID`, `TOKEN` variables accordingly.


# Things to do
- [x] Create the `db.json` file automatically if it doesn't exist.
- [ ] Use the `user ID` instead of the `username` so even if the user changes it's username, it will still be possible to track them.
- [ ] Log the activities with timestamps in a csv file so it can be used for analysis purposes later.
