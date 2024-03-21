def parse_params(params) -> dict:
    parsed = {}
    for key, value in params.items():
        parts = key.split('[')
        if len(parts) > 1:
            current_dict = parsed
            for part in parts[:-1]:
                part = part.rstrip(']')
                current_dict.setdefault(part, {})
                current_dict = current_dict[part]
            current_dict[parts[-1].rstrip(']')] = value
        else:
            parsed[key] = value
    return parsed
