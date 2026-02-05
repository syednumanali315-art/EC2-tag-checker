import boto3

# NEW SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:958315858143:xyz"

# Tags that must exist on every EC2 instance
REQUIRED_TAGS = ["Name", "Environment", "Owner"]

def lambda_handler(event, context):
    ec2 = boto3.client("ec2", region_name="us-east-1")
    sns = boto3.client("sns", region_name="us-east-1")

    response = ec2.describe_instances()
    non_compliant = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]

            # Convert EC2 tags list to dictionary
            tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}

            # Check missing tags
            missing_tags = [tag for tag in REQUIRED_TAGS if tag not in tags]

            if missing_tags:
                non_compliant.append(
                    f"InstanceId: {instance_id} | Missing tags: {', '.join(missing_tags)}"
                )

    # Send alert only if missing tags found
    if non_compliant:
        message = (
            "🚨 EC2 Tag Compliance Alert 🚨\n\n"
            "The following EC2 instances are missing required tags:\n\n"
            + "\n".join(non_compliant)
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Instances Missing Tags",
            Message=message
        )

        return {
            "statusCode": 200,
            "body": "Alert sent successfully"
        }

    return {
        "statusCode": 200,
        "body": "All EC2 instances have required tags"
    }
