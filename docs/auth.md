## Auth

### ```POST``` /api/login

User to authenticate user as admin / seller / expert / buyer.
Return JSON response with user information presented below and response cookie.

###### Parameters

| name     | type   | description          |
|----------|--------|----------------------|
| email    | string | user email           |
| password | string | not-encoded password |

###### Response success

| name      | type     | description                                    |
|-----------|----------|------------------------------------------------|
| success   | bool     | auth status                                    |
| id        | string   | id                                             |
| user_name | string   | name                                           |
| errors    | []string | list of user-readable messages if error occurs |

###### Status codes

| status code | description         |
|-------------|---------------------|
| 200         | ok                  |
| 401         | invalid credentials |
| 422         | spam                |
| 419         | validation          |
| other       | server error        |

### ```POST``` /api/register

Create buyer account with unverified phone, but with verified email.
Return JSON response with user information presented below and response cookie.

###### Parameters

| name      | type   | description          |
|-----------|--------|----------------------|
| email     | string | user email           |
| user_name | string | user name            |
| password  | string | not-encoded password |

###### Response

| name      | type     | description                                    |
|-----------|----------|------------------------------------------------|
| success   | bool     | auth status                                    |
| id        | string   | id                                             |
| user_name | string   | name                                           |
| errors    | []string | list of user-readable messages if error occurs |

###### Status codes

| status code | description         |
|-------------|---------------------|
| 200         | ok                  |
| 422         | spam                |
| 419         | validation          |
| other       | server error        |

### ```POST``` /api/logout

No request body, no response.