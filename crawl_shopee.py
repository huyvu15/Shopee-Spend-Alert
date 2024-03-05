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
    cookies = {
        '_gcl_au': '1.1.1889263762.1707193883',
        'SPC_F': 'ZYCVs3p4uPkKrC94xPBDZ7yd8QqcAo0F',
        'REC_T_ID': '96ebab8a-c4a8-11ee-ae72-0e7a5db6fafe',
        '_hjSessionUser_868286': 'eyJpZCI6IjQzMWNmNTkzLTQ5ZjUtNTRmNi1iMThmLTdhMjdlNDNkNjE0ZSIsImNyZWF0ZWQiOjE3MDcxOTM4OTU5OTcsImV4aXN0aW5nIjp0cnVlfQ==',
        'SPC_CLIENTID': 'WllDVnMzcDR1UGtLfsznlqhdmhdkkmle',
        '_fbp': 'fb.1.1708186293461.1375126532',
        '_gcl_aw': 'GCL.1708351948.CjwKCAiAlcyuBhBnEiwAOGZ2S4U4LkyZM7_Of3FuAFf__Xv3ScFpccEPE0OUNFXpA9x1WMTiUuIVlBoCsdAQAvD_BwE',
        '_gac_UA-61914164-6': '1.1708351956.CjwKCAiAlcyuBhBnEiwAOGZ2S4U4LkyZM7_Of3FuAFf__Xv3ScFpccEPE0OUNFXpA9x1WMTiUuIVlBoCsdAQAvD_BwE',
        '_med': 'affiliates',
        'SPC_EC': '.WFptWjRkbTJxNzF6Z2xrOas22RtIt3UI+Wh7Otzh+cf768Fy48+XaWBe5S9/Jgbv7eZichROzF3sNlhw4CTjQPef58+dPQDmnOmdSIcg/3peAfjFd8I8HvzZNTxdINlQUWtmkH5nEJMp1ebcQw46S5slLqWQVXUZd96lOGPaLPBGg1tSQ1pCpo/YcWJnX6REtTBzi/UrYczr0tNs5zAaIw==',
        'SPC_ST': '.WFptWjRkbTJxNzF6Z2xrOas22RtIt3UI+Wh7Otzh+cf768Fy48+XaWBe5S9/Jgbv7eZichROzF3sNlhw4CTjQPef58+dPQDmnOmdSIcg/3peAfjFd8I8HvzZNTxdINlQUWtmkH5nEJMp1ebcQw46S5slLqWQVXUZd96lOGPaLPBGg1tSQ1pCpo/YcWJnX6REtTBzi/UrYczr0tNs5zAaIw==',
        'SPC_U': '392197148',
        'SPC_T_IV': 'YlViU2ZxSXAxaGp0bDA5Zw==',
        'SPC_R_T_ID': 'r+gFYGqzvWmvpGgfjYCtzLIPF7W1rBEqHLVrD2H5SIwhBBt8FexDTWSYKsdibuyCQrfzBL4tfnNkYOQaDiR+8IOIfxV8RuTBOd4/xuoxT6ckhhGSTuPcOjQToDwn/+ZMB/eC3awm4VYYh/Qg/Are9DGCJimVTu41F/wiWKovubw=',
        'SPC_R_T_IV': 'YlViU2ZxSXAxaGp0bDA5Zw==',
        'SPC_T_ID': 'r+gFYGqzvWmvpGgfjYCtzLIPF7W1rBEqHLVrD2H5SIwhBBt8FexDTWSYKsdibuyCQrfzBL4tfnNkYOQaDiR+8IOIfxV8RuTBOd4/xuoxT6ckhhGSTuPcOjQToDwn/+ZMB/eC3awm4VYYh/Qg/Are9DGCJimVTu41F/wiWKovubw=',
        '__LOCALE__null': 'VN',
        'csrftoken': 'LnGOL9AjJgLCaG02ywUWONTIIXP0qz9u',
        '_sapid': 'c945e9a9d5f328cc21089e05f57689da47e0a6ba559cd17a98ee27fd',
        'SPC_SI': 'CFPUZQAAAABLMnA2eXZUbLGI5gEAAAAAYXIwdFlWS1o=',
        'SPC_SEC_SI': 'v1-WDZuWVJocUlWaXFqVm1RbmLzaj5E1npoO0trOOhKfdq+OvsnORcyLWyYtt8uox03Z533Y/wku7X4STk/PSoDH9tEwiE503G4I+7GSgGhjjs=',
        '_QPWSDCXHZQA': 'c523b53b-4513-4b5c-fc98-7e7b0368c981',
        'REC7iLP4Q': 'd610c659-81eb-4518-b171-1913d3ce1e99',
        '_hjSession_868286': 'eyJpZCI6IjE5N2U2OTAwLTI4YjktNGMyNi05YzFjLTJmY2ExYWY0OWRiMSIsImMiOjE3MDkzODg1OTUwNTQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        'shopee_webUnique_ccd': '7ObAwemrGvcp2UehJxmEkw%3D%3D%7CMH3E86A%2FiLQFr8q6Z4VoIUrhL7g0%2F%2FPPAghPkaE3AJP3Q1oAZINezjDoJyFqVb6BdE2EQtenvyg%3D%7CyIPrY%2BSa2rGKhF7N%7C08%7C3',
        'ds': 'bcdddc301ee3a2d1acc477e1dc86bb5d',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_ga': 'GA1.2.1324904971.1707193886',
        '_gid': 'GA1.2.1991934226.1709388596',
        '_dc_gtm_UA-61914164-6': '1',
        '_ga_4GPP1ZXG63': 'GS1.1.1709388594.15.1.1709388643.11.0.0',
        }
        
    headers = {
            'authority': 'shopee.vn',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,vi;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'af-ac-enc-sz-token': '7ObAwemrGvcp2UehJxmEkw==|MH3E86A/iLQFr8q6Z4VoIUrhL7g0//PPAghPkaE3AJP3Q1oAZINezjDoJyFqVb6BdE2EQtenvyg=|yIPrY+Sa2rGKhF7N|08|3',
            'content-type': 'application/json',
            'referer': 'https://shopee.vn/user/purchase/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-api-source': 'pc',
            'x-csrftoken': 'LnGOL9AjJgLCaG02ywUWONTIIXP0qz9u',
            'x-requested-with': 'XMLHttpRequest',
            'x-sap-ri': '6633e3654342b8fd10de2e390301a27c458973b6245a16b2987c',
            'x-sap-sec': '7GNCltcs2xJpKxJpL/JrKxcpL/JpKxcpKxJsKxJp0xhpKfFhKxJHKxJp2jilAEFpKx5XK/JpfxepKbFGP2d9/Pzw5ekRlyhYJMdq3jFcdB0cSqsS47EVpKuibXrRamU7yitj2idfiIhRceScltDqo8F0QJ4qeVB/aNvpIMlJkzL0VJlKf7pU4WBczSOboUx/T8atDCzotRS7R3TFShz7+Y9ZwNWP52DUp1lSPgcPVRy4bS9+Nd1gYkvN75oBkjStAwGde/lT11qpnSiEG6WXsjM/GcSVbbZ9oBOtMT0aHyqz7phnazF6DD1n8XfNNV6gr2UW7dH4i8wC17HPBFjUUcNF/Q1rEItXM61VJG4xCQrJxeY/YJ+zZlrA3a3w6kScBfJXwX0I4tK7GbxGHCtWeGY0ki0tKucvGTRmEsmayU2gekVNUEz2gfbMIZdVXacODieYe0bBwLaU/5NSdreL9kkclWnMEUQbX/NGUMCEjrq2sCq/gO7pX+SphPi/5UBZnzoscXdwH6nER4GAHBUXNstE8n4qwOspD0U/Y4J33usDuF0lV1g80F2Q0C3CtQBJ+UU8BgeX9dugJAudIQL1d4U6hgj0j/rOWkUNLpWsd0EgbXk9CoCz1FKdsXTGZwr699eqjJiHD+twfVyebBpit+VTpk1ThAxWI6MPU8LJLkivp2bIHDAA09Gp6qHZ0a3aPujEzb1ac81poUvktwoxRfr9T+rdKQZR/uw2xmgDAkGFAJExvAqYKu6RHg7mR2qoSH69xmOXNM2yFsBAR3OajlYtbpp68U3cWF8AXlxHtt+3TbjVJs3sFCAkDzrnAs5qyxXqtRkdCbAJrEPxpFF2FJtO7Dx7vd/sC5dWm2eIKf78K4HmZiNRqb0cIs39bc00mRksR6ZJQKbB05HGd5ZNZ4Z0yDknw0MlAzdHK90k3OGjouXEfod7NkpN55d38rwJuln9emBofV5ovvFpKxJiP6Lxc6LwQEJpKx45ArYl0xJpKZmpKxJ6KxJpO2OWtrRJwIuf7kxU7pgt/VYRUAJrKxJpP0hxOq3xPVhpKxJp0xJ5KxFpLxJrKxJp0xJpKZmpKxJ6KxJp7WHmhK3itDx01mfYK84EyGxkzuLrKxJpcVMYOHPwdbLpKxJp',
            'x-shopee-language': 'vi',
            'x-sz-sdk-version': '1.6.16',
        }
        
    params = {
            'limit': '5',
            'offset': '0',
        }
        
    response = requests.get(
        'https://shopee.vn/api/v4/order/get_all_order_and_checkout_list',
        params=params,
        cookies=cookies,
        headers=headers,
    )

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
    bucket_name = '<<bucket_name>>'
    file_key = 'bill1.csv'
    
    s3.put_object(Body=csv_buffer_bytes, Bucket=bucket_name, Key=file_key, ContentType='text/csv; charset=utf-8')
    
    df['time'] = pd.to_datetime(df['time'])
    start_of_current_month = pd.Timestamp.now().replace(day=1)
    start_of_previous_month = start_of_current_month - pd.offsets.MonthBegin(1)
    data_previous_month = df[df['time'].dt.to_period('M') == start_of_previous_month.to_period('M')]
    total_price_previous_month = data_previous_month['price'].sum()
    
    return total_price_previous_month

def lambda_handler(event, context):
    # TODO implement
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
            
    FROM_EMAIL_ADDRESS = ""
    TO_EMAIL_ADDRESSES = ""
    PASSWORD = ""

    subject = "Notification of spending on shopping in last month"
    msg = "Hello \nYou are spend "+ str(result)+ " for shopping activities at shopee" 


    send_email(subject, msg, TO_EMAIL_ADDRESSES)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }