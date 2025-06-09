# 🎬 Youtube Video Data Analytics using AWS

## 📝 Overview

This project aims to analyze the popularity of YouTube content across different regions by using data on trending videos from the platform itself. The process is divided into a few basic steps - data preprocessing, cleaning, and analysis by leveraging AWS services like S3, Lambda, Glue, and Athena to build an automated ETL pipeline.

## 🎯 Project Goals
1. Data Ingestion - Create a data ingestion pipeline to extract new incoming data into the AWS data lake
2. Data Lake - Create a centralized repository to store data from multiple sources and of different formats
3. Data ETL Jobs - Create Extract, Transform, and Load jobs to preprocess raw data into usable proper versions
4. Data Analysis - Create SQL queries to analyze data to create key insights about the product
5. Data Reporting/Analytics - Create dashboards to answer questions and communicate insights to the Stakeholders

## 🗂️ Dataset Used

The dataset includes daily statistics for up to 200 trending YouTube videos per day, covering several months. It focuses on major regions such as US, GB, DE, CA, JP, IN, and FR regions (USA, Great Britain, Germany, Canada, Japan, India, and France, respectively)
- There are two parts to this dataset:
  - 1) Each region’s trending video data is stored in a separate CSV file, with columns like video title, channel title, publish time, tags, views, likes, dislikes, description, and comment count.
  - 2) Video categories are provided in separate JSON files for each region, linking each video to its category.

Dataset link: https://www.kaggle.com/datasets/datasnaek/youtube-new

<p align="center">
  <img width="200" height="250" src="https://github.com/user-attachments/assets/e23eacf9-32c9-4910-b411-cbd82c8fc330">
  <h6 align = "center" > Source: google </h6>
</p>

## ☁️ Amazon Web Services Used in This Project

1. **AWS S3**: Serves as the main storage layer, providing scalable, secure, and highly available storage for all data files. Data is saved as objects within buckets, making it easy to organize, access, and integrate with other AWS services. <br />
2. **AWS IAM**: Manages user access and permissions securely across all AWS services used in the project. IAM controls who can sign in and what actions they can perform, ensuring only authorized users can access sensitive resources. <br />
3. **AWS Glue**: Acts as the serverless ETL and data integration tool for the project. Glue discovers, prepares, and combines data for analytics and reporting. It automatically crawls data, updates the data catalog, and enables seamless data transformation and workflow automation. <br />
4. **AWS Lambda**: Provides serverless compute power for running custom Python code to process and clean new data as soon as it’s uploaded. Lambda functions are triggered automatically and scale with demand—no server management required. <br />
5. **AWS Athena**: Enables fast, interactive analysis of data stored in S3 using standard SQL. Athena lets you explore and query large datasets without having to manage infrastructure, and can also be used to run Spark-based analytics. <br />
6. **AWS QuickSight**: Powers the business intelligence layer, allowing you to create dashboards and visual reports. QuickSight supports integration with AWS, third-party, and spreadsheet data, making it easy for stakeholders to explore insights and answer key business questions.

## 🔃 Data Architecture Diagram

<img src="https://github.com/user-attachments/assets/80e9dd91-2b6f-460c-bf72-a39bb4d1a62c">

## Implementation

#### **Step 1** - Ingest data into Amazon S3 buckets from our project directory. The first step includes uploading data from our Kaggle dataset to Amazon S3 buckets by running a shell script through AWS CLI.
<p align="center">
  <img src="https://github.com/user-attachments/assets/89112552-ac8a-429a-8adc-43eb63e435f1">
  <h6 align = "center" > Source: Author </h6>
</p>
&nbsp;

#### **Step 2** - Create a central repository to store metadata of all the data assets.
<p align="center">
  <img src="https://github.com/user-attachments/assets/1d472df9-a184-4bb5-842a-32b145627889">
  <h6 align = "center" > Source: Author </h6>
</p>
  Understanding the structure of each data asset is crucial for your project. AWS Glue Crawler scans all data sources, automatically detects their schema, structure, and formats, and stores this information in the AWS Glue Catalog. The Glue Catalog organizes metadata into databases and tables, making it easy to manage and query. Each Glue table contains key metadata details like column names, data types, and   partition keys.
&nbsp;

#### **Step 3** - Create a AWS Lambda function that processes any new incoming data based on S3 Put trigger and stores it in cleansed Amazon S3 buckets.
<p align="center">
  <img src="https://github.com/user-attachments/assets/cbe985b5-5c07-4c01-8344-6fad924db0b9">
  <h6 align = "center" > Source: Author </h6>
</p>
  AWS Lambda allows serverless compute functionality to run code in python (in this case) to process data according to business requirements. In our case, we will convert our data format from .json to parquet and store it new bucket. Parquet is an efficient data format than csv and json and is consistent across the data pipeline. It also creates updated data catalog in AWS Glue Catalog with updated schemas and column datatypes.

#### **Step 4** - Create ETL jobs to extract data from S3 buckets, apply join transformation and load for consumption through business intelligence applications.
<p align="center">
  <img src="https://github.com/user-attachments/assets/d15d7907-553e-4168-a156-3d2f6d2a77b0">
  <h6 align = "center" > Source: Author </h6>
</p>
  To avoid manual data processing each time, we set up automated ETL jobs that handle both data preparation and delivery to stakeholders - data analysts/data scientists. In this project, we join the two dataframes on the category_id and id columns to produce a final, cleaned dataset ready for analysis in business layer (gold layer based on the medallion architecture). The script for this process is included in the files section.
<p align="center">
  <img src="https://github.com/user-attachments/assets/b1416b89-28e9-44d2-8cee-f1732ec6994e">
  <h6 align = "center" > Source: Author </h6>
</p>

#### **Step 5** - Create a dashboard to visualize and answer questions according to business requirements or perform data analytics by loading our business layer data present in AWS Athena as dataset into AWS QuickSight
<p align="center">
  <img width="620" alt="Image" src="https://github.com/user-attachments/assets/e2725992-371a-4548-aa69-e3a7e13329dc" />
  <h6 align = "center" > Source: Author </h6>
</p>
