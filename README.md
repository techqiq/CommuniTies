# CommuniTies

## 接口定义

前端Query


后端返回
json我写的太乱了，还是按照分层次来吧。

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




