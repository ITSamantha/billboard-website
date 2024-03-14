from abc import ABC, abstractmethod


class BaseTransformer(ABC):
    def __init__(self):
        self.includes = []
        self.available_includes = []
        self.default_includes = []

    @abstractmethod
    def transform(self, item):
        pass

    def include(self, includes: list[str]):
        for include in includes:
            if include in self.available_includes:
                self.includes.append(include)
        return self

    def transform_with_includes(self, item):
        data = self.transform(item)
        for include in list(set(self.includes + self.default_includes)):
            func = getattr(self, 'include_' + include)
            data[include] = func(item)
        return data

    def item(self, data, transformer):
        if data is None:
            return None
        return transformer.transform_with_includes(data)

    def collection(self, data, transformer):
        return [self.item(el, transformer) for el in data]
