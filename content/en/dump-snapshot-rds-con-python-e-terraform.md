---
date: 2018-10-31
title: Dump your db from AWS RDS snapshot with Python and Terraform
slug: dump-rds-snapshot-to-sql-python-terraform
lang: en
cover: images/AWS-Feature.png
status: published
canonical: https://medium.com/@simmessa/fare-un-dump-da-uno-snapshot-rds-con-python-e-terraform-7cbd026fc
category: Tech
Tags: AWS Cloud, RDS, MySQL, Terraform, Python
---

Okay, all of you already know about Amazon cloud prowess, so I won't bore you with the details. If your instances are on AWS it's very probable you're already using their *db engine as a service*, or **RDS*** (which stands for Relational Database Service).

*Repost of article first appeared on [Medium](https://medium.com/@simmessa/fare-un-dump-da-uno-snapshot-rds-con-python-e-terraform-7cbd0fa026fc)*

Today we are talking about a useful hack for those who use this service, and specifically, we will go to see how to create a classic db dump ( .sql format) from a database instance.

## But don't backups already exist?

RDS, among the many interesting things, offers the functionality of having automatic backups, and if you have tried it you already know it is really convenient. At any time you can restore an existing snapshot or even create a new instance of the database, of which to choose the size (understood as "power" of the server), going to fish from the snapshot data.

![RDS has good backups, but they are not the sql dumps that serve us...](. /images/webp/RDS_snapshot.webp)
*RDS has good backups, but it's not the kind of sql dumps we need...*

I often thought that these backups were already what I needed, i.e. a way like another to dump the db in compressed sql file to duplicate a service, unfortunately I realized at my expense that is not so simple, especially if you want to automate the process and you want to find the way to risk as little as possible with a live db in production.

The juice of the speech is that, on RDS, it is extremely easy to duplicate a database by snapshot and creating a new instance, but the portability level of this kind of "dump" is practically null, is only valid on RDS.

On the contrary, if you want to get a dump is not so trivial.

## The basic method

The process is quite simple:

- We create a snapshot
- We launch a new instance of "small" db (e.g. a db.t2.micro, with 1 vCPU and 1 Gb of RAM) by selecting as source the snapshot that interests us
- We connect **mysqldump*** to the new instance and produce the database dump we need

Do it manually every time, however, I find it palloetto, so I looked for (thank you Google!) and processed a more smart and automatic method of doing it

## Some LIVE shortcomings

If by chance you want to have the dump of a production database and want to avoid problems, also satisfying you with not very fresh data, I recommend you to start setting up backup jobs/creation of snapshots in the band where you have fewer accesses to your service, it may be at night, but it is up to you to discover it and, in any case, if it is a public service Google Analytics is your friend, otherwise good search in logs.

## The Terraform + Python script method

As a premise, please note you'll find the sample code of this article on my profile [github](https://github.com/simmessa/rds_snaptodump). Having sorted that out, let's now see together what we have to do to go to create the dump this way.

Before continuing please clone the repo and enter with:

```
$ git clone https://github.com/simmessa/rds_snaptodump
cd rds_snaptodump
```

### Some prerequisites

To run the repository files you need:

- terraform (for installation see below)
- mysqldump
- an AWS account with the privileges needed to interact with RDS (reading, database lists, etc.) (motr information below)
- python 2 (I tested with version 2.7.12)

### Install Terraform

First, I suggest you install [Terraform](https://www.terraform.io), it is a tool made by the sympathetic [Hashicorp] gentlemen (https://www.hashicorp.com/) who is very useful and will open a world about how to create command-line cloud infrastructure, but, of course, this article does not allow us to deepen the subject.

Know at least that, with terraform, you can launch commands that will define, based on scripts, cloud environments on AWS, GKE or other environments.

I have no idea if Terraform is bundled thanks to the pkg manager of your favorite Linux distro (or maybe on [WSL](https://medium.com/@simmessa/install-un-ambiente-di-sviluppo-linux-su-windows-10-wsl-fc638bb4ff8e) under windows 10), but if you need to install it from the command line the procedure is very simple, go [here](https://www.terraform.io/downloads.html), download the right binary and then unzip it where you need it:

```
$ wget https://releases.hashicorp.com/terraform/0.11.10/terraform_0.11.10_linux_amd64.zip; unzip terraform_0.11.10_linux_amd64.zip
```

Is that done? Great! At this point you should find yourself with the terraform binary available and inside the previously cloned github repository.

To check the terraform install, just try to run terraform via cli:

```
./terraform
Usage: terraform [-version] [-help] <command> [args]

The available commands for execution are listed below.
The most common, useful commands are shown first, followed by
less common or more advanced commands. If you're just getting
started with Terraform, stick with the common commands. For the
other commands, please read the help and docs before usage.

Common commands:
    apply              Builds or changes infrastructure
    console            Interactive console for Terraform interpolations
    destroy            Destroy Terraform-managed infrastructure
    env                Workspace management
    fmt                Rewrites config files to canonical format
    get                Download and install modules for the configuration
    graph              Create a visual graph of Terraform resources
    import             Import existing infrastructure into Terraform
    init               Initialize a Terraform working directory
    output             Read an output from a state file
    plan               Generate and show an execution plan
    providers          Prints a tree of the providers used in the configuration
    push               Upload this Terraform module to Atlas to run
    refresh            Update local state file against real resources
    show               Inspect Terraform state or plan
    taint              Manually mark a resource for recreation
    untaint            Manually unmark a resource as tainted
    validate           Validates the Terraform files
    version            Prints the Terraform version
    workspace          Workspace management

All other commands:
    debug              Debug output management (experimental)
    force-unlock       Manually unlock the terraform state
    state              Advanced state management
```

If your output is like what you see above you are fine, terraform should be ready to be used.

### Editing the main.tf script

Now that you have Terraform available you will have to edit the script we will use to create the instance of our database to get the dump.

It's called main.tf and you'll find it below:

```
provider "aws" {
  region = "eu-west-1" # put your AWS region here!
}

# Get latest snapshot from production DB
data "aws_db_snapshot" "latest_prod_snapshot" {
    most_recent = true
    db_instance_identifier = "mydbname" # put the name of your db here!
}
# Create new staging DB
resource "aws_db_instance" "db_snapshot_dumper" {
  instance_class       = "db.t2.micro"
  identifier           = "db-snapshot-dumper"
  username             = "user" # necessary, but won't be used since a snapshot identifier is provided...
  password             = "password" # necessary, but won't be used since a snapshot identifier is provided...
  snapshot_identifier  = "${data.aws_db_snapshot.latest_prod_snapshot.id}"
  #vpc_security_group_ids = ["sg-12345678"] # if you are running inside a VPC uncomment and put yours here
  skip_final_snapshot = true # Won't produce a final snapshot when disposing of db
}

output "address" {
  value = "${aws_db_instance.db_snapshot_dumper.address}"
}

output "snapshot" {
  value = "${aws_db_instance.db_snapshot_dumper.snapshot_identifier}"
}
```

There are various things you will need to change to suit your specific case, such as the AWS region where you're going to use the RDS service:

```
provider "aws" {
  region = "eu-west-1" # put your AWS region here!
}
[...]
```

and the id of your database, as shown in the RDS panel:

```
[...]
# Get latest snapshot from production DB
data "aws_db_snapshot" "latest_prod_snapshot" {
    most_recent = true
    db_instance_identifier = "mydbname" # put the name of your db here!
}
[...]
```

Finally, if your cloud infrastructure provides a vpc, I recommend you to uncomment the appropriate line and enter the id of your vpc:

```
[...]
  #vpc_security_group_ids = ["sg-12345678"] # if you are running inside a VPC uncomment and put yours here
[...]
```

I would like to take this opportunity to point out that we did not have to give Terraform the id of a specific snapshot, on the contrary, we asked him to use the latest available snapshot (most_recent = true):

```
[...]
# Get latest snapshot from production DB
data "aws_db_snapshot" "latest_prod_snapshot" {
    most_recent = true
    db_instance_identifier = "mydbname" # put the name of your db here!
}
[...]
```

I find it wonderful, for my purposes, but if you need a specific snapshot, I refer you to the pretty decent [Terraform docs page](https://www.terraform.io/docs/providers/aws/db_snapshot.html) for the fine details.

Once we do this we can switch to the Python part of our dumper.

### Edit the Python snaptodump.py script

The script "snaptodump.py" in its "original" form can be found below:

```
#Python

from sys import argv
from datetime import datetime

import sys, os, os.path

start_time = datetime.now()

# MySQL setup: put the MySQL user with dump permission and database name here
# password will be asked interactively later: 

dbusr = "your_mysql_username" 
dbname = "your_mysql_database_name"

print """

This script will launch Terraform to dump the latest snapshot of prod db

PREREQUISITES:

You need AWS tokens setup as ENV vars or Terraform won't work:
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="yyy"

USAGE:

python snaptodump.py

*** WARNING ***
This tool requires the mysqldump binary installed on your system and the necessary free space on your local disk for dumping!

"""

terraform_init_dir = "./.terraform"

if os.path.exists(terraform_init_dir):
    print "terraform init already ran!\n"
else:
    os.system( "./terraform init")

if ( os.system( "./terraform apply") != 0 ):
    print "*** ERROR while applying terraform config, dumping stopped! ***"
    exit()

host = os.popen('./terraform output address').read()
filename = os.popen('./terraform output snapshot').read() + ".sql.gz"

dumpcmd = "mysqldump -h %s -u %s --compress -p %s |gzip > %s" % (host.replace('\n',''), dbusr, dbname, filename.replace('\n',''))

print "Next step is mysqldump, you will be asked for a MySQL password\n"

dbdump_start = datetime.now()

if os.system( dumpcmd ):
    print "An error occurred!"
    print "command was: %s" % dumpcmd
else:
    print "All done!"
    print "Db dumped in %s" % ( datetime.now() - dbdump_start )

#Now let's destroy our temp RDS instance
os.system( "./terraform destroy ")

#Feeling bold? comment previous command and enable this!
#os.system( "./terraform destroy -auto-approve"

print "Total procedure completed in %s\n" % ( datetime.now() - start_time )

#print dumpcmd
```
[...]
dbusr = "your_mysql_username"
dbname = "your_mysql_database_name"
[...]
``

will become, for example:

``
[...]
dbusr = "pete"
dbname = "dbproduction"
[...]
``

At this point, if you try to launch the script:

```
$ python snaptodump.py
```

You will notice that, in order to work, it needs the AWS authentication part, without which Terraform cannot dialogue with AWS.

### Authentication and AWS access keys

To interact with the AWS cloud, you need to define two system variables, containing your RDS credentials:

```
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="yyyy"
```

**WARNING: Do not run the script using credentials with all permissions (such as root account) or in any case with credentials higher than those strictly necessary to dump RDS**

By running Terraform with all AWS privileges you might literally erase your environment in the cloud, so I thought I'd put the notice above. You've been warned!

In this respect, since I lost some time, it seems only appropriate to define what these AWS IAM permits are necessary for the execution of the dump, let's see them together.

First of all, I created a user and a specific group, the necessary permissions are obviously defined within the group, so that they can be applied faster to a new future user.

The group name is "db_dumpers". I then created the policies necessary to interact with RDS, specifically two of them.

The first is part of AmazonRDS's pre-configured policies, and it's called:

"AmazonRDSReadOnlyAccess"

in json, the content looks like this:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "rds:Describe*",
        "rds:ListTagsForResource",
        "ec2:DescribeAccountAttributes",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeInternetGateways",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcAttribute",
        "ec2:DescribeVpcs"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "cloudwatch:GetMetricStatistics",
        "logs:DescribeLogStreams",
        "logs:GetLogEvents"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

As you can see, in addition to RDS this policy contains some useful privileges for ec2, including sub-networks, security groups and VPC, which are also allowed for cloudwatch logging. All of it, of course, in read only mode.

In addition to this policy, I had to create a second, custom policy, to allow action on the RDS service:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "rds:RestoreDBInstanceFromDBSnapshot",
        "rds:CreateDBInstance",
        "rds:ModifyDBInstance",
        "rds:DeleteDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:*:*:snapshot:*",
        "arn:aws:rds:*:*:secgrp:*",
        "arn:aws:rds:*:*:subgrp:*",
        "arn:aws:rds:*:*:og:*",
        "arn:aws:rds:eu-west-1:123456789012:db:db-snapshot-dumper",
        "arn:aws:rds:*:*:pg:*"
      ]
    }
  ]
}
```

As you can see, here we have the opportunity to create new instances of RDS, edit them, delete them and then restore snapshot data.

For further safety, I have limited RDS permissions only to some ARN (which are Amazon resource identifiers) specific to the environment on which I am operating, because I want this user to not touch or harm my main db.

If you do it, there is a match between the instance that terraform creates to assign the snapshot and the ARN that I defined in the policy.

From the main.tf script:

```
[...]
identifier           = "db-snapshot-dumper"
[...]
```

While from the above-defined AWS policy:

```
[...]
      "Resource": [
        "arn:aws:rds:*:*:snapshot:*",
        "arn:aws:rds:*:*:secgrp:*",
        "arn:aws:rds:*:*:subgrp:*",
        "arn:aws:rds:*:*:og:*",
        "arn:aws:rds:eu-west-1:123456789012:db:db-snapshot-dumper",
        "arn:aws:rds:*:*:pg:*"
      ]
[...]
```

Once you create the two policies you will just assign them to the group "db_dumpers" and then return your user, of which you will have kept the credentials.

### Launch the script

At this point we have prepared everything and we just have to launch the script:

```
$ python snaptodump.py
```

You should find, within a few hours, in the same folder where you launched the script, a file with your db dump, with the desired .sql.gz format

If something went wrong, you will receive an error message from the script or terraform instead.

Thank you for your attention, of course in case of problems or possible improvements, do not hesitate to comment below.

p.s.: sorry no more comments (editor note)
