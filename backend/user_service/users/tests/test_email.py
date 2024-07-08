from django.test import TestCase
from django.core import mail
from unittest import mock
from ..tasks import send_email


class EmailTest(TestCase):
    @mock.patch('users.tasks.send_mail')
    def test_send_email_task(self, mock_send_mail):
        send_email('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'])

        mock_send_mail.assert_called_once_with(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
        )
