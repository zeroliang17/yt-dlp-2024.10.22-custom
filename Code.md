[yt_dlp _init_.py] 
ydl.download(all_urls)

[YoutubeDL.py] 
download(self, url_list)  -> self.extract_info

[YoutubeDL.py] 
def extract_info(self, url, download=True, ie_key=None, extra_info=None,
                     process=True, force_generic_extractor=False)
return self.__extract_info(url, self.get_info_extractor(key), download, extra_info, process)

[YoutubeDL.py] 
@_handle_extraction_exceptions
    def __extract_info(self, url, ie, download, extra_info, process):
return self.process_ie_result(ie_result, download, extra_info)
解析器中 class InfoExtractor 访问  
 def _request_webpage(self, url_or_request, video_id, note=None, errnote=None, fatal=True, data=None,
                         headers=None, query=None, expected_status=None, impersonate=None, require_impersonation=False):
def urlopen(self, req):


def _real_initialize(self):

[YoutubeDL.py] 
def process_ie_result(self, ie_result, download=True, extra_info=None):
self.process_video_result(ie_result, download=download)

[YoutubeDL.py] 
def process_video_result(self, info_dict, download=True):

[YoutubeDL.py]
@_catch_unsafe_extension_error
    def process_info(self, info_dict):
        """Process a single resolved IE result. (Modifies it in-place)"""

[YoutubeDL.py] 
def _write_thumbnails(self, label, info_dict, filename, thumb_filename_base=None):

## 代码本地测试
pyproject.toml 安装依赖
pip install .


## 打包成架构包
pip install hatch

yt_dlp 中 修改 Version.py _pkg_version = '2024.08.06.01' 修改版本

hatch build

pip install dist/your_package_name.tar.gz
