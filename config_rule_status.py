import boto3
from aws import get_regions


def get_rules(region):
    client = boto3.client('config', region_name=region)
    response = client.describe_config_rules()

    return response


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)

    selection = input('\nChoose a Region from above to see all Config Rules'
                      ' or type "all" to deploy Config from all Regions: ')

    if selection.lower() == 'all':
        for aws_region in aws_regions:
            print('*' * 15, aws_region, '*' * 15)
            rules = get_rules(aws_region)
            if len(rules['ConfigRules']) == 0:
                print('No Config Rules Implemented')
            else:
                n = 1
                answer = get_rules(aws_region)
                rules = answer['ConfigRules']
                for rule in rules:
                    print('Config Rule {}'.format(n))
                    print('Name:\t', rule['ConfigRuleName'])
                    print('ARN:\t', rule['ConfigRuleArn'])
                    print('State:\t', rule['ConfigRuleState'], '\n')
                    n += 1

    else:
        if selection not in aws_regions:
            print('Invalid Region: {}'.format(selection))
        else:
            rules = get_rules(selection)
            if len(rules['ConfigRules']) == 0:
                print('No Config Rules Implemented')
            else:
                n = 1
                answer = get_rules(selection)
                rules = answer['ConfigRules']
                for rule in rules:
                    print('Config Rule {}'.format(n))
                    print('Name:\t', rule['ConfigRuleName'])
                    print('ARN:\t', rule['ConfigRuleArn'])
                    print('State:\t', rule['ConfigRuleState'], '\n')
                    n += 1
