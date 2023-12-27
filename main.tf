provider "aws" {
  region     = "us-east-1"
  access_key = ""
  secret_key = ""
  token      = ""
}

data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "final_security_group" {
  vpc_id      = data.aws_vpc.default.id
  name        = "final_security_group"
  description = "My final security group"

  #SSH use
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #HTTP use
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #HTTPS use
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    from_port        = 1186
    to_port          = 1186
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_instance" "t2_micro_standalone" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-east-1 region
  instance_type          = "t2.micro"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f" 
  count                  = 1
  private_ip             = "172.31.17.2"
  tags                   = {
    Name = "standalone"
  }
}

resource "aws_instance" "t2_micro_manager" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-east-1 region
  instance_type          = "t2.micro"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.3"
  count                  = 1
  tags = {
    Name = "master"
  }
}

resource "aws_instance" "worker1" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-est-2 region
  instance_type          = "t2.micro"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.4"
  
  tags = {
    Name = "worker-1"
  }
}

resource "aws_instance" "worker2" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-est-2 region
  instance_type          = "t2.micro"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.5"
  
  tags = {
    Name = "worker-2"
  }
}
resource "aws_instance" "worker3" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-est-2 region
  instance_type          = "t2.micro"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.6"
  
  tags = {
    Name = "worker-3"
  }
}


resource "aws_instance" "t2_large_proxy" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-east-1 region
  instance_type          = "t2.large"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.7"
  count                  = 1
  tags = {
    Name = "proxy"
  }
}

resource "aws_instance" "t2_large_gatekeeper" {
  ami                    = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS image ID in us-east-1 region
  instance_type          = "t2.large"
  key_name               = "vockey"
  vpc_security_group_ids = [aws_security_group.final_security_group.id]
  subnet_id              = "subnet-0e9058cb01bac003f"
  private_ip             = "172.31.17.8"
  count                  = 1
  tags = {
    Name = "gatekeeper"
  }
}