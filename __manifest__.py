{
    "name": "Todo sovellus",
    "version": "1.0",
    "summary": "Todo sovellus käyttäjähallinnalla ja ajastimella",
    "category": "Productivity",
    "author": "Sami Turunen",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/todo_task_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'todo_app/static/src/css/todo_style.css',
        ],
    },
    "installable": True,
    "application": True,
}