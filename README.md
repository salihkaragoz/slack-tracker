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

channel_name = 'test'  # new or existing channel
token = 'xar31trtejl45lsdjf123u9asdns' # example

slack = SlackChannelSender(channel_name, token)
slack.send_to_channel(text)  #print to channel
```

