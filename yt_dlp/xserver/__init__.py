import yt_dlp
import timeit
import traceback
import time

def atest(url):
    expired_cookie_string = """# Netscape HTTP Cookie File
# This file is generated by yt-dlp.  Do not edit.
.x.com	TRUE	/	TRUE	1749087731	guest_id	v1%3A170718541122698377
.x.com	TRUE	/	TRUE	1758596298	night_mode	2
.x.com	TRUE	/	TRUE	1761620298	guest_id_marketing	v1%3A170718541122698377
.x.com	TRUE	/	TRUE	1761620298	guest_id_ads	v1%3A170718541122698377
.x.com	TRUE	/	TRUE	1753435424	kdt	lSbklJoKir1eTw7GnRWaJkIE8hoyxSbmNsHKY0mw
.x.com	TRUE	/	TRUE	1753435424	auth_token	c68344a2c5ff0aac3dca3b2eedce219cb664cac6
.x.com	TRUE	/	TRUE	1753435425	ct0	465910614598a9886199443d5c9f114d5033008f7e515d82d6aa59fce10ca10a29cfc189547a2c1998e30aaba72ec3f98c699fa9fce57ed33b907667c37f28170a2990a0b5214e689f1f2eb5eaac03ec
.x.com	TRUE	/	TRUE	1758596304	twid	u%3D1803720340625072128
.x.com	TRUE	/	FALSE	1753435507	des_opt_in	Y
.x.com	TRUE	/	FALSE	1761381967	_ga	GA1.2.579213636.1718875598
.x.com	TRUE	/	TRUE	1755070065	dnt	1
.x.com	TRUE	/	TRUE	1727330261	external_referer	padhuUp37zjgzgv1mFWxJ5Xq0CLV%2BbpWuS41v6lN3QU%3D|0|8e8t2xd8A2w%3D
.x.com	TRUE	/	TRUE	1761620298	personalization_id	"v1_/cArai6HMkylGx68yje2+Q=="
x.com	FALSE	/	FALSE	1734427413	g_state	{"i_l":0}
x.com	FALSE	/	FALSE	0	lang	en
"""

    cookie_string = """# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.x.com	TRUE	/	TRUE	1748337079	guest_id	v1%3A170857238009071821
.x.com	TRUE	/	TRUE	1761202470	night_mode	2
x.com	FALSE	/	FALSE	1733646841	g_state	{"i_l":0}
.x.com	TRUE	/	TRUE	1752654879	kdt	xN525Tnne6eaGYE8U6JdyB1RbUJauQNEJzcMnhJn
.x.com	TRUE	/	TRUE	1752654879	auth_token	3ec860a9b96b2b13ba330fd7743f86535177990b
.x.com	TRUE	/	TRUE	1752654879	ct0	5cfda9c9a7dd4ba85e103eca722e7c82847e58fc8df71ff825763a2a1c4612412c01fd64da570d9b5d86bb9718284a24683aca0159349536875756a47c4f7140dff186f7e1cdf9756e27facda820f3bf
.x.com	TRUE	/	TRUE	1761202478	twid	u%3D1612631041230921729
.x.com	TRUE	/	FALSE	1753447549	des_opt_in	Y
.x.com	TRUE	/	TRUE	1764226478	guest_id_ads	v1%3A170857238009071821
.x.com	TRUE	/	TRUE	1764226478	guest_id_marketing	v1%3A170857238009071821
.x.com	TRUE	/	TRUE	1735441214	d_prefs	MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw
.x.com	TRUE	/	TRUE	1760409281	personalization_id	"v1_cZgLW3hIQdlRPC90/tykUQ=="
x.com	FALSE	/	FALSE	0	lang	en

"""

    ydl_opts = {
        "noplaylist": True,
        # 'skip_download': True,
        # 'write-thumbnail': True,
        # 'extract_flat': True,
        # 'ignore_no_formats_error': True,
        # 'debug_printtraffic': True,
        # "list-thumbnails": True,
        # 'extract_flat': True,
        'cookiestr': cookie_string
    }

    def get_entry_info(data):
        if ('formats' in data) and data['formats'] != []:  # one video
            entry = dict()
            entry['file_type'] = "Video"
            entry['cover'] = data.get('thumbnails', '')[0].get('url', '')
            formats = []
            for file_format in data["formats"]:
                if 'http' in file_format.get("format_id", ""):
                    video_info = dict()
                    video_info["resolution"] = file_format.get("resolution", "") \
                                               or str(file_format.get("width", "")) + "x" + str(
                        file_format.get("height", ""))

                    if file_format.get('video_ext', "") == "":
                        if ".mp4" in file_format.get("url", ""):
                            video_info["file_type"] = "mp4"
                        else:
                            video_info["file_type"] = "video"
                    else:
                        video_info["file_type"] = file_format.get('video_ext', "")

                    download_url = file_format.get('url', "")
                    # download_url = download_url.replace("https://video.twimg.com/",
                    #                                     "https://xcdn03.twittervideodown.com/")

                    video_info["download_url"] = download_url
                    formats.append(video_info)
            # entry['duration'] = str(int(data.get("duration", "") or 0 / 1000)) + "s" if "duration" in data else ""
            entry['formats'] = formats
            return entry

        elif ('formats' in data) and data['formats'] == []:  # one picture
            entry = dict()
            entry['file_type'] = "Picture"
            entry['cover'] = data.get('thumbnails', '')[0].get('url', '')
            formats = []
            for file_format in data["thumbnails"]:
                if 'jpg' in file_format.get("url", ""):
                    video_info = dict()
                    video_info["resolution"] = file_format.get("resolution", "") \
                                               or str(file_format.get("width", "")) + "x" + str(
                        file_format.get("height", ""))

                    if file_format.get('video_ext', "") == "":
                        if ".jpg" in file_format.get("url", ""):
                            video_info["file_type"] = "jpg"
                        else:
                            video_info["file_type"] = "picture"
                    else:
                        video_info["file_type"] = file_format.get('video_ext', "")

                    download_url = file_format.get('url', "")
                    # download_url = download_url.replace("https://pbs.twimg.com/",
                    #                                     "https://xcdn03.twittervideodown.com/")

                    video_info["download_url"] = download_url
                    formats.append(video_info)
            # entry['duration'] = str(int(data.get("duration", "") or 0 / 1000)) + "s" if "duration" in data else ""
            entry['formats'] = formats
            return entry

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        try:
            start_time = time.time()
            data = ydl.extract_info(url=url, download=False, process=False)
            print("url-->" + url + "\n"
                  + 'x-rate-limit-limit' + ":" + data['x-rate-limit-limit'] + "\n"
                  + 'x-rate-limit-reset' + ":" + data['x-rate-limit-reset'] + "\n"
                  + 'x-rate-limit-remaining' + ":" + data['x-rate-limit-remaining']
                  )

            tweet_id = data.get("id", "")
            title = data.get("title", "").replace("'", " ").replace("\"", " ")
            original_url = data.get("original_url", "")
            uploader = data.get("uploader", "")
            upload_date = data.get("upload_date", "")

            entries = []
            if 'formats' in data:
                entry = get_entry_info(data)
                entries.append(entry)
            else:
                for entry in data["entries"]:
                    single_entry = get_entry_info(entry)
                    entries.append(single_entry)

            end_time = time.time()

            result = {
                "code": 0,
                "status": "success",
                "type": "json",
                "tweet_id": tweet_id,
                "tweet_title": title,
                "original_url": original_url,
                "tweet_uploader": uploader,
                "tweet_upload_date": upload_date,
                "analyze_time": f"{end_time - start_time:.1f}s",
                "entries": entries
            }

            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exception(e)


