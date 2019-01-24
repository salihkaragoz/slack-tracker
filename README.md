# Deep Learning Experiment Tracker via Slack
A tool for tracking Deep Learning experiments via slack. You can use ``` send_to_channel() ``` method instead of print function in your code.

## Installation

``` 
git clone https://github.com/salihkaragoz/slack-tracker
python setup.py install
```

## Usage

### Get a legacy slack-API token
Get a legacy token for the desired workspace
https://api.slack.com/custom-integrations/legacy-tokens

### 

```python
from slacktracker.slacktracker import SlackChannelSender

channel_name = 'deep-experimets'  # new or existing channel
token = 'xoxp-183066818163-425116505590-531904887203-9a3c8cc3ddaed44b0f318d2d4d4' # example

slack = SlackChannelSender(channel_name, token, private=True) # This will create a channel automatically.
slack.send_to_channel(text)  #print to channel


```
![Output](https://github.com/salihkaragoz/slack-tracker/blob/master/report.png)


