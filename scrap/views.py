from django.shortcuts import render, HttpResponse, render, redirect
import requests
from bs4 import BeautifulSoup
from django.contrib import messages

import json
# Create your views here.

def index(request):
    if request.method == "POST":
        search_word = request.POST['instagramUsername']
        username = search_word
        return redirect('dashboard',userEnterdUsername = username)
    return render(request, 'scrap/index.html')


def dashboard(request, userEnterdUsername):
    

    url = 'https://www.instagram.com/{}/?__a=1'.format(userEnterdUsername)

    headers = {'user-agent': 'customize header string'}  
    response = requests.get(url, headers=headers)


    if response.status_code == 404:
        messages.error(request, "Username Is Invalid")
        return redirect('index')
    else:
        responseJSON = response.json()

        instagram_bio = responseJSON['graphql']['user']['biography']
        instagram_followers = responseJSON['graphql']['user']['edge_followed_by']['count']
        instagram_following = responseJSON['graphql']['user']['edge_follow']['count']
        instagram_fullname = responseJSON['graphql']['user']['full_name']
        instagram_username = responseJSON['graphql']['user']['username']
        instagram_pic_url = responseJSON['graphql']['user']['profile_pic_url_hd']
        instagram_total_post = responseJSON['graphql']['user']['edge_owner_to_timeline_media']['count']
        is_business_account = responseJSON['graphql']['user']['is_business_account']
        is_verified_account = responseJSON['graphql']['user']['is_verified']
        is_private_account = responseJSON['graphql']['user']['is_private']
        instagram_bio_external_url = responseJSON['graphql']['user']['external_url']

        # img_data = requests.get(instagram_pic_url).content
        # with open('image_name.jpeg', 'wb') as handler:
        #     handler.write(img_data)


        context = {
            'instagram_fullname' : instagram_fullname,
            'instagram_followers' : instagram_followers,
            'instagram_following' : instagram_following,
            'instagram_pic_url' : instagram_pic_url,
            'instagram_username' : instagram_username,
            'is_verified_account' : is_verified_account,
            'instagram_total_post': instagram_total_post,
            'instagram_bio' : instagram_bio,    
        }

        return render(request, 'scrap/dashboard.html', context)


def error_404(request, exception):
        data = {}
        return render(request,'scrape/404.html', data)