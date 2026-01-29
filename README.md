# AWS Learning Journey

## Table of Contents

1. [Introduction to Cloud Computing](#1-introduction-to-cloud-computing)
2. [Cloud Service Models (IaaS, PaaS, SaaS)](#2-cloud-service-models)
3. [Cloud Deployment Models](#3-cloud-deployment-models)
4. [Getting Started with AWS](#4-getting-started-with-aws)
5. [AWS Global Infrastructure](#5-aws-global-infrastructure)
6. [AWS Identity and Access Management (IAM)](#6-aws-iam)
7. [AWS EC2 - Virtual Servers](#7-aws-ec2)
8. [AWS Storage Solutions](#8-aws-storage-solutions)
9. [AWS S3 - Object Storage](#9-aws-s3)
10. [Working with S3 SDK](#10-working-with-s3-sdk)
11. [AWS Lambda - Serverless Computing](#11-aws-lambda)
12. [AWS Glue & Data Cataloging](#12-aws-glue)
13. [Building ETL Pipelines](#13-etl-pipelines)
14. [AWS Athena - Query Data](#14-aws-athena)

---

## 1. Introduction to Cloud Computing

### What is Cloud Computing?

Cloud computing is the delivery of computing services (servers, storage, databases, networking, software) over the internet ("the cloud") on a pay-as-you-go basis.

**Traditional IT vs Cloud:**

```style
Traditional IT (On-Premises)          Cloud Computing
┌─────────────────────┐              ┌─────────────────────┐
│ Your Data Center    │              │   Cloud Provider    │
│                     │              │                     │
│ ┌─────────────┐     │              │ ┌─────────────┐     │
│ │  Servers    │     │              │ │  Servers    │     │
│ │  (Buy/Own)  │     │              │ │  (Rent)     │     │
│ └─────────────┘     │              │ └─────────────┘     │
│ ┌─────────────┐     │              │ ┌─────────────┐     │
│ │  Storage    │     │              │ │  Storage    │     │
│ └─────────────┘     │              │ └─────────────┘     │
│ ┌─────────────┐     │              │ ┌─────────────┐     │
│ │  Network    │     │              │ │  Network    │     │
│ └─────────────┘     │              │ └─────────────┘     │
│                     │              │                     │
│ High Upfront Cost   │              │ Pay-As-You-Go       │
│ Fixed Capacity      │              │ Scalable            │
│ Manual Maintenance  │              │ Managed Service     │
└─────────────────────┘              └─────────────────────┘
```

### Why Cloud Computing?

#### Key Benefits

1. **Cost Savings**
   - No upfront hardware costs
   - Pay only for what you use
   - Reduce operational expenses

2. **Scalability**
   - Scale up during high demand
   - Scale down during low demand
   - Automatic or manual scaling

3. **Speed & Agility** ⚡
   - Deploy resources in minutes
   - Quick experimentation
   - Faster time to market

4. **Global Reach**
   - Deploy worldwide in minutes
   - Lower latency for users
   - Disaster recovery across regions

5. **Reliability**
   - Built-in redundancy
   - Automatic backups
   - High availability

6. **Security**
   - Enterprise-grade security
   - Compliance certifications
   - Regular security updates

### Real-World Analogy

Think of cloud computing like electricity:

- **Old way**: Generate your own power (buy generators, maintain them)
- **New way**: Plug into the grid (pay for what you use, no maintenance)

---

## 2. Cloud Service Models

Cloud services are typically categorized into three main models:

### Visual Representation

```style
┌─────────────────────────────────────────────────────────────┐
│                    RESPONSIBILITY MATRIX                    │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  Component   │  On-Premises │     IaaS     │  PaaS  │  SaaS │
├──────────────┼──────────────┼──────────────┼────────┼───────┤
│ Applications │     YOU      │     YOU      │  YOU   │ VENDOR│
│ Data         │     YOU      │     YOU      │  YOU   │ VENDOR│
│ Runtime      │     YOU      │     YOU      │ VENDOR │ VENDOR│
│ Middleware   │     YOU      │     YOU      │ VENDOR │ VENDOR│
│ OS           │     YOU      │     YOU      │ VENDOR │ VENDOR│
│ Virtualization│    YOU      │    VENDOR    │ VENDOR │ VENDOR│
│ Servers      │     YOU      │    VENDOR    │ VENDOR │ VENDOR│
│ Storage      │     YOU      │    VENDOR    │ VENDOR │ VENDOR│
│ Networking   │     YOU      │    VENDOR    │ VENDOR │ VENDOR│
└──────────────┴──────────────┴──────────────┴────────┴───────┘
```

### IaaS (Infrastructure as a Service)

**What you get**: Virtual machines, storage, networks
**What you manage**: OS, applications, data
**AWS Examples**: EC2, S3, VPC

```style
┌─────────────────────────────────────┐
│        IaaS Example: EC2            │
│                                     │
│  You Install & Manage:              │
│  ├── Your Application               │
│  ├── Database                       │
│  ├── Operating System               │
│  └── Security Patches               │
│                                     │
│  AWS Provides:                      │
│  ├── Virtual Machine                │
│  ├── Storage                        │
│  ├── Network                        │
│  └── Physical Hardware              │
└─────────────────────────────────────┘
```

**Use Case**: You want full control over your infrastructure
**Example**: Running a custom web server with specific configurations

### PaaS (Platform as a Service)

**What you get**: Development platform, databases, tools
**What you manage**: Applications and data
**AWS Examples**: Elastic Beanstalk, RDS, Lambda

```style
┌─────────────────────────────────────┐
│     PaaS Example: Elastic Beanstalk │
│                                     │
│  You Manage:                        │
│  ├── Your Application Code          │
│  └── Your Data                      │
│                                     │
│  AWS Manages:                       │
│  ├── Operating System               │
│  ├── Runtime Environment            │
│  ├── Server Management              │
│  ├── Scaling                        │
│  └── Load Balancing                 │
└─────────────────────────────────────┘
```

**Use Case**: Focus on coding, not infrastructure
**Example**: Deploy a Python web app without managing servers

### SaaS (Software as a Service)

**What you get**: Ready-to-use applications
**What you manage**: Your data and user access
**AWS Examples**: Amazon WorkDocs, Amazon Chime

```style
┌─────────────────────────────────────┐
│     SaaS Example: Gmail/Office365   │
│                                     │
│  You Use:                           │
│  ├── The Application                │
│  └── Store Your Data                │
│                                     │
│  Provider Manages Everything:       │
│  ├── Application Code               │
│  ├── Infrastructure                 │
│  ├── Updates                        │
│  ├── Security                       │
│  └── Availability                   │
└─────────────────────────────────────┘
```

**Use Case**: Just use the software
**Example**: Email, CRM, collaboration tools

---

## 3. Cloud Deployment Models

### Public Cloud

Resources owned and operated by third-party cloud service provider

```style
┌──────────────────────────────────────────┐
│        PUBLIC CLOUD                      │
│  ┌────────┐  ┌────────┐  ┌────────┐      │
│  │Company │  │Company │  │Company │      │
│  │   A    │  │   B    │  │   C    │      │
│  └───┬────┘  └───┬────┘  └───┬────┘      │
│      │           │           │           │
│      └───────────┼───────────┘           │
│                  │                       │
│         ┌────────▼────────┐              │
│         │  Shared Cloud   │              │
│         │  Infrastructure │              │
│         │  (AWS/Azure/GCP)│              │
│         └─────────────────┘              │
└──────────────────────────────────────────┘

Pros: Cost-effective, Scalable, No maintenance
Cons: Less control, Shared resources
```

**Examples**: AWS, Microsoft Azure, Google Cloud
**Best for**: Most businesses, startups, web applications

### Private Cloud

Resources used exclusively by one organization

```style
┌──────────────────────────────────────────┐
│       PRIVATE CLOUD                      │
│                                          │
│         ┌──────────────┐                 │
│         │  Company X   │                 │
│         └──────┬───────┘                 │
│                │                         │
│         ┌──────▼─────────┐               │
│         │  Dedicated     │               │
│         │  Cloud         │               │
│         │  Infrastructure│               │
│         └────────────────┘               │
│                                          │
│  (Can be on-premises or hosted)          │
└──────────────────────────────────────────┘

Pros: More control, Enhanced security, Customizable
Cons: Expensive, Requires maintenance
```

**Examples**: VMware Private Cloud, AWS Outposts
**Best for**: Government, healthcare, banking (high compliance needs)

### Hybrid Cloud

Combination of public and private clouds

```style
┌─────────────────────────────────────────────────┐
│            HYBRID CLOUD                         │
│                                                 │
│  ┌─────────────────┐      ┌─────────────────┐   │
│  │ Private Cloud   │◄────►│  Public Cloud   │   │
│  │                 │      │                 │   │
│  │ • Sensitive Data│      │ • Web Apps      │   │
│  │ • Core Systems  │      │ • Testing       │   │
│  │ • Compliance    │      │ • Burst Capacity│   │
│  └─────────────────┘      └─────────────────┘   │
│                                                 │
└─────────────────────────────────────────────────┘

Pros: Flexibility, Balance security & cost
Cons: Complex to manage
```

**Best for**: Enterprises with legacy systems and cloud applications

---

## 4. Getting Started with AWS

### Create Your AWS Free Tier Account

AWS provides a free tier that includes:

- **12 months free**: EC2, S3, RDS (limited usage)
- **Always free**: Lambda (1M requests/month), DynamoDB (25GB storage)
- **Free trials**: Many services offer short-term trials

#### Step-by-Step Account Setup

```style
┌─────────────────────────────────────────────────────────┐
│  STEP 1: Go to aws.amazon.com                          │
│  └─► Click "Create an AWS Account"                     │
│                                                         │
│  STEP 2: Provide Account Information                   │
│  ├─► Email address                                     │
│  ├─► Password (strong!)                                │
│  └─► AWS account name                                  │
│                                                         │
│  STEP 3: Contact Information                           │
│  ├─► Personal or Professional account                  │
│  ├─► Full name                                         │
│  ├─► Phone number                                      │
│  └─► Address                                           │
│                                                         │
│  STEP 4: Payment Information                           │
│  └─► Credit/Debit card (required, won't charge        │
│       unless you exceed free tier)                     │
│                                                         │
│  STEP 5: Identity Verification                         │
│  └─► Phone verification (automated call/SMS)          │
│                                                         │
│  STEP 6: Choose Support Plan                           │
│  └─► Select "Basic Support - Free"                    │
│                                                         │
│  STEP 7: Complete!                                     │
│  └─► Wait for confirmation email                       │
│  └─► Sign in to AWS Console                            │
└─────────────────────────────────────────────────────────┘
```

#### Important Security Steps After Account Creation

1. **Enable MFA (Multi-Factor Authentication)**

   ```path
   AWS Console → IAM → Dashboard → Activate MFA on root account
   ```

2. **Create IAM Users (Don't use root account for daily tasks)**

   ```path
   AWS Console → IAM → Users → Add User
   ```

3. **Set up Billing Alerts**

   ```path
   AWS Console → Billing → Billing Preferences → 
   Enable "Receive Billing Alerts" → Create Alarm in CloudWatch
   ```

#### Free Tier Usage Monitoring

```python
# Check your free tier usage regularly
# AWS Console → Billing → Free Tier

# Set up a budget alert
{
  "budget_name": "Monthly-Free-Tier-Alert",
  "budget_limit": "$10",
  "alert_threshold": "80%",
  "notification_email": "your-email@example.com"
}
```

---

## 5. AWS Global Infrastructure

AWS has a global network of data centers to provide low-latency access worldwide.

### Key Concepts

```infastructure
┌─────────────────────────────────────────────────────────┐
│         AWS GLOBAL INFRASTRUCTURE                       │
│                                                         │
│  REGIONS (Geographic areas)                             │
│  └─► Examples: us-east-1, eu-west-1, ap-south-1         │
│                                                         │
│      ├─► AVAILABILITY ZONES (Data centers)              │
│      │   └─► Each region has 2+ AZs                     │
│      │   └─► Isolated from each other                   │
│      │   └─► Connected with low-latency links           │
│      │                                                  │
│      └─► EDGE LOCATIONS (CDN points)                    │
│          └─► 400+ locations worldwide                   │
│          └─► Used by CloudFront (CDN)                   │
│          └─► Cache content closer to users              │
└─────────────────────────────────────────────────────────┘
```

### Visual Architecture

```architecture
                    GLOBAL
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    REGION 1      REGION 2      REGION 3
   (us-east-1)   (eu-west-1)   (ap-south-1)
        │             │             │
    ┌───┴───┐     ┌───┴───┐     ┌───┴───┐
    │       │     │       │     │       │
   AZ-a   AZ-b   AZ-a   AZ-b   AZ-a   AZ-b
    │       │     │       │     │       │
   [DC]   [DC]   [DC]   [DC]   [DC]   [DC]

Each AZ = Isolated Data Center
Regions = Multiple AZs (typically 3)
```

### Choosing a Region

**Factors to consider:**

1. **Latency** - Closer to your users = faster response
2. **Cost** - Pricing varies by region
3. **Compliance** - Data residency requirements
4. **Service Availability** - Not all services in all regions

```python
# Example: Popular AWS Regions

regions = {
    "us-east-1": {
        "name": "N. Virginia",
        "azs": 6,
        "note": "Most services launched here first, cheapest"
    },
    "us-west-2": {
        "name": "Oregon",
        "azs": 4,
        "note": "Good for US West Coast"
    },
    "eu-west-1": {
        "name": "Ireland",
        "azs": 3,
        "note": "Primary European region"
    },
    "ap-south-1": {
        "name": "Mumbai",
        "azs": 3,
        "note": "India region"
    }
}
```

### High Availability Example

```
┌───────────────────────────────────────────────┐
│  Multi-AZ Deployment for High Availability    │
│                                               │
│         Load Balancer (Across AZs)            │
│                    │                          │
│         ┌──────────┴──────────┐               │
│         │                     │               │
│    ┌────▼────┐          ┌────▼────┐           │
│    │  AZ-1a  │          │  AZ-1b  │           │
│    │         │          │         │           │
│    │ [APP]   │          │ [APP]   │           │
│    │ [DB]    │◄────────►│ [DB]    │           │
│    │         │   Sync   │         │           │
│    └─────────┘          └─────────┘           │
│                                               │
│  If AZ-1a fails → AZ-1b continues serving     │
└───────────────────────────────────────────────┘
```

---

## 6. AWS IAM

**IAM (Identity and Access Management)** controls who can access your AWS resources and what they can do.

### Core Concepts

```
┌─────────────────────────────────────────────────┐
│              IAM HIERARCHY                      │
│                                                 │
│  ROOT USER (Created at signup)                  │
│  └─► Has complete access to everything          │
│  └─► Should NOT be used for daily tasks         │
│  └─► Enable MFA immediately!                    │
│                                                 │
│  IAM USERS (Individual people/services)         │
│  └─► Has username and password                  │
│  └─► Can have access keys for API/CLI           │
│                                                 │
│  IAM GROUPS (Collection of users)               │
│  └─► Apply policies to multiple users           │
│  └─► Example: Developers, Admins, DBAs          │
│                                                 │
│  IAM ROLES (Temporary permissions)              │
│  └─► For AWS services or temporary access       │
│  └─► No permanent credentials                   │
│                                                 │
│  IAM POLICIES (Permission rules)                │
│  └─► JSON documents                             │
│  └─► Allow or deny specific actions             │
└─────────────────────────────────────────────────┘
```

### IAM Policy Example

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    },
    {
      "Effect": "Deny",
      "Action": "s3:DeleteBucket",
      "Resource": "*"
    }
  ]
}
```

**Explanation**:

- `Effect`: Allow or Deny
- `Action`: What can be done (s3:GetObject = read from S3)
- `Resource`: Which resources (specific bucket or all with *)

### Hands-On: Create an IAM User

```
STEP 1: Navigate to IAM
┌──────────────────────────────────────┐
│ AWS Console → Search "IAM" → IAM    │
└──────────────────────────────────────┘

STEP 2: Create User
┌──────────────────────────────────────┐
│ IAM Dashboard → Users → Add User    │
│                                      │
│ User name: developer-1               │
│ Access type:                         │
│   ☑ Programmatic access (API/CLI)   │
│   ☑ AWS Console access               │
└──────────────────────────────────────┘

STEP 3: Set Permissions
┌──────────────────────────────────────┐
│ Attach existing policies directly:   │
│   ☑ AmazonS3ReadOnlyAccess          │
│   ☑ AmazonEC2ReadOnlyAccess         │
│                                      │
│ OR Add to group:                     │
│   ☑ Developers (group)               │
└──────────────────────────────────────┘

STEP 4: Review and Create
┌──────────────────────────────────────┐
│ Download credentials CSV!            │
│ (Contains access key and secret)    │
└──────────────────────────────────────┘
```

### IAM Best Practices

```
DO:
├─► Enable MFA on root account
├─► Create individual IAM users
├─► Use groups to assign permissions
├─► Apply least privilege principle
├─► Rotate credentials regularly
├─► Use roles for applications
└─► Monitor activity with CloudTrail

DON'T:
├─► Use root account for daily tasks
├─► Share credentials
├─► Hardcode access keys in code
├─► Give overly broad permissions
└─► Leave unused credentials active
```

### Setting Up AWS CLI with IAM

```bash
# Install AWS CLI
# macOS
brew install awscli

# Configure with IAM credentials
aws configure

# Output:
# AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Default region name [None]: us-east-1
# Default output format [None]: json

# Test configuration
aws sts get-caller-identity

# Output:
# {
#     "UserId": "AIDAI...",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/developer-1"
# }
```

---

## 7. AWS EC2

**EC2 (Elastic Compute Cloud)** provides resizable virtual servers in the cloud.

### What is Virtualization?

```
┌────────────────────────────────────────────────┐
│        PHYSICAL SERVER                         │
│  ┌───────────────────────────────────────┐     │
│  │     Hypervisor (Virtualization)       │     │
│  ├───────────┬───────────┬───────────────┤     │
│  │   VM 1    │   VM 2    │    VM 3       │     │
│  │           │           │               │     │
│  │ OS: Linux │ OS: Win   │ OS: Linux     │     │
│  │ App: Web  │ App: DB   │ App: API      │     │
│  │ RAM: 4GB  │ RAM: 8GB  │ RAM: 2GB      │     │
│  │ CPU: 2    │ CPU: 4    │ CPU: 1        │     │
│  └───────────┴───────────┴───────────────┘     │
│                                                │
│  Hardware: CPU, RAM, Storage, Network          │
└────────────────────────────────────────────────┘

Benefits:
- Run multiple OS on one physical machine
- Efficient resource utilization
- Isolation between VMs
- Easy to scale
```

### EC2 Instance Types

```
┌──────────────────────────────────────────────────┐
│  INSTANCE TYPE CATEGORIES                        │
│                                                  │
│  General Purpose (t2, t3, m5)                   │
│  └─► Balanced CPU, memory, network              │
│  └─► Use case: Web servers, small databases     │
│  └─► Example: t2.micro (Free Tier)              │
│                                                  │
│  Compute Optimized (c5, c6)                     │
│  └─► High-performance processors                │
│  └─► Use case: Batch processing, gaming servers │
│                                                  │
│  Memory Optimized (r5, x1)                      │
│  └─► Fast performance for large datasets        │
│  └─► Use case: In-memory databases, big data    │
│                                                  │
│  Storage Optimized (i3, d2)                     │
│  └─► High sequential read/write                 │
│  └─► Use case: Data warehousing, Hadoop         │
│                                                  │
│  Accelerated Computing (p3, g4)                 │
│  └─► Hardware accelerators (GPU)                │
│  └─► Use case: Machine learning, graphics       │
└──────────────────────────────────────────────────┘
```

### Hands-On: Launch Your First EC2 Instance

```
STEP 1: Navigate to EC2
┌──────────────────────────────────────────────┐
│ AWS Console → Search "EC2" → Launch Instance│
└──────────────────────────────────────────────┘

STEP 2: Name and Choose AMI
┌──────────────────────────────────────────────┐
│ Name: my-first-server                        │
│                                              │
│ AMI (Amazon Machine Image):                  │
│   ☑ Amazon Linux 2023 (Free Tier eligible)  │
│   • Ubuntu Server                            │
│   • Windows Server                           │
└──────────────────────────────────────────────┘

STEP 3: Choose Instance Type
┌──────────────────────────────────────────────┐
│   ☑ t2.micro (Free Tier)                    │
│      1 vCPU, 1 GB RAM                        │
└──────────────────────────────────────────────┘

STEP 4: Create Key Pair (for SSH access)
┌──────────────────────────────────────────────┐
│ Key pair name: my-ec2-key                    │
│ Key type: RSA                                │
│ Format: .pem (for Mac/Linux)                 │
│                                              │
│ Download and save securely!                  │
└──────────────────────────────────────────────┘

STEP 5: Network Settings
┌──────────────────────────────────────────────┐
│ Create security group:                       │
│   ☑ Allow SSH (port 22) from My IP          │
│   ☑ Allow HTTP (port 80) from anywhere      │
└──────────────────────────────────────────────┘

STEP 6: Configure Storage
┌──────────────────────────────────────────────┐
│ Size: 8 GB (Free Tier eligible)             │
│ Type: General Purpose SSD (gp3)              │
└──────────────────────────────────────────────┘

STEP 7: Launch!
┌──────────────────────────────────────────────┐
│ Review → Launch Instance                     │
│ Wait ~2 minutes for initialization           │
└──────────────────────────────────────────────┘
```

### Connect to Your EC2 Instance

```bash
# Set permissions on key file (first time only)
chmod 400 my-ec2-key.pem

# Connect via SSH
# Get Public IP from EC2 Console
ssh -i my-ec2-key.pem ec2-user@3.85.123.45

# You're now inside your EC2 instance!
# Try some commands:
whoami          # ec2-user
pwd             # /home/ec2-user
uname -a        # Linux info
```

### Install a Web Server

```bash
# Update system packages
sudo yum update -y

# Install Apache web server
sudo yum install httpd -y

# Start the web server
sudo systemctl start httpd

# Enable auto-start on boot
sudo systemctl enable httpd

# Create a simple web page
echo "<h1>Hello from EC2!</h1>" | sudo tee /var/www/html/index.html

# Now visit http://YOUR_EC2_PUBLIC_IP in browser
```

### EC2 Pricing Models

```
┌─────────────────────────────────────────────────┐
│  ON-DEMAND                                      │
│  └─► Pay per hour/second                       │
│  └─► No commitment                             │
│  └─► Most expensive                            │
│  └─► Use: Short-term, unpredictable workloads  │
│                                                 │
│  RESERVED INSTANCES                            │
│  └─► 1 or 3 year commitment                    │
│  └─► Up to 75% discount                        │
│  └─► Use: Steady-state apps (databases)        │
│                                                 │
│  SPOT INSTANCES                                │
│  └─► Bid on unused capacity                    │
│  └─► Up to 90% discount                        │
│  └─► Can be terminated anytime                 │
│  └─► Use: Batch jobs, fault-tolerant apps      │
│                                                 │
│  SAVINGS PLANS                                 │
│  └─► Commit to usage ($/hour)                  │
│  └─► Up to 72% discount                        │
│  └─► More flexible than Reserved               │
└─────────────────────────────────────────────────┘
```

---

## 8. AWS Storage Solutions

Understanding storage types is crucial for choosing the right solution.

### Storage Type Comparison

```
┌────────────────────────────────────────────────────────┐
│  BLOCK STORAGE                                         │
│  ┌──────────────────────────────────────┐            │
│  │  [Block 1] [Block 2] [Block 3] ...   │            │
│  └──────────────────────────────────────┘            │
│                                                        │
│  • Raw storage blocks                                 │
│  • Attached to ONE instance at a time                 │
│  • Fast, low-latency                                  │
│  • Like a hard drive                                  │
│  • AWS Service: EBS (Elastic Block Store)             │
│  • Use case: Databases, boot volumes                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│  OBJECT STORAGE (BLOB)                                 │
│  ┌──────────────────────────────────────┐            │
│  │  file1.jpg (+ metadata)              │            │
│  │  file2.pdf (+ metadata)              │            │
│  │  file3.mp4 (+ metadata)              │            │
│  └──────────────────────────────────────┘            │
│                                                        │
│  • Store entire files as objects                      │
│  • Accessed via HTTP/API                              │
│  • Massively scalable                                 │
│  • Like a file system accessible from anywhere        │
│  • AWS Service: S3 (Simple Storage Service)           │
│  • Use case: Backups, media files, static websites    │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│  FILE STORAGE                                          │
│  ┌──────────────────────────────────────┐            │
│  │  /shared/                             │            │
│  │    ├── folder1/                       │            │
│  │    │   └── file.txt                   │            │
│  │    └── folder2/                       │            │
│  └──────────────────────────────────────┘            │
│                                                        │
│  • Hierarchical file structure                        │
│  • Shared access from multiple instances              │
│  • Network file system                                │
│  • AWS Service: EFS (Elastic File System)             │
│  • Use case: Shared application files, content mgmt   │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│  DATA LAKE                                             │
│  ┌──────────────────────────────────────┐            │
│  │  Raw Data | Processed | Analytics    │            │
│  │  CSV, JSON, Parquet, Images, Logs... │            │
│  └──────────────────────────────────────┘            │
│                                                        │
│  • Centralized repository                             │
│  • Structured + Unstructured data                     │
│  • For analytics and ML                               │
│  • Built on: S3 + AWS Lake Formation                  │
│  • Use case: Big data analytics, ML training          │
└────────────────────────────────────────────────────────┘
```

### Decision Tree

```
Need storage?
    │
    ├─ For EC2 boot/database? → EBS (Block)
    │
    ├─ For files/backups/media? → S3 (Object)
    │
    ├─ For shared files across EC2? → EFS (File)
    │
    └─ For analytics/big data? → S3 Data Lake
```

---

## 9. AWS S3

**S3 (Simple Storage Service)** is object storage for storing and retrieving any amount of data.

### S3 Key Concepts

```
┌─────────────────────────────────────────────────┐
│  S3 HIERARCHY                                   │
│                                                 │
│  BUCKET                                         │
│  └─► Unique name globally                      │
│  └─► Created in a region                       │
│  └─► Example: my-company-data-2024             │
│      │                                          │
│      ├─► folder1/                              │
│      │   ├─► file1.jpg (Object)                │
│      │   └─► file2.pdf                         │
│      │                                          │
│      └─► folder2/                              │
│          └─► data.csv                          │
│                                                 │
│  Each Object has:                               │
│  • Key (path/filename)                          │
│  • Value (file content)                         │
│  • Metadata (content-type, custom tags)         │
│  • Version ID (if versioning enabled)           │
└─────────────────────────────────────────────────┘
```

### S3 Storage Classes

```
┌──────────────────────────────────────────────────┐
│  Storage Class       Cost    Retrieval  Use Case │
├──────────────────────────────────────────────────┤
│  S3 Standard         $$$     Instant   Frequent  │
│  (Default)                            access     │
│                                                  │
│  S3 Intelligent-     $$      Instant   Unknown   │
│  Tiering                              patterns   │
│  (Auto-moves data)                               │
│                                                  │
│  S3 Standard-IA      $$      Instant   Monthly   │
│  (Infrequent Access)                  access     │
│                                                  │
│  S3 Glacier          $       Minutes-  Archival  │
│  Instant Retrieval            Hours    (long-term)│
│                                                  │
│  S3 Glacier Deep     ¢       12 hours  Rarely    │
│  Archive                              accessed   │
└──────────────────────────────────────────────────┘
```

### Hands-On: Create an S3 Bucket

```
STEP 1: Navigate to S3
┌──────────────────────────────────────────────┐
│ AWS Console → Search "S3" → Create bucket   │
└──────────────────────────────────────────────┘

STEP 2: Bucket Configuration
┌──────────────────────────────────────────────┐
│ Bucket name: my-learning-bucket-2024-unique  │
│ (Must be globally unique, lowercase, no _)   │
│                                              │
│ Region: us-east-1                            │
│                                              │
│ Object Ownership: ACLs disabled (default)    │
└──────────────────────────────────────────────┘

STEP 3: Block Public Access
┌──────────────────────────────────────────────┐
│ ☑ Block all public access (RECOMMENDED)     │
│   (Keep data private by default)             │
└──────────────────────────────────────────────┘

STEP 4: Versioning (Optional)
┌──────────────────────────────────────────────┐
│ ☐ Enable versioning                         │
│   (Keep multiple versions of objects)        │
└──────────────────────────────────────────────┘

STEP 5: Encryption
┌──────────────────────────────────────────────┐
│ ☑ Enable Server-Side Encryption (SSE-S3)    │
│   (Automatic encryption at rest)             │
└──────────────────────────────────────────────┘

STEP 6: Create!
┌──────────────────────────────────────────────┐
│ Create bucket                                │
└──────────────────────────────────────────────┘
```

### Upload Files to S3

```
METHOD 1: Console (UI)
┌──────────────────────────────────────────────┐
│ Open your bucket → Upload                    │
│ Drag & drop files or click "Add files"       │
│ Upload                                       │
└──────────────────────────────────────────────┘

METHOD 2: AWS CLI
```

```bash
# Upload a single file
aws s3 cp myfile.txt s3://my-learning-bucket-2024-unique/

# Upload entire folder
aws s3 cp ./my-folder s3://my-learning-bucket-2024-unique/my-folder/ --recursive

# List bucket contents
aws s3 ls s3://my-learning-bucket-2024-unique/

# Download a file
aws s3 cp s3://my-learning-bucket-2024-unique/myfile.txt ./downloaded.txt

# Sync local folder with S3 (like rsync)
aws s3 sync ./local-folder s3://my-learning-bucket-2024-unique/backup/
```

### S3 Use Cases

```
1. Static Website Hosting
   └─► Host HTML/CSS/JS files
   └─► Enable: Bucket → Properties → Static Website Hosting

2. Backup and Archive
   └─► Backup databases, logs, files
   └─► Use Glacier for long-term storage

3. Data Lake
   └─► Store raw data for analytics
   └─► Query with Athena, process with Glue

4. Media Storage
   └─► Store videos, images, audio
   └─► Serve via CloudFront CDN

5. Software Distribution
   └─► Host software packages, updates
```

### S3 Security

```json
// Bucket Policy Example (Allow public read for website)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

---

## 10. Working with S3 SDK

Access S3 programmatically using AWS SDKs (Python, JavaScript, Java, etc.)

### Python boto3 Setup

```bash
# Install boto3 (AWS SDK for Python)
pip install boto3

# Or using uv (if in your project)
uv add boto3
```

### Basic S3 Operations in Python

```python
import boto3
from botocore.exceptions import ClientError

# Initialize S3 client
s3_client = boto3.client('s3')

# Or use resource (higher-level interface)
s3_resource = boto3.resource('s3')

# ========================================
# 1. LIST ALL BUCKETS
# ========================================
def list_buckets():
    """List all S3 buckets in your account"""
    response = s3_client.list_buckets()
    
    print("Available buckets:")
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']} (Created: {bucket['CreationDate']})")

# ========================================
# 2. CREATE A BUCKET
# ========================================
def create_bucket(bucket_name, region='us-east-1'):
    """Create an S3 bucket"""
    try:
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' created successfully!")
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 3. UPLOAD A FILE
# ========================================
def upload_file(file_path, bucket_name, object_name=None):
    """
    Upload a file to S3
    
    Args:
        file_path: Path to local file
        bucket_name: S3 bucket name
        object_name: S3 object name (if None, uses file_path)
    """
    if object_name is None:
        object_name = file_path
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}'")
    except ClientError as e:
        print(f"Error: {e}")

# Upload with metadata and content type
def upload_file_with_metadata(file_path, bucket_name, object_name):
    """Upload with additional configuration"""
    s3_client.upload_file(
        file_path,
        bucket_name,
        object_name,
        ExtraArgs={
            'ContentType': 'image/jpeg',
            'Metadata': {
                'uploaded_by': 'my-app',
                'category': 'profile-images'
            },
            'StorageClass': 'STANDARD_IA'  # Use Infrequent Access
        }
    )

# ========================================
# 4. DOWNLOAD A FILE
# ========================================
def download_file(bucket_name, object_name, file_path):
    """Download a file from S3"""
    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"File downloaded to '{file_path}'")
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 5. LIST OBJECTS IN BUCKET
# ========================================
def list_objects(bucket_name, prefix=''):
    """List all objects in a bucket (with optional prefix filter)"""
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix
        )
        
        if 'Contents' in response:
            print(f"Objects in '{bucket_name}':")
            for obj in response['Contents']:
                print(f"  - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("No objects found")
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 6. DELETE AN OBJECT
# ========================================
def delete_object(bucket_name, object_name):
    """Delete an object from S3"""
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"Object '{object_name}' deleted")
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 7. GENERATE PRESIGNED URL
# ========================================
def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generate a presigned URL for temporary access
    
    Args:
        expiration: URL valid for (seconds), default 1 hour
    """
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        print(f"Presigned URL (valid for {expiration}s):")
        print(url)
        return url
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 8. READ FILE CONTENT DIRECTLY
# ========================================
def read_file_content(bucket_name, object_name):
    """Read file content without downloading"""
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
        content = response['Body'].read().decode('utf-8')
        print(f"Content of '{object_name}':")
        print(content)
        return content
    except ClientError as e:
        print(f"Error: {e}")

# ========================================
# 9. UPLOAD STRING AS FILE
# ========================================
def upload_string(bucket_name, object_name, content):
    """Upload string content as a file"""
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=content.encode('utf-8'),
        ContentType='text/plain'
    )
    print(f"String uploaded as '{object_name}'")

# ========================================
# EXAMPLE USAGE
# ========================================
if __name__ == "__main__":
    BUCKET_NAME = "my-learning-bucket-2024-unique"
    
    # List buckets
    list_buckets()
    
    # Upload a file
    upload_file("data.csv", BUCKET_NAME, "uploads/data.csv")
    
    # List objects
    list_objects(BUCKET_NAME, prefix="uploads/")
    
    # Generate presigned URL
    generate_presigned_url(BUCKET_NAME, "uploads/data.csv", expiration=300)
    
    # Upload text content
    upload_string(BUCKET_NAME, "notes.txt", "Hello from S3 SDK!")
    
    # Read content
    read_file_content(BUCKET_NAME, "notes.txt")
    
    # Download file
    download_file(BUCKET_NAME, "uploads/data.csv", "downloaded_data.csv")
```

### Advanced: Upload Large Files with Progress

```python
import os
import sys
import threading

class ProgressPercentage:
    """Display upload progress"""
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                f"\r{self._filename}  {self._seen_so_far / (1024**2):.2f}MB / "
                f"{self._size / (1024**2):.2f}MB  ({percentage:.2f}%)"
            )
            sys.stdout.flush()

# Use with upload
s3_client.upload_file(
    'large_file.zip',
    'my-bucket',
    'uploads/large_file.zip',
    Callback=ProgressPercentage('large_file.zip')
)
```

### Error Handling Best Practices

```python
import boto3
from botocore.exceptions import (
    ClientError,
    NoCredentialsError,
    PartialCredentialsError
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_s3_operation(bucket_name, key):
    """Example with proper error handling"""
    try:
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        return response['Body'].read()
        
    except NoCredentialsError:
        logger.error("AWS credentials not found. Run 'aws configure'")
        
    except PartialCredentialsError:
        logger.error("Incomplete AWS credentials")
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        
        if error_code == 'NoSuchBucket':
            logger.error(f"Bucket '{bucket_name}' does not exist")
        elif error_code == 'NoSuchKey':
            logger.error(f"Object '{key}' not found in bucket")
        elif error_code == 'AccessDenied':
            logger.error("Access denied. Check IAM permissions")
        else:
            logger.error(f"Unexpected error: {e}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    
    return None
```

---

*This is Part 1 of your AWS learning guide. The next sections will cover Lambda, Glue, and Athena with similar depth and hands-on examples.*

**Next Steps:**

1. Practice creating S3 buckets and uploading files
2. Try the Python SDK examples
3. Experiment with different storage classes
4. Set up IAM users with limited S3 permissions

**Coming Next:**

- AWS Lambda (Serverless Functions)
- AWS Glue (ETL Service)
- AWS Athena (Query S3 data with SQL)

---

## 11. AWS Lambda

**AWS Lambda** is a serverless compute service that runs your code without provisioning servers.

### What is Serverless?

Serverless doesn't mean "no servers" - it means you don't manage servers.

```
┌─────────────────────────────────────────────────┐
│  TRADITIONAL vs SERVERLESS                      │
├─────────────────────────────────────────────────┤
│                                                 │
│  TRADITIONAL (EC2):                             │
│  ┌──────────────────────────────┐              │
│  │  YOU manage:                 │              │
│  │  • Provision servers         │              │
│  │  • Install OS & runtime      │              │
│  │  • Patch & update            │              │
│  │  • Scale manually            │              │
│  │  • Pay 24/7 (even if idle)   │              │
│  └──────────────────────────────┘              │
│                                                 │
│  SERVERLESS (Lambda):                           │
│  ┌──────────────────────────────┐              │
│  │  YOU provide:                │              │
│  │  • Just your code            │              │
│  │                              │              │
│  │  AWS handles:                │              │
│  │  • Infrastructure            │              │
│  │  • Scaling (automatic)       │              │
│  │  • High availability         │              │
│  │  • Pay per execution only    │              │
│  └──────────────────────────────┘              │
└─────────────────────────────────────────────────┘
```

### Lambda Key Concepts

```
┌─────────────────────────────────────────────────┐
│  LAMBDA FUNCTION                                │
│                                                 │
│  ┌──────────────────────────────┐              │
│  │  TRIGGER (Event Source)      │              │
│  │  • API Gateway               │              │
│  │  • S3 Event                  │              │
│  │  • CloudWatch Event          │              │
│  │  • Manual Invoke             │              │
│  └─────────┬────────────────────┘              │
│            │                                    │
│            ▼                                    │
│  ┌──────────────────────────────┐              │
│  │  LAMBDA FUNCTION             │              │
│  │  • Your code (handler)       │              │
│  │  • Runtime (Python, Node.js) │              │
│  │  • Memory: 128MB - 10GB      │              │
│  │  • Timeout: max 15 minutes   │              │
│  └─────────┬────────────────────┘              │
│            │                                    │
│            ▼                                    │
│  ┌──────────────────────────────┐              │
│  │  OUTPUT                       │              │
│  │  • Return value              │              │
│  │  • Write to S3/DB            │              │
│  │  • Call another service      │              │
│  └──────────────────────────────┘              │
└─────────────────────────────────────────────────┘
```

### Lambda Pricing

```
PAY FOR:
  1. Number of requests
     • First 1 million requests/month: FREE
     • $0.20 per 1 million requests after

  2. Compute time (GB-seconds)
     • Memory allocated × execution time
     • First 400,000 GB-seconds/month: FREE
     • $0.00001667 per GB-second after

EXAMPLE:
  Function: 512 MB, runs 100ms, invoked 1M times/month
  Cost: ~$0.60/month (most likely FREE tier)
```

### Hands-On: Create Your First Lambda Function

#### Step 1: Create Function via Console

```
STEP 1: Navigate to Lambda
┌──────────────────────────────────────────────┐
│ AWS Console → Search "Lambda" → Create      │
└──────────────────────────────────────────────┘

STEP 2: Function Configuration
┌──────────────────────────────────────────────┐
│ • Author from scratch                        │
│ Function name: my-first-lambda               │
│ Runtime: Python 3.12                         │
│ Architecture: x86_64                         │
└──────────────────────────────────────────────┘

STEP 3: Permissions
┌──────────────────────────────────────────────┐
│ Execution role:                              │
│ • Create a new role with basic permissions   │
│   (Allows Lambda to write logs to CloudWatch)│
└──────────────────────────────────────────────┘

STEP 4: Create Function
┌──────────────────────────────────────────────┐
│ Click "Create function"                      │
└──────────────────────────────────────────────┘
```

#### Step 2: Write Lambda Code

```python
import json

def lambda_handler(event, context):
    """
    Lambda function entry point
    
    Args:
        event: Input data (dict)
        context: Runtime information
    
    Returns:
        dict: Response with statusCode and body
    """
    
    # Get name from event (with default)
    name = event.get('name', 'World')
    
    # Your logic here
    message = f"Hello, {name}! This is your Lambda function."
    
    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message,
            'timestamp': context.request_id
        })
    }
```

#### Step 3: Test Your Function

```
IN CONSOLE:
┌──────────────────────────────────────────────┐
│ 1. Click "Test" button                       │
│ 2. Create new test event                     │
│    Event name: test1                         │
│    Event JSON:                               │
│    {                                         │
│      "name": "Student"                       │
│    }                                         │
│ 3. Click "Save"                              │
│ 4. Click "Test" to invoke                    │
└──────────────────────────────────────────────┘

OUTPUT:
{
  "statusCode": 200,
  "body": "{\"message\": \"Hello, Student! This is your Lambda function.\", \"timestamp\": \"abc-123\"}"
}
```

### Lambda with S3 Trigger

```python
import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Triggered when file is uploaded to S3
    Processes the file and logs information
    """
    
    # Get bucket and file info from event
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_size = record['s3']['object']['size']
        
        print(f"New file uploaded:")
        print(f"  Bucket: {bucket_name}")
        print(f"  File: {object_key}")
        print(f"  Size: {file_size} bytes")
        
        # Read file content (if text file)
        if object_key.endswith('.txt'):
            response = s3_client.get_object(
                Bucket=bucket_name, 
                Key=object_key
            )
            content = response['Body'].read().decode('utf-8')
            print(f"  Content preview: {content[:100]}...")
            
            # Process content (example: count words)
            word_count = len(content.split())
            
            # Write result to another S3 location
            result_key = f"processed/{object_key}.json"
            s3_client.put_object(
                Bucket=bucket_name,
                Key=result_key,
                Body=json.dumps({
                    'original_file': object_key,
                    'word_count': word_count,
                    'file_size': file_size
                })
            )
            
            print(f"  Result saved to: {result_key}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
```

#### Configure S3 Trigger

```
IN LAMBDA CONSOLE:
┌──────────────────────────────────────────────┐
│ 1. Click "Add trigger"                       │
│ 2. Select: S3                                │
│ 3. Bucket: my-learning-bucket-2024-unique    │
│ 4. Event type: All object create events      │
│ 5. Prefix (optional): uploads/               │
│ 6. Suffix (optional): .txt                   │
│ 7. Click "Add"                               │
└──────────────────────────────────────────────┘

Now when you upload a .txt file to uploads/ folder,
Lambda automatically processes it!
```

### Lambda with API Gateway (REST API)

Create a simple REST API backed by Lambda:

```python
import json

def lambda_handler(event, context):
    """
    Handle HTTP requests via API Gateway
    """
    
    # Get HTTP method and path
    http_method = event.get('httpMethod')
    path = event.get('path')
    
    # Parse query parameters
    query_params = event.get('queryStringParameters') or {}
    
    # Parse body (for POST/PUT)
    body = {}
    if event.get('body'):
        body = json.loads(event['body'])
    
    # Route based on method and path
    if http_method == 'GET' and path == '/users':
        # Return list of users
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'users': [
                    {'id': 1, 'name': 'Alice'},
                    {'id': 2, 'name': 'Bob'}
                ]
            })
        }
    
    elif http_method == 'POST' and path == '/users':
        # Create new user
        new_user = {
            'id': 3,
            'name': body.get('name', 'Unknown')
        }
        return {
            'statusCode': 201,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(new_user)
        }
    
    else:
        # Not found
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Not found'})
        }
```

### Deploying Lambda with AWS CLI

```bash
# Create deployment package
cd my-lambda-function/
zip function.zip lambda_function.py

# Create Lambda function
aws lambda create-function \
  --function-name my-cli-lambda \
  --runtime python3.12 \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip

# Invoke function
aws lambda invoke \
  --function-name my-cli-lambda \
  --payload '{"name": "CLI User"}' \
  response.json

# View response
cat response.json

# Update function code
zip function.zip lambda_function.py
aws lambda update-function-code \
  --function-name my-cli-lambda \
  --zip-file fileb://function.zip
```

### Lambda with Python Dependencies

```bash
# Create project structure
mkdir my-lambda-with-dependencies
cd my-lambda-with-dependencies

# Install dependencies to a folder
pip install requests -t ./package

# Add your code
cp lambda_function.py ./package/

# Create deployment package
cd package
zip -r ../deployment-package.zip .
cd ..

# Upload to Lambda
aws lambda update-function-code \
  --function-name my-lambda \
  --zip-file fileb://deployment-package.zip
```

### Lambda Layers (Reusable Dependencies)

```
┌─────────────────────────────────────────────────┐
│  LAMBDA LAYERS                                  │
│                                                 │
│  ┌──────────────────┐  ┌──────────────────┐   │
│  │  Function 1      │  │  Function 2      │   │
│  │  (Your code)     │  │  (Your code)     │   │
│  └────────┬─────────┘  └────────┬─────────┘   │
│           │                     │              │
│           └──────────┬──────────┘              │
│                      │                         │
│                      ▼                         │
│           ┌──────────────────┐                │
│           │  Lambda Layer    │                │
│           │  (Shared libs)   │                │
│           │  • requests      │                │
│           │  • pandas        │                │
│           │  • numpy         │                │
│           └──────────────────┘                │
│                                                 │
│  Benefits:                                      │
│  • Reduce deployment package size              │
│  • Share dependencies across functions         │
│  • Faster deployments                          │
└─────────────────────────────────────────────────┘
```

### Lambda Best Practices

```
PERFORMANCE:
  ✓ Minimize cold starts
    - Keep functions warm with scheduled invokes
    - Use provisioned concurrency for critical apps
  
  ✓ Optimize memory allocation
    - More memory = more CPU power
    - Test different memory settings
  
  ✓ Reuse connections
    - Initialize clients outside handler
    - Reuse across invocations

SECURITY:
  ✓ Use IAM roles (not hardcoded credentials)
  ✓ Apply least privilege permissions
  ✓ Encrypt environment variables
  ✓ Use VPC for private resource access

COST OPTIMIZATION:
  ✓ Set appropriate timeout (don't use max)
  ✓ Use correct memory allocation
  ✓ Clean up unused functions
  ✓ Monitor with CloudWatch

ERROR HANDLING:
  ✓ Implement retry logic
  ✓ Use dead letter queues (DLQ)
  ✓ Log errors comprehensively
  ✓ Set up CloudWatch alarms
```

### Lambda Use Cases

```
1. Real-time File Processing
   └─► S3 upload triggers Lambda to process images,
       videos, or documents

2. API Backend
   └─► API Gateway + Lambda for serverless REST APIs

3. Scheduled Tasks (Cron Jobs)
   └─► CloudWatch Events trigger Lambda on schedule
       (e.g., daily reports, cleanup tasks)

4. Stream Processing
   └─► Process DynamoDB Streams, Kinesis data in real-time

5. ETL Jobs
   └─► Extract data, transform, load to data warehouse

6. Webhooks
   └─► Respond to external events (GitHub, Slack, etc.)

7. IoT Backend
   └─► Process data from IoT devices

8. Chatbots
   └─► Lambda processes messages and responds
```

---

## 12. AWS Glue & Data Cataloging

**AWS Glue** is a fully managed ETL (Extract, Transform, Load) service for data preparation and integration.

### What is ETL?

```
┌─────────────────────────────────────────────────┐
│  ETL PROCESS                                    │
│                                                 │
│  EXTRACT                                        │
│  ┌────────────────────────────────┐            │
│  │ Pull data from sources:        │            │
│  │ • Databases                    │            │
│  │ • S3 files (CSV, JSON, etc.)   │            │
│  │ • APIs                         │            │
│  │ • Streaming data               │            │
│  └─────────┬──────────────────────┘            │
│            │                                    │
│            ▼                                    │
│  TRANSFORM                                      │
│  ┌────────────────────────────────┐            │
│  │ Clean and modify data:         │            │
│  │ • Remove duplicates            │            │
│  │ • Change formats               │            │
│  │ • Filter rows                  │            │
│  │ • Join datasets                │            │
│  │ • Aggregate                    │            │
│  └─────────┬──────────────────────┘            │
│            │                                    │
│            ▼                                    │
│  LOAD                                           │
│  ┌────────────────────────────────┐            │
│  │ Write to destinations:         │            │
│  │ • Data warehouse (Redshift)    │            │
│  │ • Data lake (S3)               │            │
│  │ • Database                     │            │
│  └────────────────────────────────┘            │
└─────────────────────────────────────────────────┘
```

### Glue Components

```
┌─────────────────────────────────────────────────┐
│  AWS GLUE ARCHITECTURE                          │
│                                                 │
│  1. GLUE DATA CATALOG                           │
│     ┌──────────────────────────────┐           │
│     │ Metadata repository          │           │
│     │ • Databases                  │           │
│     │ • Tables (schema info)       │           │
│     │ • Partitions                 │           │
│     └──────────────────────────────┘           │
│                                                 │
│  2. GLUE CRAWLERS                               │
│     ┌──────────────────────────────┐           │
│     │ Automatically discover data  │           │
│     │ • Scan S3/databases          │           │
│     │ • Infer schema               │           │
│     │ • Update catalog             │           │
│     └──────────────────────────────┘           │
│                                                 │
│  3. GLUE ETL JOBS                               │
│     ┌──────────────────────────────┐           │
│     │ Transform data               │           │
│     │ • Python/Spark code          │           │
│     │ • Visual editor              │           │
│     │ • Schedule or trigger        │           │
│     └──────────────────────────────┘           │
│                                                 │
│  4. GLUE DATA QUALITY                           │
│     ┌──────────────────────────────┐           │
│     │ Validate data                │           │
│     │ • Define rules               │           │
│     │ • Monitor quality            │           │
│     └──────────────────────────────┘           │
└─────────────────────────────────────────────────┘
```

### Hands-On: Create a Glue Crawler

#### Step 1: Prepare Sample Data

```python
# Create sample CSV data for S3
import boto3
import csv
from io import StringIO

# Sample customer data
customers = [
    ['customer_id', 'name', 'email', 'signup_date', 'country'],
    [1, 'Alice Johnson', 'alice@example.com', '2024-01-15', 'USA'],
    [2, 'Bob Smith', 'bob@example.com', '2024-01-16', 'UK'],
    [3, 'Charlie Brown', 'charlie@example.com', '2024-01-17', 'Canada'],
    [4, 'Diana Prince', 'diana@example.com', '2024-01-18', 'USA'],
    [5, 'Ethan Hunt', 'ethan@example.com', '2024-01-19', 'Australia']
]

# Write to CSV
csv_buffer = StringIO()
writer = csv.writer(csv_buffer)
writer.writerows(customers)

# Upload to S3
s3 = boto3.client('s3')
s3.put_object(
    Bucket='my-learning-bucket-2024-unique',
    Key='data-lake/customers/customers.csv',
    Body=csv_buffer.getvalue()
)

print("Sample data uploaded to S3!")
```

#### Step 2: Create Glue Database

```
IN GLUE CONSOLE:
┌──────────────────────────────────────────────┐
│ AWS Console → Glue → Databases               │
│ 1. Click "Add database"                      │
│ 2. Name: my_data_lake                        │
│ 3. Description: Learning data lake           │
│ 4. Click "Create"                            │
└──────────────────────────────────────────────┘
```

#### Step 3: Create and Run Crawler

```
IN GLUE CONSOLE:
┌──────────────────────────────────────────────┐
│ Glue → Crawlers → Create crawler             │
│                                              │
│ STEP 1: Name                                 │
│   Name: customers-crawler                    │
│                                              │
│ STEP 2: Data source                          │
│   Source type: S3                            │
│   S3 path: s3://my-learning-bucket-.../      │
│            data-lake/customers/              │
│                                              │
│ STEP 3: IAM role                             │
│   Create new role: AWSGlueServiceRole-Demo   │
│   (Glue needs permission to read S3)         │
│                                              │
│ STEP 4: Target database                      │
│   Database: my_data_lake                     │
│   Table prefix: raw_                         │
│                                              │
│ STEP 5: Schedule                             │
│   Frequency: On demand (or schedule)         │
│                                              │
│ STEP 6: Review and create                    │
│   Click "Create crawler"                     │
│                                              │
│ STEP 7: Run crawler                          │
│   Select crawler → Click "Run"               │
│   Wait ~1-2 minutes                          │
└──────────────────────────────────────────────┘

RESULT:
  Crawler discovers schema and creates table:
  Database: my_data_lake
  Table: raw_customers
  Columns: customer_id, name, email, signup_date, country
```

### View Discovered Data

```
IN GLUE CONSOLE:
┌──────────────────────────────────────────────┐
│ Glue → Tables → raw_customers                │
│                                              │
│ Schema:                                      │
│   customer_id (bigint)                       │
│   name (string)                              │
│   email (string)                             │
│   signup_date (string)                       │
│   country (string)                           │
│                                              │
│ Location: s3://bucket/data-lake/customers/   │
│ Input format: TextInputFormat                │
│ Output format: HiveIgnoreKeyTextOutputFormat │
└──────────────────────────────────────────────┘
```

### Create a Glue ETL Job (Visual Editor)

```
IN GLUE CONSOLE:
┌──────────────────────────────────────────────┐
│ Glue → ETL Jobs → Visual ETL                 │
│                                              │
│ STEP 1: Source                               │
│   Add source → Data Catalog table            │
│   Database: my_data_lake                     │
│   Table: raw_customers                       │
│                                              │
│ STEP 2: Transform                            │
│   Add transform → Filter                     │
│   Condition: country == "USA"                │
│                                              │
│   Add transform → Select Fields              │
│   Keep: customer_id, name, email             │
│                                              │
│ STEP 3: Target                               │
│   Add target → S3                            │
│   Format: Parquet                            │
│   S3 path: s3://bucket/processed/usa-customers/ │
│                                              │
│ STEP 4: Job details                          │
│   Name: filter-usa-customers                 │
│   IAM role: AWSGlueServiceRole-Demo          │
│   Type: Spark                                │
│                                              │
│ STEP 5: Save and run                         │
└──────────────────────────────────────────────┘
```

### Glue ETL Job (Python Script)

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# READ: Load data from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_data_lake",
    table_name="raw_customers"
)

# TRANSFORM: Filter USA customers only
filtered = Filter.apply(
    frame=datasource,
    f=lambda row: row["country"] == "USA"
)

# TRANSFORM: Select specific columns
selected = SelectFields.apply(
    frame=filtered,
    paths=["customer_id", "name", "email", "signup_date"]
)

# TRANSFORM: Rename column
renamed = RenameField.apply(
    frame=selected,
    old_name="customer_id",
    new_name="id"
)

# WRITE: Save to S3 as Parquet
glueContext.write_dynamic_frame.from_options(
    frame=renamed,
    connection_type="s3",
    connection_options={
        "path": "s3://my-learning-bucket-2024-unique/processed/usa-customers/"
    },
    format="parquet"
)

job.commit()
```

### Advanced: Glue with PySpark

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, count, avg

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from catalog
customers_df = glueContext.create_dynamic_frame.from_catalog(
    database="my_data_lake",
    table_name="raw_customers"
).toDF()

# Convert to Spark DataFrame for advanced operations
# Add new column
customers_df = customers_df.withColumn(
    "region",
    when(col("country").isin(["USA", "Canada"]), "North America")
    .when(col("country") == "UK", "Europe")
    .otherwise("Other")
)

# Aggregate data
region_stats = customers_df.groupBy("region").agg(
    count("*").alias("customer_count")
)

# Show results (for debugging)
region_stats.show()

# Write results
region_stats.write.mode("overwrite").parquet(
    "s3://my-learning-bucket-2024-unique/analytics/region-stats/"
)

job.commit()
```

### Schedule Glue Job

```
IN GLUE CONSOLE:
┌──────────────────────────────────────────────┐
│ Job details → Triggers → Add trigger          │
│                                              │
│ Trigger type: Schedule                       │
│ Name: daily-etl-trigger                      │
│ Frequency: Daily at 2:00 AM                  │
│                                              │
│ OR                                           │
│                                              │
│ Trigger type: Event-based                    │
│ Trigger on: Crawler completion               │
│ Crawler name: customers-crawler              │
└──────────────────────────────────────────────┘
```

### Glue Data Catalog with boto3

```python
import boto3

glue = boto3.client('glue')

# List databases
response = glue.get_databases()
for db in response['DatabaseList']:
    print(f"Database: {db['Name']}")

# List tables in a database
response = glue.get_tables(DatabaseName='my_data_lake')
for table in response['TableList']:
    print(f"Table: {table['Name']}")
    print(f"  Location: {table['StorageDescriptor']['Location']}")
    print(f"  Columns:")
    for col in table['StorageDescriptor']['Columns']:
        print(f"    - {col['Name']} ({col['Type']})")

# Start crawler
glue.start_crawler(Name='customers-crawler')

# Start job
glue.start_job_run(JobName='filter-usa-customers')
```

---

## 13. Building ETL Pipelines

Complete end-to-end ETL pipeline example.

### Pipeline Architecture

```
┌──────────────────────────────────────────────────┐
│  ETL PIPELINE FLOW                               │
│                                                  │
│  1. DATA INGESTION                               │
│     ┌────────────┐                               │
│     │ Raw Data   │ → Upload to S3                │
│     │ (CSV/JSON) │    s3://bucket/raw/           │
│     └────────────┘                               │
│                                                  │
│  2. CATALOG                                      │
│     ┌────────────┐                               │
│     │ Glue       │ → Scan and discover schema    │
│     │ Crawler    │    Create table in catalog    │
│     └────────────┘                               │
│                                                  │
│  3. TRANSFORM                                    │
│     ┌────────────┐                               │
│     │ Glue ETL   │ → Clean, filter, aggregate    │
│     │ Job        │    Write to s3://bucket/      │
│     └────────────┘    processed/                 │
│                                                  │
│  4. QUERY                                        │
│     ┌────────────┐                               │
│     │ Athena     │ → SQL queries on processed    │
│     │            │    data without loading        │
│     └────────────┘                               │
│                                                  │
│  5. VISUALIZE (Optional)                         │
│     ┌────────────┐                               │
│     │ QuickSight │ → Dashboards and reports      │
│     └────────────┘                               │
└──────────────────────────────────────────────────┘
```

### Example: Sales Data Pipeline

#### Step 1: Generate Sample Sales Data

```python
import boto3
import json
import random
from datetime import datetime, timedelta

s3 = boto3.client('s3')

# Generate sample sales data
def generate_sales_data(num_records=100):
    products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Monitor']
    regions = ['North', 'South', 'East', 'West']
    
    sales = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(num_records):
        sale = {
            'sale_id': i + 1,
            'product': random.choice(products),
            'quantity': random.randint(1, 10),
            'price': round(random.uniform(100, 2000), 2),
            'region': random.choice(regions),
            'sale_date': (start_date + timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d'),
            'customer_id': random.randint(1000, 9999)
        }
        sale['total'] = round(sale['quantity'] * sale['price'], 2)
        sales.append(sale)
    
    return sales

# Upload to S3
sales_data = generate_sales_data(1000)

# Write as JSON lines (one JSON per line)
json_lines = '\n'.join([json.dumps(sale) for sale in sales_data])

s3.put_object(
    Bucket='my-learning-bucket-2024-unique',
    Key='data-lake/raw/sales/sales_2024.json',
    Body=json_lines
)

print("Sales data uploaded!")
print(f"Total records: {len(sales_data)}")
print(f"Sample record: {sales_data[0]}")
```

#### Step 2: Create Crawler for Sales Data

```
Follow same process as before:
1. Create crawler: sales-crawler
2. S3 path: s3://bucket/data-lake/raw/sales/
3. Database: my_data_lake
4. Table prefix: raw_
5. Run crawler
6. Result: Table "raw_sales" created
```

#### Step 3: ETL Job - Sales Analytics

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw sales data
sales_df = glueContext.create_dynamic_frame.from_catalog(
    database="my_data_lake",
    table_name="raw_sales"
).toDF()

# =============================================
# TRANSFORM 1: Clean Data
# =============================================
# Remove records with null values
clean_sales = sales_df.dropna()

# Filter out invalid prices
clean_sales = clean_sales.filter(col("price") > 0)

# =============================================
# TRANSFORM 2: Aggregate by Region
# =============================================
regional_sales = clean_sales.groupBy("region").agg(
    sum("total").alias("total_revenue"),
    count("sale_id").alias("num_sales"),
    avg("total").alias("avg_sale_value"),
    countDistinct("customer_id").alias("unique_customers")
)

# =============================================
# TRANSFORM 3: Aggregate by Product
# =============================================
product_sales = clean_sales.groupBy("product").agg(
    sum("quantity").alias("total_units_sold"),
    sum("total").alias("total_revenue"),
    avg("price").alias("avg_price")
).orderBy(desc("total_revenue"))

# =============================================
# TRANSFORM 4: Monthly Trends
# =============================================
monthly_sales = clean_sales.withColumn(
    "month", 
    date_format(col("sale_date"), "yyyy-MM")
).groupBy("month").agg(
    sum("total").alias("monthly_revenue"),
    count("sale_id").alias("monthly_sales")
).orderBy("month")

# =============================================
# SAVE: Write transformed data to S3
# =============================================
# Regional analysis
regional_sales.write.mode("overwrite").parquet(
    "s3://my-learning-bucket-2024-unique/processed/sales/by-region/"
)

# Product analysis
product_sales.write.mode("overwrite").parquet(
    "s3://my-learning-bucket-2024-unique/processed/sales/by-product/"
)

# Monthly trends
monthly_sales.write.mode("overwrite").parquet(
    "s3://my-learning-bucket-2024-unique/processed/sales/monthly-trends/"
)

# Clean sales data (for querying)
clean_sales.write.mode("overwrite") \
    .partitionBy("region") \
    .parquet("s3://my-learning-bucket-2024-unique/processed/sales/clean-data/")

job.commit()
```

#### Step 4: Create Crawlers for Processed Data

```
Create separate crawlers for:
1. by-region data
2. by-product data  
3. monthly-trends data
4. clean-data

This makes processed data queryable via Athena
```

---

## 14. AWS Athena

**Amazon Athena** is an interactive query service that analyzes data directly in S3 using standard SQL.

### Athena Overview

```
┌─────────────────────────────────────────────────┐
│  ATHENA WORKFLOW                                │
│                                                 │
│  1. Data in S3                                  │
│     └─► CSV, JSON, Parquet, ORC, etc.          │
│                                                 │
│  2. Schema in Glue Data Catalog                 │
│     └─► Table definitions                       │
│                                                 │
│  3. Query with SQL                              │
│     └─► SELECT * FROM table WHERE ...          │
│                                                 │
│  4. Results                                     │
│     └─► View in console or save to S3          │
│                                                 │
│  KEY FEATURES:                                  │
│  • No servers to manage                         │
│  • Pay per query ($5 per TB scanned)            │
│  • Standard SQL (ANSI SQL)                      │
│  • Integrates with Glue Catalog                 │
│  • Fast (parallel execution)                    │
└─────────────────────────────────────────────────┘
```

### Hands-On: Query with Athena

#### Step 1: Setup Athena

```
IN ATHENA CONSOLE:
┌──────────────────────────────────────────────┐
│ AWS Console → Athena                         │
│                                              │
│ First time setup:                            │
│ 1. Settings → Manage                         │
│ 2. Query result location:                    │
│    s3://my-learning-bucket-.../athena-results/│
│ 3. Save                                      │
└──────────────────────────────────────────────┘
```

#### Step 2: Basic Queries

```sql
-- Select database
USE my_data_lake;

-- View all tables
SHOW TABLES;

-- Query raw customers
SELECT * 
FROM raw_customers 
LIMIT 10;

-- Count customers by country
SELECT country, COUNT(*) as customer_count
FROM raw_customers
GROUP BY country
ORDER BY customer_count DESC;

-- Filter USA customers
SELECT name, email
FROM raw_customers
WHERE country = 'USA';
```

#### Step 3: Sales Data Analysis

```sql
-- Total revenue
SELECT SUM(total) as total_revenue
FROM raw_sales;

-- Revenue by region
SELECT 
    region,
    COUNT(*) as num_sales,
    SUM(total) as total_revenue,
    ROUND(AVG(total), 2) as avg_sale
FROM raw_sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Top selling products
SELECT 
    product,
    SUM(quantity) as units_sold,
    SUM(total) as revenue,
    COUNT(DISTINCT customer_id) as unique_customers
FROM raw_sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- Monthly revenue trend
SELECT 
    DATE_FORMAT(CAST(sale_date AS DATE), '%Y-%m') as month,
    SUM(total) as monthly_revenue,
    COUNT(*) as num_sales
FROM raw_sales
GROUP BY DATE_FORMAT(CAST(sale_date AS DATE), '%Y-%m')
ORDER BY month;

-- High value customers (>$10,000 total purchases)
SELECT 
    customer_id,
    COUNT(*) as num_purchases,
    SUM(total) as total_spent
FROM raw_sales
GROUP BY customer_id
HAVING SUM(total) > 10000
ORDER BY total_spent DESC;
```

#### Step 4: Join Queries

```sql
-- Join customers with sales
SELECT 
    c.name,
    c.country,
    COUNT(s.sale_id) as num_purchases,
    SUM(s.total) as total_spent
FROM raw_customers c
JOIN raw_sales s ON c.customer_id = s.customer_id
GROUP BY c.name, c.country
ORDER BY total_spent DESC
LIMIT 10;
```

#### Step 5: Query Parquet (Processed Data)

```sql
-- Query processed regional data
-- (Faster than raw data, columnar format)
SELECT *
FROM processed_sales_by_region;

-- Query partitioned clean data
SELECT 
    product,
    SUM(total) as revenue
FROM processed_sales_clean
WHERE region = 'North'
GROUP BY product;
```

### Create Athena Table Manually (Without Crawler)

```sql
-- Create external table pointing to S3
CREATE EXTERNAL TABLE IF NOT EXISTS sales_manual (
    sale_id INT,
    product STRING,
    quantity INT,
    price DOUBLE,
    region STRING,
    sale_date STRING,
    customer_id INT,
    total DOUBLE
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://my-learning-bucket-2024-unique/data-lake/raw/sales/';

-- Query it
SELECT * FROM sales_manual LIMIT 10;
```

### Create Partitioned Table

```sql
-- Create partitioned table for better performance
CREATE EXTERNAL TABLE sales_partitioned (
    sale_id INT,
    product STRING,
    quantity INT,
    price DOUBLE,
    sale_date STRING,
    customer_id INT,
    total DOUBLE
)
PARTITIONED BY (region STRING)
STORED AS PARQUET
LOCATION 's3://my-learning-bucket-2024-unique/processed/sales/clean-data/';

-- Add partitions
MSCK REPAIR TABLE sales_partitioned;

-- Query specific partition (scans less data = cheaper + faster)
SELECT * 
FROM sales_partitioned
WHERE region = 'North'
LIMIT 10;
```

### Athena Best Practices

```
COST OPTIMIZATION:
  ✓ Use columnar formats (Parquet, ORC)
    - Scan only needed columns
    - 5-10x cheaper than CSV/JSON
  
  ✓ Partition data
    - By date, region, etc.
    - Scan only relevant partitions
  
  ✓ Compress data
    - Gzip, Snappy for Parquet
    - Reduce data scanned
  
  ✓ Use LIMIT for testing
    - Test queries with small data first
  
  ✓ Optimize JOIN operations
    - Put smaller table first in JOIN
    - Filter before joining

PERFORMANCE:
  ✓ Use appropriate data types
  ✓ Create statistics
  ✓ Avoid SELECT * (specify columns)
  ✓ Use WHERE clauses effectively
```

### Query Athena with boto3

```python
import boto3
import time

athena = boto3.client('athena')

def run_athena_query(query, database, output_location):
    """Execute Athena query and return results"""
    
    # Start query execution
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': output_location}
    )
    
    query_execution_id = response['QueryExecutionId']
    print(f"Query execution ID: {query_execution_id}")
    
    # Wait for query to complete
    while True:
        result = athena.get_query_execution(
            QueryExecutionId=query_execution_id
        )
        status = result['QueryExecution']['Status']['State']
        
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        
        print(f"Query status: {status}")
        time.sleep(2)
    
    if status == 'SUCCEEDED':
        # Get query results
        results = athena.get_query_results(
            QueryExecutionId=query_execution_id
        )
        
        # Parse results
        rows = results['ResultSet']['Rows']
        headers = [col['VarCharValue'] for col in rows[0]['Data']]
        data = []
        
        for row in rows[1:]:
            values = [col.get('VarCharValue', '') for col in row['Data']]
            data.append(dict(zip(headers, values)))
        
        return data
    else:
        error = result['QueryExecution']['Status'].get('StateChangeReason', 'Unknown error')
        raise Exception(f"Query failed: {error}")

# Example usage
query = """
SELECT region, COUNT(*) as sales_count
FROM raw_sales
GROUP BY region
"""

results = run_athena_query(
    query=query,
    database='my_data_lake',
    output_location='s3://my-learning-bucket-2024-unique/athena-results/'
)

for row in results:
    print(row)
```

### Complete Data Lake Workflow

```
COMPLETE PIPELINE:
┌─────────────────────────────────────────────────┐
│                                                 │
│  1. INGEST                                      │
│     → Upload data to S3 (raw/)                  │
│     → Manual upload, Lambda, Data Firehose      │
│                                                 │
│  2. CATALOG                                     │
│     → Glue Crawler discovers schema             │
│     → Creates tables in Data Catalog            │
│                                                 │
│  3. TRANSFORM                                   │
│     → Glue ETL Job cleans & transforms          │
│     → Writes to S3 (processed/)                 │
│     → Scheduled or event-driven                 │
│                                                 │
│  4. CATALOG PROCESSED                           │
│     → Another crawler for processed data        │
│     → Update Data Catalog                       │
│                                                 │
│  5. ANALYZE                                     │
│     → Athena SQL queries                        │
│     → Fast, serverless analytics                │
│                                                 │
│  6. VISUALIZE (Optional)                        │
│     → QuickSight dashboards                     │
│     → Connect to Athena                         │
│                                                 │
│  All managed, serverless, pay-per-use!          │
└─────────────────────────────────────────────────┘
```

---

## Summary & Next Steps

### What You've Learned

**Foundations:**

- Cloud computing concepts and benefits
- AWS account setup and security
- IAM for access management
- Global infrastructure (Regions, AZs)

**Compute:**

- EC2 for virtual servers
- Lambda for serverless functions

**Storage:**

- S3 for object storage
- Different storage types (Block, Object, File)
- S3 SDK for programmatic access

**Data Processing:**

- AWS Glue for ETL
- Crawlers for data cataloging
- Building data pipelines
- Athena for SQL analytics

### Practice Projects

1. **Build a Serverless API**
   - Lambda functions
   - API Gateway
   - DynamoDB for data storage

2. **Create a Data Lake**
   - Store logs in S3
   - Use Glue to transform
   - Query with Athena
   - Visualize with QuickSight

3. **Image Processing Pipeline**
   - Upload image to S3
   - Lambda resizes image
   - Store thumbnails in S3
   - Track metadata in DynamoDB

4. **Log Analysis System**
   - Collect application logs
   - Store in S3
   - Process with Glue
   - Analyze with Athena

### Additional AWS Services to Explore

```
DATABASES:
  • RDS (Relational Database Service)
  • DynamoDB (NoSQL)
  • Aurora (High-performance MySQL/PostgreSQL)

MESSAGING:
  • SQS (Simple Queue Service)
  • SNS (Simple Notification Service)
  • EventBridge (Event bus)

MONITORING:
  • CloudWatch (Logs, Metrics, Alarms)
  • X-Ray (Distributed tracing)

CI/CD:
  • CodeCommit, CodeBuild, CodeDeploy
  • CodePipeline

CONTAINERS:
  • ECS (Elastic Container Service)
  • EKS (Elastic Kubernetes Service)
  • Fargate (Serverless containers)

MACHINE LEARNING:
  • SageMaker (ML platform)
  • Rekognition (Image/Video analysis)
  • Comprehend (NLP)
```

### Certification Paths

```
1. AWS Certified Cloud Practitioner
   └─► Entry level, foundational knowledge

2. AWS Certified Solutions Architect - Associate
   └─► Design and deploy AWS systems

3. AWS Certified Developer - Associate
   └─► Develop and maintain AWS applications

4. AWS Certified Data Engineer - Associate
   └─► Data ingestion, transformation, and orchestration
```

### Learning Resources

- **AWS Free Tier**: Hands-on practice
- **AWS Documentation**: Official guides
- **AWS Skill Builder**: Free training courses
- **AWS Workshops**: Step-by-step labs
- **YouTube**: AWS Online Tech Talks
- **GitHub**: AWS samples and examples

### Cost Management Tips

```
STAY WITHIN FREE TIER:
✓ Set up billing alerts
✓ Monitor usage in Billing Dashboard
✓ Stop EC2 instances when not in use
✓ Delete unused resources
✓ Use AWS Cost Explorer
✓ Enable AWS Budgets
✓ Review monthly bills carefully

FREE TIER LIMITS:
• Lambda: 1M requests/month
• S3: 5 GB storage
• EC2: 750 hours/month (t2.micro)
• Athena: Pay per TB scanned
• Glue: First 1M requests free for crawlers
```

---

**End of AWS Learning Guide**

You now have a comprehensive foundation in AWS cloud services. Keep practicing, building projects, and exploring new services. The cloud is constantly evolving, so continuous learning is key!
