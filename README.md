# League of Item Sets

What is this?
--
This our (Jonas Sandbekk and Ole Harbosen) attempt at the [RIOT API 2.0 Challenge](https://developer.riotgames.com/discussion/announcements/show/2lxEyIcE).
It is a website built with a python and django backend. On this website you can choose a champion and build an item set for that champion. If you want you can then download the item set to use it in-game.

Where can I use the site?
--
The site is currently not being hosted anywhere as we never got that far, but you can download the repo and run it yourself if you want to. The requirments are Python 3.4+ and Django 1.8+. From there on you need a "settings" file in the main folder containing the text "_API_KEY: \<your api key here\>_" and "_SECRET_KEY: \<a secret key for django here\>_" .Then you need to setup the database with "_manage.py migrate_". You can then run main.py which will download the required files and update the database for you and the site is ready for use. Test it by running "_manage.py runserver_" and go to localhost:8000

Why is it not the most beautiful creation known to mankind?
--
Unfortunately neither of us had any experience with HTML, CSS or Javascript before and little to no experience with Django so we had to learn a lot of things to make the site. Which is fun and rewarding, but means that a lot of time goes to making the site work as intended rather than making it look beautiful. Coupled with the lack of time we already had the sites looks suffered in the process.
