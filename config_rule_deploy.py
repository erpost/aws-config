import boto3
from aws import get_regions
from botocore.exceptions import ClientError, ParamValidationError


def put_rule(region, rule_name, rule_identifier):
    try:
        client = boto3.client('config', region_name=region)
        response = client.put_config_rule(
            ConfigRule={
                'ConfigRuleName': rule_name,
                'Source': {
                    'Owner': 'AWS',
                    'SourceIdentifier': rule_identifier
                }
            }
        )

        print('Rule deployed:', region)

        return response

    except ParamValidationError as err:
        print(err)
        exit(1)

    except ClientError as err:
        error_code = err.response['Error']['Code']
        if error_code == 'InvalidParameterValueException':
            print('Invalid AWS Rule ID: {}'.format(rule_identifier))

        elif error_code == 'NoAvailableConfigurationRecorderException':
            print('No configured Recorder')

        else:
            print('ClientError: {}'.format(err))


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    region_selection = input('\nChoose a Region from above to deploy a Config Rule'
                             ' or type "all" to deploy Config from all Regions: ')

    rule_selection = input('\nChoose an AWS Rule Name: ')

    rule_id = input('\nInput an AWS Rule ID: ')

    if region_selection.lower() == 'all':
        for aws_region in aws_regions:
            put_rule(aws_region, rule_selection, rule_id)

    else:
        if region_selection not in aws_regions:
            print('Invalid Region: {}'.format(region_selection))
        else:
            put_rule(region_selection, rule_selection, rule_id)
