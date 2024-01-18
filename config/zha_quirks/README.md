# Working with ZHA Quirks

- Source: https://github.com/zigpy/zha-device-handlers
- Doc: https://www.home-assistant.io/integrations/zha#how-to-add-support-for-new-and-unsupported-devices

Add to your `configuration.yaml`

```yaml
zha:
  custom_quirks_path: /config/zha_quirks/
```

- There is a possibility that someone reported it already and a quirk might be available in an issue, so start there. Tip: not always but most of the time they are labelled [`label:"custom quirk available"`](https://github.com/zigpy/zha-device-handlers/issues?q=is%3Aissue+is%3Aopen+label%3A%22custom+quirk+available%22+).
- If not, find a base quirk, which are mostly a tuya based device:
  https://github.com/zigpy/zha-device-handlers/tree/dev/zhaquirks/tuya
