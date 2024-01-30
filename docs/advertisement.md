## Advertisement

### ```POST``` /api/advertisement

Create new advertisement as seller with status `not paid`.

###### Parameters

| name        | type                         | description                                                                                                                      | example                |
|-------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------|
| title       | string                       | advertisement main title                                                                                                         |                        |
| description | string                       | advertisement description content                                                                                                |                        |
| category_id | int                          | [category id](../backend/src/schemas/entities/category.py)                                                                       | camera(5)              |
| filters     | map[filter_id => str \| int] | [filter_id](../backend/src/schemas/entities/filter.py), [filter_value](../backend/src/schemas/entities/filter_value.py)          | camera_width(7) => 120 |
| type_id     | int                          | [type](../backend/src/schemas/characteristics/ad_type.py)                                                                        |                        |
| address     | address-json \| address_id   | [address](../backend/src/schemas/entities/address.py). either json-encoded address or address_id for quick filling advertisement |                        |

###### Response

| name    | type   | description |
|---------|--------|-------------|
| success | bool   | auth status |
| id      | string | id          |

###### Status codes

| status code | description                    |
|-------------|--------------------------------|
| 200         | ok                             |
| 403         | forbidden (not a seller/admin) |
| 422         | spam                           |
| 419         | validation                     |
| other       | server error                   |

to be continued...