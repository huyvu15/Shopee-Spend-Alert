---
title : "Add Trigger và permissions cho S3"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---

#### Add Trigger và permissions cho S3




1. Truy cập vào giao diện **Lambda**

   - Chọn **Function**
   - Chọn **Crawl_data**

![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/1.png?featherlight=false&width=90pc)

2. Tại Function **Crawl_data**
   - Chọn **Add Trigger** .

![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/2.png?featherlight=false&width=90pc)

3. Tại giao diện **Add trigger**
   - Tại bucket chọn **S3/workshoph**.
   - Event types chọn **All object create events** .
   - Tích vào ô ở cuối xong ấn **add trigger** .

![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/3.png?featherlight=false&width=90pc)

4. Configure quyền cho S3
   - Tại giao diện **function**
   - Chọn **Configuration**
   - Chọn **Permissions**
   - Click đường dẫn ở **Role_name** .


![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/4.png?featherlight=false&width=90pc)

5. Tại giao diện IAM
 - Chọn **Attach policies** .
 - Tìm **```AmazonS3FullAccess```** và tích vào.
 - **Add permissions** .
![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/5.png?featherlight=false&width=90pc)


![Create VPC](/images/4-CreateEc2Server/4.4-addtrigger/6.png?featherlight=false&width=90pc)

{{% notice tip %}}
Trong dự án thực tế chúng ta sẽ set quyền rất chặt cho việc truy cập vào s3 tuy nhiên để bài lab này được thực hiện đơn giản hơn. Chúng ta sẻ sử dụng quyền cao nhất đối với S3(Full Acess).
{{% /notice %}}








