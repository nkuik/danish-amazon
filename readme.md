[![Build Status](https://travis-ci.org/nkuik/danish-amazon.png?branch=master)](https://travis-ci.org/nkuik/danish-amazon)
[![codecov](https://codecov.io/gh/nkuik/danish-amazon/branch/master/graph/badge.svg)](https://codecov.io/gh/nkuik/danish-amazon)

# Danish Amazon

Since Amazon doesn't exist in Denmark, but I want to have things delivered to my home, I have built a little slackbot that takes search criteria, lists results, and gives the option to add an item to a shopping list.

## Todo

- [X] Get sanic running
- [X] Fix config load
- [ ] Clean up entry point
- [ ] Deploy app to Kubernetes Engine
- [ ] Create slackbot on Slack
- [ ] Add a command event listener in Slack
- [ ] Create endpoint to receive commands/messages from Slack
- [ ] Fix problem with env variable of config path in docker image
- [X] Automatic tests
- [X] Test coverage
- [X] Add health endpoint
