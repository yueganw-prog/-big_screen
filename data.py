#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Describe: 2025年中国数字经济数据可视化大屏 - 数据模型定义

import json


class SourceDataDemo:

    def __init__(self):
        self.title = '2025年中国数字经济数据可视化大屏'
        # 国家数据局: 2025年数字经济增加值49万亿; 核心产业增加值14.7万亿, 占GDP 35%
        self.counter = {'name': '数字经济核心产业增加值(万亿元)', 'value': 147000}  # 14.7万亿
        self.counter2 = {'name': '数字经济占GDP比重(%)', 'value': 35}
        # 国家统计局: 2024年数字经济核心产业内部构成
        self.echart1_data = {
            'title': '核心产业构成(亿元)',
            'data': [
                {"name": "数字技术应用业", "value": 61928},
                {"name": "数字产品制造业", "value": 48145},
                {"name": "数字要素驱动业", "value": 26519},
                {"name": "数字产品服务业", "value": 4298},
            ]
        }
        # 中国信通院: 各省数字经济规模排名
        self.echart2_data = {
            'title': '数字经济规模TOP7省份(万亿元)',
            'data': [
                {"name": "广东", "value": 683},
                {"name": "江苏", "value": 572},
                {"name": "浙江", "value": 418},
                {"name": "山东", "value": 395},
                {"name": "北京", "value": 322},
                {"name": "上海", "value": 285},
                {"name": "福建", "value": 268},
            ]
        }
        # 国家统计局: 三次产业数字经济渗透率
        self.echarts3_1_data = {
            'title': '产业数字化渗透率(%)',
            'data': [
                {"name": "第三产业", "value": 4563},
                {"name": "第二产业", "value": 2503},
                {"name": "第一产业", "value": 1078},
            ]
        }
        # 2024年电子信息制造业 vs 软件业 vs 互联网
        self.echarts3_2_data = {
            'title': '数字产业收入构成(万亿元)',
            'data': [
                {"name": "软件和信息技术服务", "value": 142},
                {"name": "电子信息制造业", "value": 163},
                {"name": "互联网和相关服务", "value": 35},
                {"name": "通信业", "value": 17},
            ]
        }
        # 数字经济重点领域 2025
        self.echarts3_3_data = {
            'title': '重点领域规模(万亿元)',
            'data': [
                {"name": "电子商务", "value": 1552},
                {"name": "云计算/大数据", "value": 680},
                {"name": "人工智能", "value": 520},
                {"name": "工业互联网", "value": 435},
                {"name": "区块链", "value": 85},
                {"name": "其他", "value": 210},
            ]
        }
        # 数字经济核心产业增加值年增长 2020-2025
        self.echart4_data = {
            'title': '核心产业增加值年度趋势(万亿元)',
            'data': [
                {"name": "核心产业增加值", "value": [81, 96, 108, 128, 141, 147]},
                {"name": "占GDP比重(%)", "value": [78, 83, 92, 99, 105, 105]},
            ],
            'xAxis': ['2020', '2021', '2022', '2023', '2024', '2025'],
        }
        # 赛迪: 2025中国城市数字经济百强
        self.echart5_data = {
            'title': '城市数字经济百强TOP8',
            'data': [
                {"name": "北京", "value": 925},
                {"name": "上海", "value": 908},
                {"name": "深圳", "value": 895},
                {"name": "广州", "value": 862},
                {"name": "杭州", "value": 848},
                {"name": "成都", "value": 782},
                {"name": "南京", "value": 765},
                {"name": "武汉", "value": 728},
            ]
        }
        # 重点城市数字经济占GDP比重
        self.echart6_data = {
            'title': '重点城市数字经济占GDP比重(%)',
            'data': [
                {"name": "北京", "value": 425, "value2": 575, "color": "01", "radius": ['59%', '70%']},
                {"name": "上海", "value": 388, "value2": 612, "color": "02", "radius": ['49%', '60%']},
                {"name": "深圳", "value": 362, "value2": 638, "color": "03", "radius": ['39%', '50%']},
                {"name": "杭州", "value": 315, "value2": 685, "color": "04", "radius": ['29%', '40%']},
                {"name": "广州", "value": 288, "value2": 712, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        # 各省数字经济规模 (十亿元)
        self.map_1_data = {
            'symbolSize': 30,
            'data': [
                {'name': '广东', 'value': 683}, {'name': '江苏', 'value': 572}, {'name': '浙江', 'value': 418},
                {'name': '山东', 'value': 395}, {'name': '北京', 'value': 322}, {'name': '上海', 'value': 285},
                {'name': '福建', 'value': 268}, {'name': '四川', 'value': 245}, {'name': '湖北', 'value': 230},
                {'name': '河南', 'value': 215}, {'name': '湖南', 'value': 195}, {'name': '安徽', 'value': 180},
                {'name': '重庆', 'value': 155}, {'name': '河北', 'value': 168}, {'name': '陕西', 'value': 135},
                {'name': '江西', 'value': 120}, {'name': '天津', 'value': 108}, {'name': '贵州', 'value': 85},
                {'name': '广西', 'value': 92}, {'name': '辽宁', 'value': 105}, {'name': '云南', 'value': 78},
                {'name': '山西', 'value': 72}, {'name': '黑龙江', 'value': 65}, {'name': '吉林', 'value': 58},
                {'name': '甘肃', 'value': 42}, {'name': '内蒙古', 'value': 52}, {'name': '新疆', 'value': 48},
                {'name': '海南', 'value': 32}, {'name': '宁夏', 'value': 22}, {'name': '青海', 'value': 15},
                {'name': '西藏', 'value': 8},
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