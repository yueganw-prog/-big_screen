#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Describe: 2025年中国数字经济数据可视化大屏 - 数据模型定义

import json


class SourceDataDemo:

    def __init__(self):
        self.title = '2025年中国数字经济数据可视化大屏'
        self.counter = {'name': '2025年平台GMV总额(万元)', 'value': 47562380}
        self.counter2 = {'name': '2025年活跃用户数(人)', 'value': 8926410}
        self.echart1_data = {
            'title': '行业分布',
            'data': [
                {"name": "人工智能", "value": 135},
                {"name": "新能源", "value": 118},
                {"name": "直播电商", "value": 142},
                {"name": "半导体", "value": 96},
                {"name": "生物医药", "value": 78},
                {"name": "智能制造", "value": 105},
                {"name": "低空经济", "value": 58},
            ]
        }
        self.echart2_data = {
            'title': '省份分布',
            'data': [
                {"name": "广东", "value": 215},
                {"name": "浙江", "value": 178},
                {"name": "江苏", "value": 165},
                {"name": "北京", "value": 142},
                {"name": "上海", "value": 138},
                {"name": "四川", "value": 95},
                {"name": "湖北", "value": 82},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "18-24岁", "value": 68},
                {"name": "25-34岁", "value": 142},
                {"name": "35-44岁", "value": 110},
                {"name": "45-54岁", "value": 55},
                {"name": "55岁以上", "value": 28},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "AI/算法工程师", "value": 35},
                {"name": "新媒体运营", "value": 42},
                {"name": "跨境电商", "value": 38},
                {"name": "软件开发", "value": 30},
                {"name": "金融科技", "value": 25},
                {"name": "其他", "value": 33},
            ]
        }
        self.echarts3_3_data = {
            'title': '消费偏好',
            'data': [
                {"name": "数码3C", "value": 28},
                {"name": "国潮品牌", "value": 22},
                {"name": "户外运动", "value": 19},
                {"name": "知识付费", "value": 15},
                {"name": "健康养生", "value": 18},
                {"name": "其他", "value": 11},
            ]
        }
        self.echart4_data = {
            'title': '24小时活跃趋势',
            'data': [
                {"name": "工作日", "value": [5, 3, 2, 1, 1, 2, 6, 15, 22, 28, 25, 23, 20, 22, 26, 30, 28, 32, 35, 28, 22, 15, 8]},
                {"name": "节假日", "value": [3, 2, 1, 1, 1, 3, 8, 18, 25, 30, 28, 26, 22, 24, 28, 32, 30, 34, 38, 30, 25, 18, 10]},
            ],
            'xAxis': ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                      '17', '18', '19', '20', '21', '22', '23'],
        }
        self.echart5_data = {
            'title': '城市数字经济指数TOP8',
            'data': [
                {"name": "深圳", "value": 95},
                {"name": "杭州", "value": 88},
                {"name": "北京", "value": 92},
                {"name": "上海", "value": 85},
                {"name": "广州", "value": 78},
                {"name": "成都", "value": 72},
                {"name": "苏州", "value": 68},
                {"name": "武汉", "value": 63},
            ]
        }
        self.echart6_data = {
            'title': '重点城市渗透率',
            'data': [
                {"name": "深圳", "value": 92, "value2": 8, "color": "01", "radius": ['59%', '70%']},
                {"name": "上海", "value": 85, "value2": 15, "color": "02", "radius": ['49%', '60%']},
                {"name": "杭州", "value": 78, "value2": 22, "color": "03", "radius": ['39%', '50%']},
                {"name": "北京", "value": 72, "value2": 28, "color": "04", "radius": ['29%', '40%']},
                {"name": "广州", "value": 65, "value2": 35, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '北京', 'value': 880},
                {'name': '上海', 'value': 920},
                {'name': '广州', 'value': 760},
                {'name': '深圳', 'value': 950},
                {'name': '成都', 'value': 720},
                {'name': '重庆', 'value': 680},
                {'name': '杭州', 'value': 890},
                {'name': '武汉', 'value': 650},
                {'name': '南京', 'value': 600},
                {'name': '天津', 'value': 520},
                {'name': '西安', 'value': 580},
                {'name': '郑州', 'value': 540},
                {'name': '长沙', 'value': 510},
                {'name': '青岛', 'value': 460},
                {'name': '沈阳', 'value': 420},
                {'name': '大连', 'value': 380},
                {'name': '济南', 'value': 440},
                {'name': '哈尔滨', 'value': 350},
                {'name': '福州', 'value': 430},
                {'name': '厦门', 'value': 480},
                {'name': '昆明', 'value': 390},
                {'name': '合肥', 'value': 500},
                {'name': '南昌', 'value': 370},
                {'name': '石家庄', 'value': 360},
                {'name': '太原', 'value': 340},
                {'name': '南宁', 'value': 330},
                {'name': '长春', 'value': 310},
                {'name': '温州', 'value': 350},
                {'name': '宁波', 'value': 420},
                {'name': '苏州', 'value': 560},
                {'name': '无锡', 'value': 480},
                {'name': '贵阳', 'value': 320},
                {'name': '珠海', 'value': 380},
                {'name': '兰州', 'value': 260},
                {'name': '洛阳', 'value': 280},
                {'name': '海口', 'value': 290},
                {'name': '乌鲁木齐', 'value': 300},
                {'name': '扬州', 'value': 280},
                {'name': '南通', 'value': 310},
                {'name': '烟台', 'value': 290},
                {'name': '海门', 'value': 200},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        sym = data.get('symbolSize')
        if sym is None or (isinstance(sym, (int, float)) and not (sym > 0)):
            sym = 100
        echart = {
            'symbolSize': sym,
            'data': data.get('data'),
        }
        return echart

    def to_dict(self):
        """
        将数据对象转换为字典格式，用于 JSON 序列化
        """
        return {
            'title': self.title,
            'counter': self.counter,
            'counter2': self.counter2,
            'echart1': self.echart1,
            'echart2': self.echart2,
            'echarts3_1': self.echarts3_1,
            'echarts3_2': self.echarts3_2,
            'echarts3_3': self.echarts3_3,
            'echart4': self.echart4,
            'echart5': self.echart5,
            'echart6': self.echart6,
            'map_1': self.map_1,
        }


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '2025年中国数字经济数据可视化大屏'


class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('static_data/corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('static_data/job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')