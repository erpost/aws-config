import boto3


def get_regions():
    client = boto3.client('ec2')
    response = client.describe_regions()
    regions = []
    for region in response['Regions']:
        regions.append(region['RegionName'])

    return regions


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


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    selection = input('\nChoose a Region from above to deploy Config'
                      ' or type "all" to deploy Config from all Regions: ')
    s3_bucket = input('Please input the S3 bucket: ')
    role_arn = input('Please input the Role ARN: ')

    if selection.lower() == 'all':
        for aws_region in aws_regions:
            print('*' * 15, aws_region, '*' * 15)
            if get_recorder_status(aws_region) == 0:
                put_recorder(aws_region)
                put_channel(aws_region)
                start_recorder(aws_region)
            else:
                print('Already deployed: ', aws_region)

    else:
        if selection not in aws_regions:
            print('Invalid Region: {}'.format(selection))
        else:
            if get_recorder_status(selection) == 0:
                put_recorder(selection)
                put_channel(selection)
                start_recorder(selection)
            else:
                print('Already deployed: ', selection)
