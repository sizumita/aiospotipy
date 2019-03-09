import base64
import time
import aiohttp
import json


def is_token_expired(token_info):
    now = int(time.time())
    return token_info['expires_at'] - now < 60


class SpotifyOauthError(Exception):
    pass


class SpotifyCredentials(object):
    OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id=None, client_secret=None, proxy=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_info = None
        self.proxy = proxy

    async def get_access_token(self):
        if self.token_info and not is_token_expired(self.token_info):
            return self.token_info['access_token']

    async def request_access_token(self):
        payload = {'grant_type': 'client_credentials'}
        auth_header = base64.b64encode(str(self.client_id + ':' + self.client_secret).encode())
        headers = {'Authorization': 'Basic %s' % auth_header.decode()}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.OAUTH_TOKEN_URL, data=payload, headers=headers, verify=True,
                                    proxy=self.proxy) as response:
                if response.status != 200:
                    raise SpotifyOauthError(response.reason)
                return json.loads(await response.text())

    @staticmethod
    def _add_custom_values_to_token_info(token_info):
        token_info['expires_at'] = int(time.time()) + token_info['expires_in']
        return token_info


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    async def test():
        # async with aiohttp.ClientSession() as session:
        #     # url = "https://connpass.com/api/v1/event?nickname=sizumita"
        #     url = 'https://qiita.com/api/v2/users/sizumita/items?page=1&per_page=1'
        #     async with session.get(url) as response:
        #         r = await response.text()
        #         print(type(json.loads(r)))
        #         print(response.status)
        await asyncio.sleep(5)
        return "5"

    async def t():
        return await asyncio.wait_for(test(), 30, loop=loop)

    def tt():
        return t()

    loop.run_until_complete(tt())
