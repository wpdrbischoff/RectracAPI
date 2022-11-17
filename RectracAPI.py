from __future__ import annotations

import requests
from typing import Any

import urlconfig

class API():
    def __init__(self, live: bool = False) -> None:
        self.live = live
        _live_demo = f'/wbwsc/{urlconfig.DEMO}'

        if self.live:
            _live_demo = f'/wbwsc/{urlconfig.LIVE}'

        self.full_url = f'{urlconfig.BASEURL}{_live_demo}/{urlconfig.RTWS}'


    def auth(self, username: str, password: str) -> bool: 
        self.username = username
        self.password = password

        payload = {'UserName': self.username, 'Password': self.password}
        params = {'UseSessionDefaultValues': 'Yes'}

        endpoint = 'sessions'
        response = requests.post(f'{self.full_url}/{endpoint}', params=params, data=payload)

        self.headers = {'Cookie': f'_rectracsessionid={response.json()["sessionID"]}'}

        if response.json()['data']['sessionState'] == 'WaitingForVic':

            sub_endpoint = 'waitingforvic'
            endpoint = f'{endpoint}/{sub_endpoint}'
            
            response = requests.post(f'{self.full_url}/{endpoint}', headers=self.headers)
            self.headers = {'Cookie': f'_rectracsessionid={response.json()["sessionID"]}'}


    def query_endpoint(self, endpoint: str, params: dict) -> dict:
        self.endpoint = endpoint
        self.params = params

        response = requests.get(f'{self.full_url}/{self.endpoint}', headers=self.headers, params=params)

        return response.json()['data']


if __name__ == "__main__":
    pass
