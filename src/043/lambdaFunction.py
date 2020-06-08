#Sample SQS Queue
#Lambda Function to similate banking queue


import json
import boto3
import random

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
       SQS Message
       Event doc: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html 

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    """
    try:
        for record in event['Records']:
            body = json.loads(record["body"])
            bank_schedule = body["bank_schedule"]
            account = record['messageAttributes']['Account']['stringValue']
            reconcile_transaction(account, bank_schedule)
            
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        # throw exception, do not handle. Lambda will make message visible again.
        raise e


def reconcile_transaction(account, bank_schedule):
    """reconciles the bank schedule for a specified account
    
    Arguments:
        account {number} -- account number to reconcile
        bank_schedule {dict} -- the schedule for the bank statement
    
    Raises:
        ArithmeticError: Cannot compute negative number
        Exception: Custom exception
    """
    books_schedule = get_books_schedule_for_account(account)
    balance_per_books = books_schedule["balance_per_books"]
    balance_per_statement = bank_schedule['balance_per_statement']
    print(f"Balance per Statement={balance_per_statement}; Balance per Books={balance_per_books}")

    if balance_per_statement < 0:
        raise ArithmeticError("Cannot be negative")
    elif balance_per_statement > balance_per_books:
        raise Exception("Schedules cannot be reconciled")
    else:
        print(f"Successfully reconciled {account}")


def get_books_schedule_for_account(account):
    print(f"Getting Books Schedule for account {account}")
    # Generate some random figures
    balance_per_books = random.randint(-10000, 10000)
    nfs_checks_and_fees = random.randint(-100, 0)
    bank_service_charges = random.randint(-100, 0)
    check_printing_charges = random.randint(-100, 0)
    interest_earned = random.randint(0, 100)
    note_receivable = random.randint(0, 1000)
    errors = random.randint(1, 5)
    
    books_schedule =  {
                "books_schedule": {
                    "balance_per_books": balance_per_books,
                    "adjustments": {
                        "bank_service_charges": bank_service_charges,
                        "nfs_checks_and_fees": nfs_checks_and_fees,
                        "check_printing_charges":check_printing_charges,
                        "interest_earned": interest_earned,
                        "note_receivable": note_receivable,
                        "errors": errors
                    }
                }
            }
    
    return books_schedule["books_schedule"]