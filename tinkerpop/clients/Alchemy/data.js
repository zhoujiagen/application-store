// FIXME: CORS BUG in gremlim-server http endpoint
// const options = {
//   // mode: 'no-cors', // DEBUG
//   method: 'POST',
//   headers: {'Content-Type': 'application/json'},
//   body: '{"gremlin":"g","bindings":{"x":1},"language":"gremlin-groovy"}'
// };

// fetch('http://127.0.0.1:8182/', options)
//   .then(response => response.json())
//   .then(response => console.log(response))
//   .catch(err => console.error(err));

const data = {
  "requestId": "395fec4a-f891-4046-84a8-5b80459e77e2",
  "status": {
    "message": "",
    "code": 200,
    "attributes": {}
  },
  "result": {
    "data": [
      {
        "graph": {
          "vertices": [
            {
              "id": 49,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 50,
                    "value": "Denise",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 35,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 36,
                    "value": "Dave",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 37,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 38,
                    "value": "Josh",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 39,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 40,
                    "value": "Ted",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 41,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 42,
                    "value": "Hank",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 43,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 44,
                    "value": "Kelly",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 45,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 46,
                    "value": "Jim",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 47,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 48,
                    "value": "Paras",
                    "label": "name"
                  }
                ]
              }
            }
          ],
          "edges": [
            {
              "id": 64,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 39,
              "outV": 35,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2016
                },
                "end_year": {
                  "key": "end_year",
                  "value": 2017
                }
              }
            },
            {
              "id": 65,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 39,
              "outV": 37,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2016
                },
                "end_year": {
                  "key": "end_year",
                  "value": 2019
                }
              }
            },
            {
              "id": 66,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 41,
              "outV": 35,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2017
                },
                "end_year": {
                  "key": "end_year",
                  "value": 2018
                }
              }
            },
            {
              "id": 67,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 43,
              "outV": 35,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2018
                }
              }
            },
            {
              "id": 68,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 49,
              "outV": 35,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2018
                }
              }
            },
            {
              "id": 69,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 43,
              "outV": 49,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2018
                }
              }
            },
            {
              "id": 51,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 39,
              "outV": 35
            },
            {
              "id": 52,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 37,
              "outV": 35
            },
            {
              "id": 53,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 41,
              "outV": 35
            },
            {
              "id": 54,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 41,
              "outV": 37
            },
            {
              "id": 55,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 37,
              "outV": 39
            },
            {
              "id": 56,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 45,
              "outV": 35
            },
            {
              "id": 57,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 43,
              "outV": 35
            },
            {
              "id": 58,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 45,
              "outV": 43
            },
            {
              "id": 59,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 49,
              "outV": 43
            },
            {
              "id": 60,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 49,
              "outV": 45
            },
            {
              "id": 61,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 47,
              "outV": 45
            },
            {
              "id": 62,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 49,
              "outV": 47
            },
            {
              "id": 63,
              "label": "works_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 37,
              "outV": 35,
              "properties": {
                "start_year": {
                  "key": "start_year",
                  "value": 2016
                },
                "end_year": {
                  "key": "end_year",
                  "value": 2017
                }
              }
            }
          ]
        },
        "strategies": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ],
        "bytecode": {},
        "anonymousTraversalClass": {
          "empty": false,
          "present": true
        }
      }
    ],
    "meta": {}
  }
};
