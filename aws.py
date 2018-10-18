import boto3


def get_regions():
    client = boto3.client('ec2')
    response = client.describe_regions()
    regions = []
    for region in response['Regions']:
        regions.append(region['RegionName'])

    return regions


if __name__ == "__main__":
    aws_regions = get_regions()
    for aws_region in aws_regions:
        print(aws_region)
