from django.db import models


class Message(models.Model):
    class Meta:
        db_table = 'main_messages'

    message_content = models.TextField(null=False, )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message_content
