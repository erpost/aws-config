import boto3
import sys, time
from aws import get_regions
from config_rule_deploy import put_rule
from config_rule_remove import del_rule


def get_recorder_status(region):
    client = boto3.client('config', region_name=region)
    response = client.describe_configuration_recorder_status()
    recorder_length = len(response['ConfigurationRecordersStatus'])

    return recorder_length


def put_recorder(region):
    client = boto3.client('config', region_name=region)
    response = client.put_configuration_recorder(
        ConfigurationRecorder={
            'name': 'default',
            'roleARN': role_arn,
            'recordingGroup': {
                'allSupported': True,
                'includeGlobalResourceTypes': True
            }
        }
    )
    print('Deployed Recorder: ', region)

    return response


def put_channel(region):
    client = boto3.client('config', region_name=region)
    response = client.put_delivery_channel(
        DeliveryChannel={
            'name': 'default',
            's3BucketName': s3_bucket
        }
    )
    print('Deployed Channel: ', region)

    return response


def start_recorder(region):
    client = boto3.client('config', region_name=region)
    response = client.start_configuration_recorder(
        ConfigurationRecorderName='default'
    )
    print('Started Recorder: ', region)

    return response


def progress_dots():
    for i in range(30):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print('\n')


if __name__ == "__main__":
    rule_name = 'rds-storage-encrypted'
    rule_id = 'RDS_STORAGE_ENCRYPTED'

    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    region_selection = input('\nChoose a Region from above to deploy Config'
                             ' or type "all" to deploy Config from all Regions: ')
    s3_bucket = input('Please input the S3 bucket: ')
    role_arn = input('Please input the Role ARN: ')

    if region_selection.lower() == 'all':
        for aws_region in aws_regions:
            print('*' * 15, aws_region, '*' * 15)
            if get_recorder_status(aws_region) == 0:
                put_recorder(aws_region)
                put_channel(aws_region)
                start_recorder(aws_region)
                put_rule(aws_region, rule_name, rule_id)
                progress_dots()
                del_rule(aws_region, rule_name)

            else:
                print('Already deployed: ', aws_region)

    else:
        if region_selection not in aws_regions:
            print('Invalid Region: {}'.format(region_selection))
        else:
            if get_recorder_status(region_selection) == 0:
                put_recorder(region_selection)
                put_channel(region_selection)
                start_recorder(region_selection)
                put_rule(region_selection, rule_name, rule_id)
                progress_dots()
                del_rule(region_selection, rule_name)

            else:
                print('Already deployed: ', region_selection)
