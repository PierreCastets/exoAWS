import boto3

numVM = input("Entrez le nombre de VM à instancier: ")

client = boto3.client('ec2', region_name='eu-central-1')

for i in numVM:
    response = client.run_instances(
        ImageId='ami-0a49b025fffbbdac6',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[
            {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'exo',
                    'Value': 'formation'
                }
            ]
            }
        ],
        UserData='''
        #!/bin/bash
        apt-get update -y
        apt-get install docker-engine -y
        systemctl start docker
        docker run -d apache2
        '''
        
    )

response = client.describe_instances(Filters=[{'Name': 'tag:exo', 'Values': ['formation']}, {'Name': 'instance-state-name', 'Values': ['running']}])
instancesId = []
instancesIpAddress = []

for i in range(len(response['Reservations'])):
    instancesId.append(response['Reservations'][i]['Instances'][0]['InstanceId'])
    instancesIpAddress.append(response['Reservations'][i]['Instances'][0]['PublicIpAddress'])

with open("instancesId.txt", "w") as file:
    for id in instancesId:
        file.write(id + '\n')

with open("instancesIpAddress.txt", "w") as file:
    for ip in instancesIpAddress:
        file.write(ip + '\n')  