if __name__ == '__main__':
    # execution_time = timeit.timeit(atest, number=1)
    # print(f"运行时间: {execution_time} 秒")

    urls = [
        # "https://x.com/diaochan12345/status/1785319787264180647",
        # "https://x.com/ximeibaobao/status/1784849463615578341",
        # "https://x.com/nunadoic/status/1790401143132115154",
        # "https://x.com/din_lol_/status/1838128873088946561",
        # "https://x.com/bbcchinese/status/1839225336711540787",
        # "https://x.com/RedLi8ning/status/1839263964586455365",
        # "https://x.com/LoversInArt/status/1826656323930558501",
        # "https://x.com/AVjingxuan/status/1849706803409584614",  # need cookies tweet video
        # "https://x.com/LoversInArt/status/1826515202998706443", # need cookies tweet gif
        # "https://x.com/twrnaat/status/1839197344429990048",  # two videos
        # "https://x.com/chiguayong_1/status/1849562130120683675",  # two pictures
        # "https://x.com/Solacified/status/1803801373730812301",  # video and pictures
        # "https://x.com/JianLv117/status/1848569731462402101",  # one picture only
        "https://x.com/brutalfightz2/status/1849196480764256363",  # one video only
        # "https://x.com/aigclink/status/1848282370404954304",  # one video only
    ]
    for url in urls:
        atest(url)
