## Logging

### LOG LEVELS (CATEGORIES)
DEBUG 1
INFO 2
WARNING 3
ERROR 4
CRITICAL 5

### Loggers
logger help you to pick up a message from your code (input)

### Handlers
Handlers decide where to display that information from the logger,
sometimes it also decides how the information is displayed (output)

- Terminal
- File
- Email
- 3rd Party Api (sentry, aws, googlecloud)

### How to Setup Loggers and Handlers
- we need to work on our django settings file
- add A LOGGING constant

### how to use loggers in our code
- import logging
- search for the logger 
- then use the logger

### Formatters
they simply just help you display your message in a nicer way or with a better format