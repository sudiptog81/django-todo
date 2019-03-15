# Django Todo App

This is a simple todo app that uses Django and Postgres. A working example is hosted at [Heroku](https://todo-app-demo-django.herokuapp.com/todo/). The following rudimentary API documentation should be helpful:

## API

_**Note**: POST requests require CSRF Cookies_

### Viewing Todos

#### GET /view/

Response set will be ordered by completion boolean and descending order of date and time.

Example Request:

```bash
curl https://todo-app-demo-django.herokuapp.com/view/
```

Example Response:

```json
{
  "data": [
    {
      "todo_id": 1,
      "todo_content": "This is a todo that has been completed",
      "todo_completed": true,
      "todo_time": "2019-03-14T22:58:00Z",
      "date_created": "2019-03-14T17:26:36.728Z"
    },
    {
      "todo_id": 2,
      "todo_content": "This is a todo that is yet to be completed",
      "todo_completed": false,
      "todo_time": "2019-03-22T07:46:00Z",
      "date_created": "2019-03-14T17:26:36.728Z"
    },
    {
      "todo_id": 3,
      "todo_content": "This is an updated todo",
      "todo_completed": false,
      "todo_time": "2019-03-17T23:03:00Z",
      "date_created": "2019-03-14T17:33:12.513Z"
    }
  ]
}
```

### Adding Todos

#### POST /add/

- `content` (required) - TextField
- `date` (required) - MMM DD, YYYY format
- `time` (required) - HH:MM AM/PM format
- `browser` (required) - 0 for JSON Response, 1 for Redirection

### Updating Todos

#### POST /toggle/

- `id` (required) - Todo ID (from /view/)
- `browser` (required) - 0 for JSON Response, 1 for Redirection

#### POST /edit/

- `id` (required) - Todo ID (from /view/)
- `content` (required) - TextField
- `browser` (required) - 0 for JSON Response, 1 for Redirection

### Deleting Todos

#### POST /delete/

- `id` (required) - Todo ID (from /view/)
- `browser` (required) - 0 for JSON Response, 1 for Redirection

## Author

**[Sudipto Ghosh](https://sudipto.ghosh.pro)**

## License

Licensed under the open-source MIT License