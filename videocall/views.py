import os
import time
import json
from django.shortcuts import render
from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
import random


# Create your views here.

def video(request, streem_id):
    appID = '0f570de36eb94fb3a437232a08c1b45c'
    appCertificate = '4779da6b7a5f45c985040864a0371fb6'
    channelName = streem_id
    userAccount = streem_id
    uid= random.randint(1000, 5000)
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    # print(currentTimestamp)
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
    # print(privilegeExpiredTs)
    # token = RtcTokenBuilder.buildTokenWithAccount(
    #     appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    # print('token', token)

    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Attendee,
                                              privilegeExpiredTs)
    print("Token with int uid: {}".format(token))
    context = {
        'appID': appID,
        'appCertificate': appCertificate,
        'channelName': channelName,
        'token': token,
        'uid':uid

    }
    return render(request, 'videocall/video_call.html', context)