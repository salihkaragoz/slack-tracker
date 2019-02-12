from slacker import Slacker

class SlackChannelSender():
    """Custom class that posts to Slack while training a neural network"""

    def __init__(self, channel, token, private=False):
        # Channel --> Channel name
        # token   --> Slack API token
        self.channel = channel
        self.slack = Slacker(token)

        if (self.slack.api.test().successful):
            print("Successfully connected to " + self.slack.team.info().body['team']['name'])
        else:
            print('Try Again!, Check your API TOKEN')

        channel_list = [c['name'] for c in self.slack.channels.list().body['channels']]
        group_list = [c['name'] for c in self.slack.groups.list().body['groups']]
        #if (channel in channel_list or channel in group_list):
        if (any(s.lower() == channel.lower() for s in channel_list) or any(x.lower() == channel.lower() for x in group_list)):
            print ('The Channel exist, the outputs will be overwrite!')
        else:
            print ('The ' + channel + ' will create. ')
            if private:
                self.slack.groups.create(channel)
            else:
                self.slack.channels.create(channel)
        #assert channel not in channel_list, 'The channel name exist, take the different one'
        #assert channel not in group_list, 'The channel name exist, take the different one'

    def send_to_channel(self,text):
        """Report training stats"""
        r = self.slack.chat.post_message(channel=self.channel, text=text,
	                        username='Training Report',
	                        icon_emoji=':clipboard:')
