# coding=utf-8

def loc_cluster(loc):

    loc = '台'.join(loc.split('臺'))
    loc_list = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '新竹市', '嘉義市', '新竹縣',
                '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '台東縣', '澎湖縣']

    if loc not in loc_list:
        loc = '其他地區'

    return loc
