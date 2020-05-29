import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Context-Type': 'text/plain'
        },
        'body': 'Hello, Cloud Development Kit! You have hit {}\n'.format(event['path'])
    }