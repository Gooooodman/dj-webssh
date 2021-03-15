'''
@project : gops
@author  : lupuxiao
@contact : jiucows@gmail.com
@file    : channel.py
@time    : 2021-03-14 17:41:51
'''

# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import uuid

layer = get_channel_layer()


class Channel:
    @staticmethod
    def get_token():
        # return uuid.uuid4().hex
        return  "123a"
    @staticmethod
    def send_ssh_executor(hostname, port, username, command, token=None):
        message = {
            'type': 'exec',
            'token': token,
            'hostname': hostname,
            'port': port,
            'username': username,
            'command': command
        }
        async_to_sync(layer.send)('ssh_exec', message)