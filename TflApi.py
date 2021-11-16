import ast
import requests


class TflApi:
    base_url: str = "https://api.tfl.gov.uk/"

    def __init__(self, app_key: str) -> None:
        self.app_key: str = app_key  # also called primary_key

    def construct_request(self, url_part: str):
        url: str = self.base_url + url_part
        header = {'Cache-control': 'no-cache', 'app_key': self.app_key}
        return url, header

    def request_air_quality(self):
        url, headers = self.construct_request(url_part="AirQuality/")
        res = requests.get(url, headers=headers)
        return res.text

    def air_quality(self):
        res = self.request_air_quality()
        res_dict = ast.literal_eval(res)
        res_list_summary = [res_dict['currentForecast'][0]['forecastSummary'],
                            res_dict['currentForecast'][1]['forecastSummary']]
        res_list_text = [res_dict['currentForecast'][0]['forecastText'],
                         res_dict['currentForecast'][1]['forecastText']]
        return res_list_summary, res_list_text

    def request_next_arrival(self):
        url, headers = self.construct_request(url_part="Mode/tube/Arrivals")
        params = {'count': '1'}
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        return res.text

    def find_next_arrival_by_tube(self, station_name: str = None) -> str:
        try:
            res = self.request_next_arrival()
            res_dict = ast.literal_eval(res)
            return res_dict[1]['stationName']
        except requests.exceptions.HTTPError:
            print("api request error")
