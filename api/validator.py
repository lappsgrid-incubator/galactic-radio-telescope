from jsonschema import validate as json_validate

SCHEMA_V1 = {
  "required": [
    "galaxy_version",
    "generated",
    "jobs",
    "metrics",
    "report_hash",
    "tools",
    "users",
    "version"
  ],
  "type": "object",
  "properties": {
    "galaxy_version": {
      "type": "string"
    },
    "generated": {
      "type": "string"
    },
    "jobs": {
      "required": [
        "error",
        "ok"
      ],
      "properties": {
        "error": {
          "minimum": 0,
          "type": "integer"
        },
        "ok": {
          "minimum": 0,
          "type": "integer"
        },
      },
      "type": "object"
    },
    "metrics": {
      "required": [
        "_times"
      ],
      "properties": {
        "_times": {
          "items": {
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "minItems": 1,
          "type": "array"
        },
      },
      "type": "object"
    },
    "report_hash": {
      "type": "string"
    },
    "tools": {
      "items": {
        "maxItems": 6,
        "minItems": 6,
        "type": "array"
      },
      "minItems": 0,
      "type": "array"
    },
    "users": {
      "properties": {
        "active": {
          "minimum": 0,
          "type": "integer"
        },
        "total": {
          "minimum": 0,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "vesion": {
      "type": "integer"
    }
  }
}


def validate(data):
    if 'version' not in data:
        raise Exception("Data does not specify schema version")

    if data['version'] == 1:
        return json_validate(data, SCHEMA_V1)

    raise Exception("Unknown schema version: %s" % data['version'])
