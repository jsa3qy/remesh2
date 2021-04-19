from django.db import models
import uuid

# Conversations point to messages, messages point to thoughts
# Thoughts belong to exactly one message and each messages belongs to exactly one conversation
# If we delete a parent we will delete all 'children' and 'grandchildren' -- i.e. if we delete a Conversation
#   then we will delete all messages associated with that conversation, and all thoughts associated with each of those
#   messages respectively

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Conversation: ' + self.title

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE) 

    def __str__(self):
        return 'Message: ' + self.title

class Thought(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'Thought: ' + self.text   

