import boto3
from aws import get_regions
from botocore.exceptions import ClientError, ParamValidationError


def del_rule(region, config_rule):
    try:
        client = boto3.client('config', region_name=region)
        response = client.delete_config_rule(
            ConfigRuleName=config_rule
        )

        print('Rule removed: \'{}\''.format(config_rule))

        return response

    except ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchConfigRuleException':
            print('Config Rule does not exist in region: {}'.format(region))

        else:
            print('\nUnknown error: ', err.response)
            return err.response['Error']['Message']

    except ParamValidationError:
        print('\nNo Config Name entered. Exiting..')


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    region_selection = input('\nChoose a Region to delete a Config Rule or'
                             ' type "all" to delete a Config Rule in all Regions: ')

    rule_selection = input('\nInput a Config Rule Name to delete: ')

    if region_selection.lower() == 'all':
        for aws_region in aws_regions:
            print('*' * 15, aws_region, '*' * 15)
            del_rule(aws_region, rule_selection)

    else:
        if region_selection not in aws_regions:
            print('Invalid Region: {}'.format(region_selection))
        else:
            del_rule(region_selection, rule_selection)
