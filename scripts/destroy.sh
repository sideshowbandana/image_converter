#!/bin/sh

set -ex

accountNumber=202305538718 # put your AWS account number here
apexProject=image_converter # put your Apex project name here (as named in project.json file)

apex delete
aws iam detach-role-policy --role-name ${apexProject}_lambda_function --policy-arn arn:aws:iam::${accountNumber}:policy/${apexProject}_lambda_logs
aws iam delete-policy --policy-arn arn:aws:iam::${accountNumber}:policy/${apexProject}_lambda_logs
aws iam delete-role --role-name ${apexProject}_lambda_function
