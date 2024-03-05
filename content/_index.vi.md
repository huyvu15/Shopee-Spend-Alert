---
title : "Nhận thông báo chi tiêu cho hoạt động mua sắp tại Shopee"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
---

# Nhận thông báo chi tiêu cho hoạt động mua sắp tại Shopee

#### Tổng quan

Chúng ta đều biết rằng việc tự động hóa các quy trình kinh doanh có thể mang lại nhiều lợi ích về mặt thời gian, hiệu quả và tiết kiệm chi phí và rất nhiều sự tiện dụng. Trong bài workshop hôm nay, chúng ta sẽ tập trung vào việc xây dựng một hệ thống gửi thông báo **số tiền** đã chi cho các hoạt động mua sắp trên Shopee thông qua Gmail, bằng cách sử dụng các dịch vụ mạnh mẽ của Amazon Web Services (AWS).

Đồng thời chúng ta cùng làm quen với các Services phổ biến như sau:

**1. AWS Lambda Function:** Lambda Function cho phép chúng ta thực thi mã một cách linh hoạt mà không cần quản lý máy chủ.

**2. Amazon EventBridge:** EventBridge giúp chúng ta lên lịch và kiểm soát các sự kiện trong hệ thống của mình như điều khiển các lambda function chạy vào mỗi đầu tháng.

**3. Amazon S3:** S3 là một trong số các dịch vụ lưu trữ đám mây của AWS. Là một trong những giải pháp hữu hiệu để xây dựng data lake cho doanh nghiệp. Trong phần thực hành này S3 sẽ được sử dụng để lưu trữ các tệp đính kèm trong các email mà chúng ta sẽ gửi(file dữ liệu, ảnh phân tích). 

Tuy nhiên để đơn giản và demo một cách thuận tiện nhất có thể bài lab chỉ gửi thông báo số tiền chi tiêu trong tháng trước thông qua email. Do một ngày mình check email khá nhiều nên mình quyết định dùng nền tảng này để thực hiện. Ngoài ra có thể gửi thông báo qua zalo, telegram thông qua api. 

Ngôn ngữ chính để phục vụ workshop này là python 3.10

![Create VPC](/images/schema.png?featherlight=false&width=90pc)



#### Nội dung

1. [Giới thiệu](1-introduce/)
2. [Tường lửa trong VPC](2-firewallinvpc/)
3. [Các bước chuẩn bị](3-prerequiste/) 
4. [Lấy Cookie từ shopee](4-createec2server/)
5. [Tạo schema cho EventBridge](5-vpnsitetosite/)
6. [Dọn dẹp tài nguyên](6-cleanup/)
