from src.api.transformers.base_transformer import BaseTransformer


def transform(data, transformer: BaseTransformer):
    """
    Transforms the data with the given transformer
    :param data: data to transform: model, list, null or paginator? todo paginator
    :param transformer:
    :return: returns none, dict, or array of dicts
    """
    if data is None:
        return None
    if isinstance(data, list):
        return [transformer.transform_with_includes(item) for item in data]
    if False:
        pass  # pagination stuff?
    # model
    return transformer.transform_with_includes(data)
