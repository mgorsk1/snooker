import logging
from abc import abstractmethod
from typing import Any, List, Optional, Type, Union  # noqa

import requests

from snooker.models import JsonModel

ReturnType = Optional[Union[Type[JsonModel], List[Type[JsonModel]]]]


class BaseApi:
    def __init__(self, headers: dict = dict()):
        self.session = requests.Session()

        self.session.headers.update(**headers)

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @staticmethod
    def _unmarshal(data: dict, model: Type[JsonModel]) -> Any:
        try:
            return model.schema().load(data, many=True)
        except Exception:
            logging.warning('Error unmarshaling data.', extra=dict(data=data, model=model), exc_info=True)

            return None

    def _get_one_dimensional(self, params: dict, model: Type[JsonModel]) -> Any:
        result = None

        data = self._make_request(params)

        if data:
            result = BaseApi._unmarshal(data, model)

        if not result:
            return None
        else:
            return result[0]

    def _get_two_dimensional(self, params: dict, model: Type[JsonModel]) -> Any:
        result = None

        data = self._make_request(params)

        if data:
            result = BaseApi._unmarshal(data, model)

        if not result:
            return None
        else:
            return result

    def _make_request(self, params: dict = dict()) -> Optional[dict]:
        try:
            response = self.session.get(self.base_url, params=params)
        except Exception as e:
            raise e

        try:
            return response.json()
        except Exception:
            logging.warning('Error retrieving json data.', extra=dict(params=params), exc_info=True)

            return None
