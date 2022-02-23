"""
    Tag: hashmap

    The people who buy ads on our network don't have enough data about how ads are working for their business. 
    They've asked us to find out which ads produce the most purchases on their website.

    Our client provided us with a list of user IDs of customers who bought something on a landing page after 
    clicking one of their ads:

    # Each user completed 1 purchase.
    completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]

    And our ops team provided us with some raw log data from our ad server showing every time a user clicked on 
    one of our ads:

    ad_clicks = [
        #"IP_Address,Time,Ad_Text",
        "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
        "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
        "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
        "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
        "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
        "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
        "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
    ]

    The client also sent over the IP addresses of all their users.

    all_user_ips = [
        #"User_ID,IP_Address",
        "2339985511,122.121.0.155",
        "234111110,122.121.0.1",
        "3123122444,92.130.6.145",
        "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
        "8321125440,82.1.106.8",
        "99911063,92.130.6.144"
    ]

    Write a function to parse this data, determine how many times each ad was clicked, then return the ad text, 
    that ad's number of clicks, and how many of those ad clicks were from users who made a purchase.

    Expected output:
    1 of 2     2017 Pet Mittens
    0 of 1     The Best Hollywood Coats
    3 of 4     Buy wool coats for your pets

    purchases: number of purchase IDs
    clicks: number of ad clicks
    ips: number of IP addresses


    ad_2_ip = {'ad': [ip1, ip2]}
    ip_2_userid = {'ip': user_id}
    completed_purchase_user_ids = {"3123122444","234111110", "8321125440", "99911063"}

    {
        ad1: (1, 2)
    }
"""

def get_click_to_buy_ratio(all_user_ips, ad_clicks, completed_purchase_user_ids):
    
    completed_purchase_user_id_set = set(completed_purchase_user_ids)
    ip_2_user_id = {x.split(',')[1]: x.split(',')[0] for x in all_user_ips}

    ad_2_user_ids = {}
    for ad_click in ad_clicks:
        _a = ad_click.split(',')
        user_id_list = ad_2_user_ids.get(_a[2], list())
        user_id_list.append(ip_2_user_id.get(_a[0], None))

        ad_2_user_ids[_a[2]] = user_id_list
    
    ad_click_2_purchase_ratio = {}
    for ad, users in ad_2_user_ids.items():
        ad_purchases = 0
        for user in users:
            if user in completed_purchase_user_id_set:
                ad_purchases += 1

        ad_click_2_purchase_ratio[ad] = (ad_purchases, len(users))

    return ad_click_2_purchase_ratio


all_user_ips = [
    #"User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


ad_clicks = [
    #"IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

completed_purchase_user_ids = ["3123122444", "234111110", "8321125440", "99911063"]

assert(
    get_click_to_buy_ratio(all_user_ips, ad_clicks, completed_purchase_user_ids) == {
        'Buy wool coats for your pets': (3, 4), 
        '2017 Pet Mittens': (1, 2), 
        'The Best Hollywood Coats': (0, 1)
    }
)
print('Tests Passed!')