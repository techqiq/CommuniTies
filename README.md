# CommuniTies

## 接口定义

目前我后端就只有一个返回的接口，返回的内容如下. 我觉得就是和之前的一样。。但是res.message.sublist 给我报错了？

``` json
{"message":{"graph":"https://hub.graphistry.com/graph/graph.html?dataset=3bd7e1294d9f4dc5885a903ee606ef70&type=arrow&viztoken=7fdf4b69-8dcd-4787-9e69-749722261519&usertag=7148a415-pygraphistry-0.25.1&splashAfter=1658433749&info=true&menu=False",
"sublist":[{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.2},{"name":"neutral","value":0.2},{"name":"negative","value":0.6}],"name":"LockdownSkepticism"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"austincirclejerk"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"austincirclejerk"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"conspiracy"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"chicago"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"CoronavirusUS"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"philadelphia"},{"activities":[{"name":"hate_speech","value":0.3},{"name":"misinfomation","value":0.5},{"name":"fake_activity1","value":0.6},{"name":"fake_activity2","value":0.1}],"emotion":[{"name":"possitive","value":0.6},{"name":"neutral","value":0.2},{"name":"negative","value":0.2}],"name":"Covid2019"}]},"status":"success"}

```


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


