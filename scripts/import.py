from artists.models import Artist


filename = '../data'

with open(filename, 'r') as f:
    cur_serial_number = 0
    cur_name = ''
    cur_artstation_urls = []
    cur_behance_urls = []
    cur_deviantart_urls = []
    cur_facebook_urls = []
    cur_instagram_urls = []
    cur_pinterest_urls = []
    cur_pixiv_urls = []
    cur_tumblr_urls = []
    cur_twitter_urls = []
    cur_weibo_urls = []
    cur_other_urls = []

    for line in f:
        if line.startswith('- '):
            # Save previous entry
            Artist.objects.get_or_create(
                name=cur_name,
                serial_number=cur_serial_number,
                artstation_url=','.join(cur_artstation_urls),
                behance_url=','.join(cur_behance_urls),
                deviantart_url=','.join(cur_deviantart_urls),
                facebook_url=','.join(cur_facebook_urls),
                instagram_url=','.join(cur_instagram_urls),
                pinterest_url=','.join(cur_pinterest_urls),
                pixiv_url=','.join(cur_pixiv_urls),
                tumblr_url=','.join(cur_tumblr_urls),
                twitter_url=','.join(cur_twitter_urls),
                weibo_url=','.join(cur_weibo_urls),
                other_url=','.join(cur_other_urls),
            )
            # Clear and start next entry
            line = line.split(' ', 2)
            cur_serial_number = line[1]
            if len(line) == 3:
                cur_name = line[2]
            else:
                cur_name = ''
            cur_artstation_urls = []
            cur_behance_urls = []
            cur_deviantart_urls = []
            cur_facebook_urls = []
            cur_instagram_urls = []
            cur_pinterest_urls = []
            cur_pixiv_urls = []
            cur_tumblr_urls = []
            cur_twitter_urls = []
            cur_weibo_urls = []
            cur_other_urls = []
        else:
            if 'artstation' in line:
                cur_artstation_urls.append(line)
            elif 'behance' in line:
                cur_behance_urls.append(line)
            elif 'deviantart' in line:
                cur_deviantart_urls.append(line)
            elif 'facebook' in line:
                cur_facebook_urls.append(line)
            elif 'instagram' in line:
                cur_instagram_urls.append(line)
            elif 'pinterest' in line:
                cur_pinterest_urls.append(line)
            elif 'pixiv' in line:
                cur_pixiv_urls.append(line)
            elif 'tumblr' in line:
                cur_tumblr_urls.append(line)
            elif 'twitter' in line:
                cur_twitter_urls.append(line)
            elif 'weibo' in line:
                cur_weibo_urls.append(line)
            else:
                cur_other_urls.append(line)
