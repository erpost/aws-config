# Deploys AWS Config to all Regions #

- Enable AWS Config in one Region using the [Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
    - You will be prompted to create a new AWS Bucket
    - You will be prompted to create a new IAM Role
- Run config-deploy.py
    - Input 'all' to select all AWS Regions
    - Input AWS Bucket from above
    - Input IAM Role from above

That's it! The script will deploy and enable Config in all Regions.

Additional scripts available:
- config_remove.py: Removes AWS Config from one or all Regions
- config_status.py: Obtains a status of AWS Config in one or all Regions
- config_rule_deploy.py: Deploys AWS Managed Config Rule
- config_rule_remove.py: Removes AWS Managed Config Rule
- config_rule_status.py: Obtains a status of an AWS Managed Config Rule

- config_deploy_with_workaround.py: Workaround from AWS to support to remove 'Config Rule Splash Screen'
    - Currently Not Working