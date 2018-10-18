import boto3
from aws import get_regions
from botocore.exceptions import ClientError


def del_recorder(region):
    try:
        client = boto3.client('config', region_name=region)
        response = client.delete_configuration_recorder(
            ConfigurationRecorderName='default'
        )
        print('Recorder removed for region: {}'.format(region))

        return response

    except ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchConfigurationRecorderException':
            print('No Recorder configured for region: {}'.format(region))

        else:
            print('\nUnknown error: ', err.response)
            return err.response['Error']['Message']


def del_channel(region):
    try:
        client = boto3.client('config', region_name=region)
        response = client.delete_delivery_channel(
            DeliveryChannelName='default'
        )
        print('Delivery Channel removed for region: {}'.format(region))

        return response

    except ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchDeliveryChannelException':
            print('No Delivery Channel configured for region: {}'.format(region))

        else:
            print('\nUnknown error: ', err.response)
            return err.response['Error']['Message']


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)
    selection = input('\nChoose a Region from above to remove Config'
                      ' or type "all" to remove Config from all Regions: ')
    if selection.lower() == 'all':
        for aws_region in aws_regions:
            del_recorder(aws_region)
            del_channel(aws_region)

    else:
        if selection not in aws_regions:
            print('Invalid Region: {}'.format(selection))
        else:
            del_recorder(selection)
            del_channel(selection)
