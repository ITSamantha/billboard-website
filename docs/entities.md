## User

| name           | type                  | description                      | permissions                                  |
|----------------|-----------------------|----------------------------------|----------------------------------------------|
| id             | string                |                                  | all                                          |
| user_name      | string                |                                  | all                                          |
| avatar         | string                | path to avatar photo             | all                                          |
| registered_at  | string                | 5 years ago, 10 minutes ago, ... | all                                          |
| role           | string                | admin, seller, buyer, ...        | all                                          |
| user_fields    | map\[field => value\] |                                  | all                                          |
| phone          | string                |                                  | admins or auth()->user() == $request->user() |
| email          | string                |                                  | admins or auth()->user() == $request->user() |
| email_verified | bool                  |                                  | admins or auth()->user() == $request->user() |

## Address

| name           | type                | permissions                                  |
|----------------|---------------------|----------------------------------------------|
| id             | string              | all                                          |
| address        | string              | all                                          |
| longitude      | double              | all                                          |
| latitude       | double              | all                                          |

## Full address

Can be filled either (longitude, latitude) or (country, city, street)

| name      | type           | permissions                                  |
|-----------|----------------|----------------------------------------------|
| id        | string         | all                                          |
| country   | string \| null | all                                          |
| city      | string \| null | all                                          |
| street    | string \| null | all                                          |
| house     | string \| null | all                                          |
| flat      | string \| null | all                                          |
| longitude | double \| null | all                                          |
| latitude  | double \| null | all                                          |


## Categories

| name      | type           | permissions                                  |
|-----------|----------------|----------------------------------------------|
| id        | string         | all                                          |
| category  | string         | all                                          |

## Tags

| name    | type           | permissions                                  |
|---------|----------------|----------------------------------------------|
| id      | string         | all                                          |
| tag     | string         | all                                          |

## Reviews

| name       | type          | comment                                  | permissions                                  |
|------------|---------------|------------------------------------------|----------------------------------------------|
| id         | string        |                                          | all                                          |
| text       | string        |                                          | all                                          |
| ratings    | int           | from 1 to 5                              | all                                          |
| user       | [user](#user) | if possible short version (name, avatar) | all                                          |
| created_at | string        | 5 years ago, 10 minutes ago, ...         | all                                          |

## Priorities

| name       | type          | comment                                  | permissions                                  |
|------------|---------------|------------------------------------------|----------------------------------------------|
| color      | string        | colored advertisement background         | all                                          |
| title      | string        | title of priority                        | all                                          |

