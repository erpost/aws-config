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
- config-remove.py: Removes AWS Config from one or all Regions
- config-status.py: Obtains a status of AWS Config in one or all Regions