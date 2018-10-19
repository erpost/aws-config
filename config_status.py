import boto3
from aws import get_regions


def get_recorder(region):
    client = boto3.client('config', region_name=region)
    response = client.describe_configuration_recorders()

    return response


def get_channel(region):
    client = boto3.client('config', region_name=region)
    response = client.describe_delivery_channels()

    return response


def get_recorder_status(region):
    client = boto3.client('config', region_name=region)
    response = client.describe_configuration_recorder_status()

    return response


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    region_selection = input('\nChoose a Region to see a status of Config or'
                             ' type "all" to deploy Config from all Regions: ')

    if region_selection.lower() == 'all':
        for aws_region in aws_regions:
            print('*' * 15, aws_region, '*' * 15)
            recorder = get_recorder(aws_region)
            if len(recorder['ConfigurationRecorders']) == 0:
                print('No Config Resources Available')
            else:
                print('Recorder Name:\t', recorder['ConfigurationRecorders'][0]['name'])
                print('Recorder ARN:\t', recorder['ConfigurationRecorders'][0]['roleARN'])
                channel = get_channel(aws_region)
                print('Channel Name:\t', channel['DeliveryChannels'][0]['name'])
                print('Channel Bucket:\t', channel['DeliveryChannels'][0]['s3BucketName'])
                status = get_recorder_status(aws_region)
                print('Recording:\t\t', status['ConfigurationRecordersStatus'][0]['recording'])
    else:
        if region_selection not in aws_regions:
            print('Invalid Region: {}'.format(region_selection))
        else:
            recorder = get_recorder(region_selection)
            if len(recorder['ConfigurationRecorders']) == 0:
                print('No Config Resources Available')
            else:
                print('Recorder Name:\t', recorder['ConfigurationRecorders'][0]['name'])
                print('Recorder ARN:\t', recorder['ConfigurationRecorders'][0]['roleARN'])
                channel = get_channel(region_selection)
                print('Channel Name:\t', channel['DeliveryChannels'][0]['name'])
                print('Channel Bucket:\t', channel['DeliveryChannels'][0]['s3BucketName'])
                status = get_recorder_status(region_selection)
                print('Recording:\t\t', status['ConfigurationRecordersStatus'][0]['recording'])
