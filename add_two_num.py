def lambda_handler(event, context):
    num1 = event.get('num1')
    num2 = event.get('num2')
    if num1 is None or num2 is None:
        return {'statusCode': 400, 'message': 'num1 and num2 are required'}
    return {'statusCode': 200, 'result': num1 + num2}
