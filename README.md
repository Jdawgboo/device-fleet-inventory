# Device Fleet Inventory

Validate required device fields and summarize models and health labels from offline inventory records.

```bash
cat devices.json | python tool.py
python -m unittest -v
```

The tool does not discover or alter devices. Record quality and health semantics come from the caller.
