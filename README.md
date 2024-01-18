# My Home Assistant Files

Quick way to add a quirk without the full HA dev env setup.

```
# https://github.com/home-assistant/core/blob/dev/requirements_all.txt

./.venv/bin/pip install zigpy
./.venv/bin/pip install zha-quirks
```

For a proper env setup
https://developers.home-assistant.io/docs/development_environment/

---

- Logging: https://www.home-assistant.io/integrations/zha#debug-logging
  - Also possible to set `logger.set_level` through events in HA dev tools
