---
title : "Lấy cookie từ shopee"
date :  "`r Sys.Date()`" 
weight : 4 
chapter : false
pre : " <b> 4. </b> "
---

#### Lấy cookie từ shopee

Ở bước này chúng ta sẽ thực hiện lấy cookie từ shopee

1. Truy cập vào **```Shopee.com```**
    - Chọn **Đơn mua**.

![Create VPC](/images/4-CreateEc2Server/2.png?featherlight=false&width=90pc)

2. Tại giao diện Đơn hàng
    - Click chuột phải chọn **inspect** .

![Create VPC](/images/4-CreateEc2Server/3.png?featherlight=false&width=90pc)

3. Tại giao diện backend
    - Click vào **Network** .
    - Loading lại trang kém xuống tìm **get_all_order_and_checkout_list?limit=5&offset=0**
    - Di chuột vào phần copy. Chọn **Copy all as cURL(bash)**

![Create VPC](/images/4-CreateEc2Server/4.png?featherlight=false&width=90pc)

4. Mở tab mới và vào link: **```https://curlconverter.com/```**
    - Dán phần vừa copy vào **curl command** .
    - Tiếp tục **copy** phần trả về phía dưới. 

![Create VPC](/images/4-CreateEc2Server/5.png?featherlight=false&width=90pc)

{{% notice tip %}}
Một điểm đáng chú ý nữa là thi thoảng web bị lỗi trong trường hợp copy nhiều lần thì cái trả về sẽ sinh ra nhiều code và liên tục bị trồng lên nhau. Nếu gặp trường hợp như vậy thì chỉ nên **copy** từ phần **import** đến hết **respon()**.
{{% /notice %}}





#### Nội dung 

1. [Lấy mật khẩu ứng dụng Gmail](4.1-createec2/)
2. [Trích xuất thông tin file json](4.2-connectec2/)
3. [Thêm code vào Lambda Function](4.3-natgateway/)
<!-- 4. [Sử dụng Reachability Analyzer](4.4.-createreachabilityanalyzer/)
5. [Tạo EC2 Instance Connect Endpoint](4.5-EICEndpoint/) -->