## Advertisement

### ```POST``` /api/advertisement

Create new advertisement as seller with status `not paid`.

###### Parameters

| name        | type                                             | description                                                                                                             | example                |
|-------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------|
| title       | string                                           | advertisement main title                                                                                                |                        |
| description | string                                           | advertisement description content                                                                                       |                        |
| category_id | int                                              | [category id](../backend/src/schemas/entities/category.py)                                                              | camera(5)              |
| filters     | map[filter_id => str \| int]                     | [filter_id](../backend/src/schemas/entities/filter.py), [filter_value](../backend/src/schemas/entities/filter_value.py) | camera_width(7) => 120 |
| type_id     | int                                              | [type](../backend/src/schemas/characteristics/ad_type.py)                                                               |                        |
| address     | [Full address](entities.md#full-address) \| null | [address](../backend/src/schemas/entities/address.py)                                                                   |                        |
| address_id  | int \| null                                      | [address](../backend/src/schemas/entities/address.py)                                                                   |                        |

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


### ```GET``` /api/advertisement/{id}

Get information about advertisement according to user role. 

Not display advertisements with status->is_shown === true.

###### Parameters

no params

| name         | type                                 | description                                                                                                             | permissions |
|--------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
| success      | bool                                 | true if ok                                                                                                              | all         |
| id           | string                               | id                                                                                                                      | all         |
| price        | double                               |                                                                                                                         | all         |
| user         | [user](entities.md#user)             | user who created advertisement                                                                                          | all         |
| address      | [address](entities.md#address)       | advertisement address                                                                                                   | all         |
| status       | string                               | status to be displayed                                                                                                  | all         |
| filters      | map[filter_id => str \| int]         | [filter_id](../backend/src/schemas/entities/filter.py), [filter_value](../backend/src/schemas/entities/filter_value.py) | all         |
| is_booking   | bool                                 |                                                                                                                         | all         |
| photos_paths | []string                             |                                                                                                                         | all         |
| categories   | [][category](entities.md#categories) |                                                                                                                         | all         |
| tags         | [][tags](entities.md#tags)           |                                                                                                                         | all         |
| reviews      | [][reviews](entities.md#reviews)     |                                                                                                                         | all         |
| created_at   | string                               | 5 years ago, 10 minutes ago, ...                                                                                        | all         |

###### Status codes

| status code | description                    |
|-------------|--------------------------------|
| 200         | ok                             |
| 422         | spam                           |
| other       | server error                   |


### ```GET``` /api/advertisement/{id}?short=true

Get information about advertisement according to user role.

Not display advertisements with status->is_shown === true.

###### Parameters

no params

| name             | type                                   | description                                                                                                             | permissions |
|------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
| success          | bool                                   | true if ok                                                                                                              | all         |
| id               | string                                 | id                                                                                                                      | all         |
| price            | double                                 |                                                                                                                         | all         |
| user             | [user](entities.md#user)               | user who created advertisement                                                                                          | all         |
| address          | [address](entities.md#address)         | advertisement address                                                                                                   | all         |
| status           | string                                 | status to be displayed                                                                                                  | all         |
| filters          | map\[filter_id => str \| int\]         | [filter_id](../backend/src/schemas/entities/filter.py), [filter_value](../backend/src/schemas/entities/filter_value.py) | all         |
| is_booking       | bool                                   |                                                                                                                         | all         |
| photos_paths     | []string                               |                                                                                                                         | all         |
| categories       | [][category](entities.md#categories)   |                                                                                                                         | all         |
| tags             | [][tags](entities.md#tags)             |                                                                                                                         | all         |
| current_priority | [priorities](entities.md#priorities)   |                                                                                                                         | all         |
| created_at       | string                                 | 5 years ago, 10 minutes ago, ...                                                                                        | all         |

###### Status codes

| status code | description                    |
|-------------|--------------------------------|
| 200         | ok                             |
| 422         | spam                           |
| other       | server error                   |

to be continued...

to be continued...