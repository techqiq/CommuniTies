from flask import Flask, jsonify
from flask_cors import CORS
# from flaskext.mysql import MySQL #pip install flask-mysql
# import pymysql

# test data
import json
data = {
                    "graph": "https://hub.graphistry.com/graph/graph.html?dataset=3bd7e1294d9f4dc5885a903ee606ef70&type=arrow&viztoken=7fdf4b69-8dcd-4787-9e69-749722261519&usertag=7148a415-pygraphistry-0.25.1&splashAfter=1658433749&info=true&menu=False",
                    "sublist":[
                    {
                        "name": "LockdownSkepticism",
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
                        "name": "austincirclejerk",
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
                    },
                    {
                        "name": "austincirclejerk",
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
                    },
                    {
                        "name": "conspiracy",
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
                    },
                    {
                        "name": "chicago",
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
                    },
                    {
                        "name": "CoronavirusUS",
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
                    },
                    {
                        "name": "philadelphia",
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
                    },
                    {
                        "name": "Covid2019",
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
                    }
                    
                    ]
}

 
# configuration
DEBUG = True
 
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
     
# mysql = MySQL()
    
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'tashi85795110'
# app.config['MYSQL_DATABASE_DB'] = 'testingdb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
 
@app.route('/')
def home():
    # conn = mysql.connect()
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        # cursor.execute("SELECT * from members order by id")
        # userslist = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'message': data
        })
    except Exception as e:
        print(e)
    # finally:
    #     cursor.close() 
    #     conn.close()
 
 
if __name__ == '__main__':
    app.run()