class BaseSearcher():
    def __init__(self, _dict: dict[str, str]):
        self._dict = _dict

    def search(self, key: str) -> str or None:
        pass


class SimpleSearcher(BaseSearcher):
    def __init__(self, _dict: dict[str, str]):
        super().__init__(_dict)

    def search(self, key: str) -> str or None:
        for item in self._dict.items():
            if item[0] == key:
                return item[1]
        return None


class BinarySearcher(BaseSearcher):
    def __init__(self, _dict: dict[str, str]):
        super().__init__(_dict)

    def search(self, key: str) -> str or None:
        return BinarySearcher._search(key, self._dict)

    @staticmethod
    def _search(key: str, _dict: dict[str, str]) -> str or None:
        """
        _dict must be already sorted (ascending)

        :param key: key to find in _dict
        :param _dict: ascending sorted dictionary
        :return: _dict value by key
        """
        sorted_keys = list(_dict.keys())
        sorted_values = list(_dict.values())

        down_limit: int = 0
        up_limit: int = len(_dict) - 1
        center_i: int = up_limit // 2

        while sorted_keys[center_i] != key and down_limit < up_limit:
            if key > sorted_keys[center_i]:
                down_limit = center_i + 1
            else:
                up_limit = center_i - 1
            center_i = int((down_limit + up_limit) / 2)

        if down_limit >= up_limit:
            return None
        return sorted_values[center_i]


class CombinedSearcher(BaseSearcher):
    def __init__(self, _dict: dict[str, str]):
        super().__init__(_dict)
        self.segments: [dict] = self.frequency_analysis()

    def frequency_analysis(self):
        # Сколько раз встречается первый символ каждого ключа  _dict
        frequency_dict: dict[str, int] = {}
        for key in self._dict.keys():
            if key[0] in frequency_dict.keys():
                frequency_dict[key[0]] += 1
            else:
                frequency_dict[key[0]] = 1

        segmented_list: [dict] = []
        for key_letter in frequency_dict.keys():
            keys = {'letter': key_letter, 'count': frequency_dict[key_letter], 'dict': {}}

            for key in self._dict.keys():
                if key[0] == key_letter:
                    keys['dict'][key] = self._dict[key]

            # сортировка словаря по ключу
            keys['dict'] = dict(sorted(keys['dict'].items()))

            segmented_list.append(keys)

        segmented_list.sort(key=lambda value: value['count'], reverse=True)
        return segmented_list

    def search(self, key: str) -> str or None:
        """
        _dict can be any dictionary

        :param key: key to find in _dict
        :param _dict: any dictionary
        :return: _dict value by key
        """
        found_dict = {}
        for i in range(len(self.segments)):
            if self.segments[i]['letter'] == key[0]:
                found_dict = self.segments[i]['dict']
                break

        if len(found_dict) == 0:
            return None

        return BinarySearcher._search(key, found_dict)
