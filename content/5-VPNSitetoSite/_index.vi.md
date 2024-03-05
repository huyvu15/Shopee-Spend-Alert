---
title : "Tạo schema cho EventBridge"
date :  "`r Sys.Date()`" 
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### EventBridge 

1. Truy cập vào dịch vụ **EventBridge**
    - Chọn **Rule**. 
    - **Create rule**. 
![Create VPC](/images/5-CreateVPNenv/1.png?featherlight=false&width=90pc)

![Create VPC](/images/5-CreateVPNenv/2.png?featherlight=false&width=90pc)

2. Điền các thông tin:
    - Name **```send-email```**
    - Description -  optional **```notification for shopping```**
    - Chọn **Schedule**.
    - Chọn **Continue in EventBridge Scheduler**.

![Create VPC](/images/5-CreateVPNenv/3.png?featherlight=false&width=90pc)

![Create VPC](/images/5-CreateVPNenv/4.png?featherlight=false&width=90pc)

3. Schedule pattern
    - Chọn **Recurring schedule**.
    - Tại **Schedule** type chọn **Cron-based-schedule**.
    - Tại **Cron expression** chọn đặt lịch 2h chiều mỗi ngày.

![Create VPC](/images/5-CreateVPNenv/5.png?featherlight=false&width=90pc)


**Flexible time windown** chọn **Off**.

![Create VPC](/images/5-CreateVPNenv/6.png?featherlight=false&width=90pc)

4. Select target 
    - Chọn **AWS Lambda** .
    - **Lambda function** chọn **Crawl_data**.
    - Tiếp tục chọn **NEXT** 2 lần tiếp theo.

![Create VPC](/images/5-CreateVPNenv/7.png?featherlight=false&width=90pc)

![Create VPC](/images/5-CreateVPNenv/8.png?featherlight=false&width=90pc)

![Create VPC](/images/5-CreateVPNenv/9.png?featherlight=false&width=90pc)

5. Click **Create schedule**

![Create VPC](/images/5-CreateVPNenv/10.png?featherlight=false&width=90pc)


{{% notice tip %}}
Đợi đến thời gian chỉ định và check thông báo.
{{% /notice %}}

6. Kết quả:

![Create VPC](/images/5-CreateVPNenv/result.png?featherlight=false&width=90pc)

{{% notice tip %}}
Do tháng trước mình không chi tiêu gì trên shopee nên kết quả sẽ là 0đ :)).
{{% /notice %}}


File bill.csv được lưu vào S3.

![Create VPC](/images/5-CreateVPNenv/11.png?featherlight=false&width=90pc)

Tải xuống để kiểm tra dữ liệu:

![Create VPC](/images/5-CreateVPNenv/12.png?featherlight=false&width=90pc)

{{% notice tip %}}
Từ file dữ liệu này bạn có thể tùy ý phân tích theo ý muốn.
{{% /notice %}}




**Nội dung:**
1. [EventBridge](5.1-createvpnenv/)
2. [Tạo schedule](5.2-vpnsitetosite/)
