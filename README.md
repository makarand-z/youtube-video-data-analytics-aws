# 🎬 Youtube Video Data Analytics using AWS

## 📝 Overview

This project aims to analyze the popularity of YouTube content across different regions by using data on trending videos from the platform itself. The process is divided into a few basic steps - data preprocessing, cleaning, and analysis by leveraging AWS services like S3, Lambda, Glue, and Athena to build an automated ETL pipeline

## 🎯 Project Goals
1. Data Ingestion - Create a data ingestion pipeline to extract new incoming data into the AWS data lake
2. Data Lake - Create a centralized repository to store data from multiple sources and of different formats
3. Data ETL Jobs - Create Extract, Transform, and Load jobs to preprocess raw data into usable proper versions
4. Data Analysis - Create SQL queries to analyze data to create key insights about the product
5. Data Reporting/Analytics - Create dashboards to answer questions and communicate insights to the Stakeholders

## 🗂️ Dataset Used

The dataset includes daily statistics for up to 200 trending YouTube videos per day, covering several months. It focuses on major regions such as US, GB, DE, CA, JP, IN, and FR regions (USA, Great Britain, Germany, Canada, Japan, India, and France, respectively)
- There are two parts to this dataset:
  - 1) Each region’s trending video data is stored in a separate CSV file, with columns like video title, channel title, publish time, tags, views, likes, dislikes, description, and comment count
  - 2) Video categories are provided in separate JSON files for each region, linking each video to its category

Dataset link: https://www.kaggle.com/datasets/datasnaek/youtube-new

<p align="center">
  <img width="200" height="250" src="https://github.com/user-attachments/assets/e23eacf9-32c9-4910-b411-cbd82c8fc330">
  <h6 align = "center" > Source: google </h6>
</p>

## ☁️ Amazon Web Services Used in This Project

1. **AWS S3**: Serves as the main storage layer, providing scalable, secure, and highly available storage for all data files. Data is saved as objects within buckets, making it easy to organize, access, and integrate with other AWS services <br />
2. **AWS IAM**: Manages user access and permissions securely across all AWS services used in the project. IAM controls who can sign in and what actions they can perform, ensuring only authorized users can access sensitive resources <br />
3. **AWS Glue**: Acts as the serverless ETL and data integration tool for the project. Glue discovers, prepares, and combines data for analytics and reporting. It automatically crawls data, updates the data catalog, and enables seamless data transformation and workflow automation <br />
4. **AWS Lambda**: Provides serverless compute power for running custom Python code to process and clean new data as soon as it’s uploaded. Lambda functions are triggered automatically and scale with demand—no server management required <br />
5. **AWS Athena**: Enables fast, interactive analysis of data stored in S3 using standard SQL. Athena lets you explore and query large datasets without having to manage infrastructure, and can also be used to run Spark-based analytics <br />
6. **AWS QuickSight**: Powers the business intelligence layer, allowing you to create dashboards and visual reports. QuickSight supports integration with AWS, third-party, and spreadsheet data, making it easy for stakeholders to explore insights and answer key business questions 
