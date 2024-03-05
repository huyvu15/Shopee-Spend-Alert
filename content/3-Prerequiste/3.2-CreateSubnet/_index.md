---
title : "Tạo Lambda Function"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.2 </b> "
---

#### Tạo Lambda Function

1. Trong giao diện **AWS Management Console**

   - Chọn **Lambda**

![Create VPC](/images/3-Prerequiste/3.2-lambda/1.png?featherlight=false&width=90pc)

2. Trong giao diện **Lambda Function**

   - Chọn **Function**
   - Chọn **Create Function**

![Create VPC](/images/3-Prerequiste/3.2-lambda/2.png?featherlight=false&width=90pc)


3. Thực hiện **cấu hình Function**

   - **Function name**, nhập **```Crawl_data```**
   - Chọn Runtime **Python 3.10**
   - Chọn **Create Function**

![Create VPC](/images/3-Prerequiste/3.2-lambda/3.png?featherlight=false&width=90pc)


4. Hoàn thành tạo **Function**
![Create VPC](/images/3-Prerequiste/3.2-lambda/4.png?featherlight=false&width=90pc)



<!-- {{% notice tip %}}
Một điểm đáng chú ý nữa là các subnet về cơ bản đều giống nhau, thông qua cấu hình route table và cấp phát public IP address mà chúng ta mới phân chia ra Public và Private Subnet.
{{% /notice %}} -->




