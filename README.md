# Functions to deploy AWS Config to all Regions #

- Enable AWS Config in one Region using the [Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
    - Create new AWS Bucket
    - Create new IAM Role
- Run config-deploy.py
    - Select All Regions
    - Input AWS Bucket from above
    - Input IAM Role from above

That's it! The script will deploy and enable Config in all Regions.