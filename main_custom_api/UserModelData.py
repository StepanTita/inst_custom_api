import urllib.request

from PIL import Image, ImageChops


class UserData(object):
    def __init__(self, account):
        # avatar
        self.__default_img = Image.open("static/files/default.jpg")
        url_img = Image.open(urllib.request.urlopen(account.profile_pic_url))
        self.no_avatar = self.__compare_img(url_img)

        # nums/length username
        self.nums_to_len_username = sum(c.isdigit() for c in account.username) / len(account.username)

        # number of tokens in fullname
        self.tokens_in_fullname = len(account.full_name.split(' '))

        # nums/length fullname
        self.nums_to_len_fullname = sum(c.isdigit() for c in account.full_name) / len(account.full_name) if len(account.full_name) > 0 else 0

        # name==username
        self.name_equals_username = (account.username == account.full_name)

        # bio len
        self.bio_len = len(account.biography)

        # has external URL
        self.has_external = False  # todo:fix

        # is private profile
        self.is_private = account.is_private

        # number of posts
        self.posts_number = account.media_count

        # number of followers
        self.followers = account.followers_count

        # number of follows
        self.follows = account.follows_count

        self.user_desc = {
            'pic_url': account.profile_pic_url,
            'username': account.username,
            'follows': account.follows_count,
            'followers': account.followers_count,
            'name': account.full_name,
        }

    # @return true if avatar image is default
    def __compare_img(self, image_url):
        diff = ImageChops.difference(self.__default_img, image_url)
        return not diff.getbbox()

    def __str__(self) -> str:
        return str(self.__dict__)
