# CommuniTies

## 接口定义

前端Query


后端返回

return:

    - status: 1
    - message:
        - graph: iframe_url
        - sublist:
            - name: "Chicago"
                - emotion:
                    - possitive: 0.3
                    - neutral: 0.2
                    - negative: 0.5
                - activities:
                    - hate_speech: 0.5
                    - misinformation: 0.4
                    - fake_name1 : 0.2
                    - fake_name2 : 0.6
            - name: "Beijing"
                - emotion:
                    - possitive: 0.5
                    - neutral: 0.2
                    - negative: 0.3
                - activities:
                    - hate_speech: 0.4
                    - misinformation: 0.4
                    - fake_name1 : 0.2
                    - fake_name2 : 0.6

json format
``` json

{
    "message":{
        "graph": "iframe_url",
        "sublist":[
        {
            "name": "Chicago",
            "emotion": [
                {
                    "name": "possitive",
                    "value": 0.2
                },
                {
                    "name": "neutral",
                    "value": 0.2
                },
                {
                    "name": "negative",
                    "value": 0.6
                }
            ],
            "activities":[
                {
                    "name": "hate_speech",
                    "value": 0.3
                },
                {
                    "name": "misinfomation",
                    "value": 0.5
                },
                {
                    "name": "fake_activity1",
                    "value": 0.6
                },
                {
                    "name": "fake_activity2",
                    "value": 0.1
                }
            ]
        },
        {
            "name": "Beijing",
            "emotion": [
                {
                    "name": "possitive",
                    "value": 0.6
                },
                {
                    "name": "neutral",
                    "value": 0.2
                },
                {
                    "name": "negative",
                    "value": 0.2
                }
            ],
            "activities":[
                {
                    "name": "hate_speech",
                    "value": 0.3
                },
                {
                    "name": "misinfomation",
                    "value": 0.5
                },
                {
                    "name": "fake_activity1",
                    "value": 0.6
                },
                {
                    "name": "fake_activity2",
                    "value": 0.1
                }
            ]
        }]
    }
}


```


