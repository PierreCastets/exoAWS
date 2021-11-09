import boto3

instancesId = []
with open('instancesId.txt', 'r') as file:
    for line in file:
        instancesId.append(line)

ec2 = boto3.resource('ec2')
for id in instancesId:
    instance = ec2.Instance(id.strip('\n'))
    instance.terminate()