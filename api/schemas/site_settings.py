site_settings_schema = {
    "type": "object",
    "anyOf": [
        {"required": ["allow_registration"]},
        {"required": ["allow_upload"]},
        {"required": ["skip_patterns"]},
        {"required": ["heavyweight_process"]},
        {"required": ["map_api_key"]},
    ],
    "properties": {
        "allow_registration": {"type": "boolean"},
        "allow_upload": {"type": "boolean"},
        "skip_patterns": {"type": "string"},
        "heavyweight_process": {"type": "number"},
        "map_api_key": {"type": "string"},
    },
}
