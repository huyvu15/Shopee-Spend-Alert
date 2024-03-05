---
title : "Dọn dẹp tài nguyên"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 6. </b> "
---
#### Dọn dẹp tài nguyên

Trong bài lab này chúng ta đã sử dụng các dịch vụ S3, Lambda Function, EventBridge. Các dịch vụ này đều có chi phí khá là rẻ và free cho tài khoản 12 tháng nên ko cần phải xóa tài nguyên.

Nếu vẫn muốn xóa thì đây là lần lượt các bước:

### Xóa S3 Bucket
Vào S3 chọn bucket và chọn **workshoph** và chọn Empty. sau đó chọn **Delete** làm theo các hiển thị tiếp theo để xóa.

### Xóa shedule EventBridge 
Vào EventBridge chọn shedule và chọn **send-email** và chọn **Delete**.

### Xóa Lambda function
Vào Lambda function chọn function chọn **Crawl_data** và chọn **Actions** chọn **Delete** để xóa.


