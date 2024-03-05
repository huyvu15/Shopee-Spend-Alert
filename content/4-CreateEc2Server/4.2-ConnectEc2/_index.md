---
title : "Trích xuất thông tin từ file json"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 4.2 </b> "
---

#### Trích xuất thông tin từ file json(Chỉ xem)

{{% notice note %}}
Để trích xuất các thông tin theo ý muốn bạn cần có một mức hiểu biết nhất định về cấu trúc file json(thử bằng cách print(response.json())) từ đoạn json trả về để thực hiện đi lần lượt vào từng cái list, dictionary để lấy dữ liệu mong muốn. Công cụ hỗ trợ dễ dàng làm việc với file json hơn **```https://dev.2fbuff.com/   ```**
{{% /notice %}}

1. View một đoạn json trả về.
```python
{'error': 0,
 'data': {'order_data': {'details_list': [{'status': {'status_label': {'text': 'label_order_completed',
       'tl': False},
      'header_text': {'text': 'order_status_text_completed_thank_you_shopping',
       'tl': False},
      'header_image': 'https://deo.shopeemobile.com/shopee/shopee-orderprocessing-live-vn/completed.png',
      'list_view_status_label': {'text': 'label_completed', 'tl': False}},
     'shipping': {'tracking_info': {'driver_phone': '',
       'driver_name': '',
       'ctime': 1696224180,
       'description': 'Đơn hàng đã được giao thành công',
       'type': 0},
      'is_multi_parcel': False,
      'num_parcels': 1,
      'parcel_no': 1},
     'info_card': {'order_id': 149752100291872,
      'order_list_cards': [{'shop_info': {'shop_id': 48311894,
         'shop_name': 'Bra & Knickers',
         'user_id': 48313282,
         'username': 'anannshop',
         'portrait': 'd664c852e1100082b09a13d09457d93d',
         'shop_tag': 3},
        'order_id': 149752100291872,
        'product_info': {'item_groups': [{'items': [{'item_id': 1602031702,
             'model_id': 9613089074,
             'shop_id': 48311894,
             'name': 'Khăng Choàng Cổ Dạ Len Quàng Nam Nữ Cao Cấp Nhiều Màu Cashmere Hàng Đẹp Giá Rẻ',
             'model_name': '8 - da sáng',
             'image': '7e3e7ed202c224dae7641bab1ab0eefd',
             'amount': 1,
             'ext_info': {'add_on_deal_id': 0,
              'is_add_on_sub_item': False,
              'free_return_day': 0,
              'is_wholesale': False,
              'is_pre_order': False,
              'is_membership_gift': False,
              'is_free_return': False},
             'status': 1,
             'item_price': 2890000000,
             'price_before_discount': 6500000000,
             'order_price': 2890000000,
             'snapshot_id': 16436071430}],
           'num_items': 1}],
         'total_num_items': 1}}],
      'product_count': 1,
      'subtotal': 1445000000,
      'final_total': 1445000000},
     'primary_buttons': [{'id': 24}],
     'guarantee': {'learn_more_url': 'https://shopee.vn/m/shopee-dam-bao',
      'is_extend_enabled': False},
     'secondary_buttons': [{'id': 15}],
     'list_type': 3},
     ...
 }
}
```

2. Thực hiện trích xuất thông tin từ đoạn json thu được

```python
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
```

{{% notice note %}}
Thi thoảng code sẽ bị lỗi do shopee thay đổi cấu trúc của file json trả về. Khi gặp lỗi chỉ cần xóa cái key-value đó đi là được. Thông thường sẽ không có thay đổi nhiều.
{{% /notice %}}




