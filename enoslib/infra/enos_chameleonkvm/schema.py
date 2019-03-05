SCHEMA = {
    "type": "object",
    "properties": {
        "resources": {"$ref": "#/resources"},
        "key_name": {"type": "string"},
        # everything is optionnal
        "image": {"type": "string"},
        "user": {"type": "string"},
        "allocation_pool": {"$ref": "#/os_allocation_pool"},
        "configure_network": {"type": "boolean"},
        "dns_nameservers": {"type": "array", "items": {"type": "string"}},
        "gateway": {"type": "boolean"},
        "gateway_user": {"type": "string"},
        "network": {"$ref": "#/os_network"},
        "subnet": {"$ref": "#/os_subnet"},
        "prefix": {"type": "string"}
    },
    "additionalProperties": True,
    "required": ["resources", "key_name"],

    "os_allocation_pool": {
        "title": "OSallocationPool",
        "type": "object",
        "properties": {
            "start": {"type": "string"},
            "end": {"type": "string"}
        },
        "required": ["start", "end"],
        "additionalProperties": False
    },

    "os_network": {
        "title": "OSNetwork",
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        },
        "required": ["name"],
        "additionalProperties": False
    },

    "os_subnet": {
        "title": "OSSubnet",
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "cidr": {"type": "string"}
        },
        "required": ["name"],
        "additionalProperties": False
    },

    "resources": {
        "title": "Resource",

        "type": "object",
        "properties": {
            "machines": {"type": "array", "items": {"$ref": "#/machine"}},
            "networks": {"type": "array", "items": {"type": "string"}}
        },
        "additionalProperties": False,
        "required": ["machines", "networks"]
    },

    "machine": {
        "title": "Compute",
        "type": "object",
        "properties": {
            "roles": {"type": "array", "items": {"type": "string"}},
            "flavour": {"type": "string"},
            "number": {"type": "number"}
        },
        "required": [
            "roles",
            "number",
            "flavour"
        ]
    }
}
