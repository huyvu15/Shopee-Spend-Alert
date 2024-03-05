---
title : "Thêm code vào lambda function"
date :  "`r Sys.Date()`" 
weight : 3 
chapter : false
pre : " <b> 4.3 </b> "
---

#### Thêm code vào lambda function

1. Truy cập **Lambda Function**

   - Chọn **Function**
   - Chọn **Crawl_data**

![Create VPC](/images/4-CreateEc2Server/4.3-addcode/1.png?featherlight=false&width=90pc)


2. Kéo xuống và **copy** đoạn code sau vào **lambda function**, sửa thêm 1 số cái:
   - Với **cookie, header, params, response** để copy ở phần trước đó.(nhớ tag lại)
   - Thay đổi **email cần gửi** và **email nhận.**

![Create VPC](/images/4-CreateEc2Server/4.3-addcode/2.png?featherlight=false&width=90pc)

```python
import json
import requests
import datetime
import time
import boto3 
import os
from io import BytesIO
import pandas as pd
import io
import smtplib

def crawl():
    "<cookie-api>"# Lấy từ shopee từ bước 
    products = []

    for i in range(0, 301, 5):
        params['offset'] = i
        response = requests.get('https://shopee.vn/api/v4/order/get_all_order_and_checkout_list', headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            data = response.json().get('data').get('order_data').get('details_list')
            if data is not None:
                for j in range(len(data)):
                        order_info = data[j]
                        main = order_info.get('info_card').get('order_list_cards')[0].get('product_info').get('item_groups')[0].get('items')[0]
                        main1 = order_info.get('info_card').get('order_list_cards')[0].get('shop_info')
                        main2 = order_info.get('shipping', {}).get('tracking_info', {})
                        product_id = main.get('item_id')
                        shop_id = main1.get('shop_id')
                        shop_name = main1.get('shop_name')
                        name = main.get('name')
                        price = main.get('item_price') / 100000 
                        amount = main.get('amount')
                        shop_name = main1.get('shop_name')
                        status = main2.get('description', 'Đã hủy')
                        if status == 'Đã hủy':
                            status = None  
                            time = None    
                        else:
                            time = datetime.datetime.fromtimestamp(main2.get('ctime', 0))
                    
                        products.append({
                            'product_id': product_id,
                            'shop_id': shop_id,
                            'product_name': name,
                            'shop_name': shop_name,
                            'price': price,
                            'amount': amount,
                            'status': status,
                            'time': time
                        })
    return products        

def save_to_s3(products):    
    df = pd.DataFrame(products)
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    
    csv_buffer.seek(0)
    csv_buffer_bytes = csv_buffer.getvalue()
    
    s3 = boto3.client('s3')
    bucket_name = 'do-lab'
    file_key = 'bill1.csv'
    
    s3.put_object(Body=csv_buffer_bytes, Bucket=bucket_name, Key=file_key, ContentType='text/csv; charset=utf-8')
    
    df['time'] = pd.to_datetime(df['time'])
    start_of_current_month = pd.Timestamp.now().replace(day=1)
    start_of_previous_month = start_of_current_month - pd.offsets.MonthBegin(1)
    data_previous_month = df[df['time'].dt.to_period('M') == start_of_previous_month.to_period('M')]
    total_price_previous_month = data_previous_month['price'].sum()
    
    return total_price_previous_month

def lambda_handler(event, context):
    products = crawl()
    result = save_to_s3(products)
    def send_email(subject, msg, toEmail):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(FROM_EMAIL_ADDRESS, PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(FROM_EMAIL_ADDRESS, toEmail, message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Email failed to send.")
            
    FROM_EMAIL_ADDRESS = "<email-gửi>"
    TO_EMAIL_ADDRESSES = "<email-nhận>"
    PASSWORD = "<mật-khẩu-ứng-dụng-gmail"

    subject = "Notification of spending on shopping"
    msg = "Hello \nYou are spend "+ str(result)+ " for shopping activities at shopee" 

    send_email(subject, msg, TO_EMAIL_ADDRESSES)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```
{{% notice note %}}
**Các phần cần sửa:**

bucket_name = <<do_lab>> // cái này để tùy ý bucket theo mong muốn.

"<<cookie-api>>: Chỗ đã copy từ trang rút gọn api 

FROM_EMAIL_ADDRESS = "<<email-gửi>>"

TO_EMAIL_ADDRESSES = "<<email-nhận>>"

PASSWORD = "<<mật-khẩu-ứng-dụng-gmail>>"

{{% /notice %}}

3. Nhấn **Deploy** để lưu code:


![Create VPC](/images/4-CreateEc2Server/4.3-addcode/3.png?featherlight=false&width=90pc)


{{% notice note %}}
Code trên đã điều chỉnh để đơn giản nhất có thể là chỉ dùng để thu thập dữ liệu và xử lý đơn giản để tính được số tiền chi tiêu trong tháng trước đó và lưu file dữ liệu vào S3. 

Có thể phát triển thêm theo hướng là dùng thư viện **pandas** để vẽ các biểu đồ, doanh thu các ngày, phân tích đánh giá như sử dụng BI tool và gửi hết tất cả những phân tích đó qua email.
{{% /notice %}}


{{% notice note %}}
Khi nhấn test code sẽ k**hông chạy được** và bị **time out** ngay lập tức. Lý do là do **lambda function** mặc định được cấu hình **time out là 3s**. Một funtion có thời gian timeout tối đa là 15p. Đây cùng là một trong những lý do lambda không được sử dụng để train các mô hình AI do thời gian time out tương đối thấp. Code trên thực hiện sẽ mất tầm **1p**. Sau đây ta sẽ đi cấu hình thời gian **time out cho Lambda**.
{{% /notice %}}


4. Cấu hình **time out**
    - Tại giao diện function chọn **Configuration**.
    - Chọn **General configuration**.
    - Chọn **Edit**.
 
![Create VPC](/images/4-CreateEc2Server/4.3-addcode/4.png?featherlight=false&width=90pc)

5. Nhập thông số:
    - Description **```Increate amout time out```**.
    - Memory **```512```**.
    - Time out **```1```**.
    - Nhấn **Save**.
![Create VPC](/images/4-CreateEc2Server/4.3-addcode/5.png?featherlight=false&width=90pc)
![Create VPC](/images/4-CreateEc2Server/4.3-addcode/6.png?featherlight=false&width=90pc)

{{% notice note %}}
Hiện tại bạn có thể nhấn luôn phím test để test thử đoạn code. Nếu có mail gửi về là thành công được 80% rồi. Tiếp theo chúng ta sẽ đi cài lịch cho Lambda Function chạy vào đầu tháng. Và kết quả thu được sẽ là số tiền đã chi cho tháng trước. 
{{% /notice %}}

![Create VPC](/images/4-CreateEc2Server/4.3-addcode/7.png?featherlight=false&width=90pc)



{{% notice tip %}}
Nếu có lỗi là do chỗ lấy thông tin từ web bị thay đổi. Hoặc là do cookies hết hạn và cần phải lặp lại các bước để lấy lại từ shopee.
{{% /notice %}}