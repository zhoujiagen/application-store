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
  "requestId": "52fef28d-19db-44e3-b0b9-8937bca6cd36",
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
              "id": 17,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 18,
                    "value": "Jim",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 2,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 3,
                    "value": "Dave",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 19,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 20,
                    "value": "Paras",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 4,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 5,
                    "value": "Josh",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 21,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 22,
                    "value": "Denise",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 6,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 7,
                    "value": "Ted",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 8,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 9,
                    "value": "Hank",
                    "label": "name"
                  }
                ]
              }
            },
            {
              "id": 15,
              "label": "person",
              "properties": {
                "name": [
                  {
                    "id": 16,
                    "value": "Kelly",
                    "label": "name"
                  }
                ]
              }
            }
          ],
          "edges": [
            {
              "id": 10,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 6,
              "outV": 2
            },
            {
              "id": 11,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 4,
              "outV": 2
            },
            {
              "id": 12,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 8,
              "outV": 2
            },
            {
              "id": 13,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 8,
              "outV": 4
            },
            {
              "id": 14,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 4,
              "outV": 6
            },
            {
              "id": 23,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 17,
              "outV": 2
            },
            {
              "id": 24,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 15,
              "outV": 2
            },
            {
              "id": 25,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 17,
              "outV": 15
            },
            {
              "id": 26,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 21,
              "outV": 15
            },
            {
              "id": 27,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 21,
              "outV": 17
            },
            {
              "id": 28,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 19,
              "outV": 17
            },
            {
              "id": 29,
              "label": "is_friends_with",
              "inVLabel": "person",
              "outVLabel": "person",
              "inV": 21,
              "outV": 19
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
