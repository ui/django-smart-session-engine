# django-smart-session-engine


Django Smart Session Engine allows django application to do more with its session capabilities. On top of normal session engine capabilities that Django provide, this package provide these capabilities:

* Get all of user's session (**TODO**)
* Get all session based on channel (**TODO**)


## Installation
**TODO**



## Dependencies

* django > 2.x
* django-redis


## Configuration

Put the following in `settings.py`

```
SESSION_ENGINE = "libraries.smart_session_engine.session_engine"
SMART_SESSION_ENGINE_CONNECTION_URL = "redis://127.0.0.1:6379/1"
```

## How to use

**TODO**


## Testing
```
django-admin.py test smart_session_engine.tests --settings=smart_session_engine.tests.settings --pythonpath=.
```



##### Disclaimer
Created and maintained by [Stamps](https://stamps.co.id/), Indonesia's most elegant CRM/loyalty platform.
