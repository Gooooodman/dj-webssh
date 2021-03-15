from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from libs.channel import Channel
from apps.host.models import Host
import json


# def do_task(request):
#     token = Channel.get_token()
#     Channel.send_ssh_executor(
#             token=token,
#             hostname="10.2.30.37",
#             port=22,
#             username="10.2.30.37",
#             command="echo 123 > /tmp/1.txt"
#         )
#     print("do_task------------------------")
#     return HttpResponse(json.dumps(token), content_type='application/json')


def host(request):
    return render(request, "ssh.html")