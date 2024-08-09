import requests
import json
import time
import pprint
import pandas as pd

headers = {
    'Content-Type': 'application/json'
}

HOST='localhost'
URL_PREFIX = 'http://{host}:9200'.format(host=HOST)

INDEX_NAME_CONDUCTOR_WORKFLOW="workflow"
INDEX_NAME_CONDUCTOR_TASK="task"

# Requests
# https://docs.python-requests.org/en/latest/api
def print_request(pr):
    body = pr.body
    if body != None and len(body) > 1000:
        body = str(body[:100]) + '...'
    print("""=== >
{method} {url}
{headers}
{body}""".format(method=pr.method, url=pr.url, headers=pr.headers, body=body))

def print_response(r):
    print("====== Response\n", r.status_code)
    print_request(r.request)
    print("=== <")
    print(r.headers)
    if 'content-type' in r.headers and  'application/json' in r.headers['content-type']:
        pprint.pprint(r.json())
    else:
        if len(r.content) > 1000:
            print(r.content[:100], '...')
        else:
            print(r.content)

###############################################################################
# Explicit mapping
#
# workflow
# task
###############################################################################

# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/explicit-mapping.html

# MetadataCreateIndexService

url = URL_PREFIX + \
    '/{index_name}'.format(index_name=INDEX_NAME_CONDUCTOR_WORKFLOW)
params = {}
mapping_data = {
    "properties": {
        "correlationId": {
            "type": "keyword",
            "index": True,
            "doc_values": True
        },
        "endTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis",
            "doc_values": True
        },
        "executionTime": {
            "type": "long",
            "doc_values": True
        },
        "failedReferenceTaskNames": {
            "type": "text",
            "index": False
        },
        "input": {
            "type": "text",
            "index": True
        },
        "output": {
            "type": "text",
            "index": True
        },
        "reasonForIncompletion": {
            "type": "keyword",
            "index": True,
            "doc_values": True
        },
        "startTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis",
            "doc_values": True
        },
        "status": {
            "type": "keyword",
            "index": True,
            "doc_values": True
        },
        "updateTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis",
            "doc_values": True
        },
        "version": {
            "type": "long",
            "doc_values": True
        },
        "workflowId": {
            "type": "keyword",
            "index": True,
            "doc_values": True
        },
        "workflowType": {
            "type": "keyword",
            "index": True,
            "doc_values": True
        },
        "rawJSON": {
            "type": "text",
            "index": False
        },
        "event": {
            "type": "keyword",
            "index": True
        }
    }
}

data = {
  "mappings": mapping_data
}

print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
print_response(r)


url = URL_PREFIX + '/{index_name}/_mapping'.format(index_name=INDEX_NAME_CONDUCTOR_WORKFLOW)
params = {
}
print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.get(url=url, headers=headers, params=params)
print_response(r)


# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/explicit-mapping.html

# MetadataCreateIndexService

url = URL_PREFIX + \
    '/{index_name}'.format(index_name=INDEX_NAME_CONDUCTOR_TASK)
params = {}
mapping_data = {
    "properties": {
        "correlationId": {
            "type": "keyword",
            "index": True
        },
        "endTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
        },
        "executionTime": {
            "type": "long"
        },
        "input": {
            "type": "text",
            "index": True
        },
        "output": {
            "type": "text",
            "index": True
        },
        "queueWaitTime": {
            "type": "long"
        },
        "reasonForIncompletion": {
            "type": "keyword",
            "index": True
        },
        "scheduledTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
        },
        "startTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
        },
        "status": {
            "type": "keyword",
            "index": True
        },
        "taskDefName": {
            "type": "keyword",
            "index": True
        },
        "taskId": {
            "type": "keyword",
            "index": True
        },
        "taskType": {
            "type": "keyword",
            "index": True
        },
        "updateTime": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
        },
        "workflowId": {
            "type": "keyword",
            "index": True
        },
        "workflowType": {
            "type": "keyword",
            "index": True
        }
    }
}


data = {
    "mappings": mapping_data
}

print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
print_response(r)

url = URL_PREFIX + '/{index_name}/_mapping'.format(index_name=INDEX_NAME_CONDUCTOR_TASK)
params = {
}
print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.get(url=url, headers=headers, params=params)
print_response(r)

###############################################################################
# Index Template
#
# template_event
# template_task_log
###############################################################################
# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/index-templates.html
# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/indices-put-template.html

# MetadataIndexTemplateService

url = URL_PREFIX + \
    '/_index_template/{template_name}'.format(template_name='template_event')
params = {}

data = {
    "index_patterns": ["*event*"],
    "template": {
        "settings": {
            "refresh_interval": "1s"
        },
        "mappings": {
            "properties": {
                "action": {
                    "type": "keyword",
                    "index": True
                },
                "created": {
                    "type": "long"
                },
                "event": {
                    "type": "keyword",
                    "index": True
                },
                "id": {
                    "type": "keyword",
                    "index": True
                },
                "messageId": {
                    "type": "keyword",
                    "index": True
                },
                "name": {
                    "type": "keyword",
                    "index": True
                },
                "output": {
                    "properties": {
                        "workflowId": {
                            "type": "keyword",
                            "index": True
                        }
                    }
                },
                "status": {
                    "type": "keyword",
                    "index": True
                }
            }
        },
        "aliases": {}
    }
}


print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
print_response(r)


url = URL_PREFIX + \
    '/_index_template/{template_name}'.format(template_name='template_message')
params = {}

data = {
  "index_patterns": [ "*message*" ],
  "priority" : 1,
  "template": {
    "settings": {
      "refresh_interval": "1s"
    },
    "mappings": {
      "properties": {
        "created": {
          "type": "long"
        },
        "messageId": {
          "type": "keyword",
          "index": True
        },
        "payload": {
          "type": "keyword",
          "index": True
        },
        "queue": {
          "type": "keyword",
          "index": True
        }
      }
    },
    "aliases": { }
  }
}

print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
print_response(r)


url = URL_PREFIX + \
    '/_index_template/{template_name}'.format(
        template_name='template_task_log')
params = {}

data = {
    "index_patterns": ["*task*log*"],
    "priority": 2,
    "template": {
        "settings": {
            "refresh_interval": "1s"
        },
        "mappings": {
            "properties": {
                "createdTime": {
                    "type": "long"
                },
                "log": {
                    "type": "keyword",
                    "index": True
                },
                "taskId": {
                    "type": "keyword",
                    "index": True
                }
            }
        },
        "aliases": {}
    }
}


print(url)
pprint.pprint(headers)
pprint.pprint(params)

r = requests.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
print_response(r)