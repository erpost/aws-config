import boto3


def get_regions():
    client = boto3.client('ec2')
    response = client.describe_regions()
    regions = []
    for region in response['Regions']:
        regions.append(region['RegionName'])

    return regions


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

    selection = input('\nChoose a Region to see a status of Config or'
                      ' type "all" to deploy Config from all Regions: ')

    if selection.lower() == 'all':
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
        if selection not in aws_regions:
            print('Invalid Region: {}'.format(selection))
        else:
            recorder = get_recorder(selection)
            if len(recorder['ConfigurationRecorders']) == 0:
                print('No Config Resources Available')
            else:
                print('Recorder Name:\t', recorder['ConfigurationRecorders'][0]['name'])
                print('Recorder ARN:\t', recorder['ConfigurationRecorders'][0]['roleARN'])
                channel = get_channel(selection)
                print('Channel Name:\t', channel['DeliveryChannels'][0]['name'])
                print('Channel Bucket:\t', channel['DeliveryChannels'][0]['s3BucketName'])
                status = get_recorder_status(selection)
                print('Recording:\t\t', status['ConfigurationRecordersStatus'][0]['recording'])
