#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据处理管道 — 从公开数据源采集、清洗、聚合，生成大屏可视化数据

数据来源（2025年权威公开数据）:
  - 数字经济: 国家统计局、国家数据局、中国信通院《中国数字经济发展报告(2025)》
  - 新能源:   国家能源局《2025年电力统计数据》(2026.01.30 发布)
  - AI人才:   智联招聘《2025年人工智能产业人才发展报告》(2025.10.24 发布)

运行方式:
  python data_pipeline.py          # 生成 static_data/*.json
  python data_pipeline.py --all    # 同时更新 data.py 中的 SourceDataDemo

ETL 流程:
  公开报告/API → 抽取(Extract) → 清洗转换(Transform) → 输出JSON(Load) → Flask 可视化
"""

import json
import os
import sys
from typing import Optional

# ============================================================
# 第一阶段: 数据抽取 (Extract)
# 从公开报告中提取原始数据点，每条标注出处
# 生产环境中可替换为 API 调用或数据库读取
# ============================================================

class DigitalEconomyExtractor:
    """数字经济数据抽取 — 国家统计局、国家数据局、中国信通院"""

    @staticmethod
    def extract():
        return {
            # 国家数据局: 2025年数字经济增加值总量约49万亿，核心产业14.7万亿
            "core_industry_value": 14.7,        # 核心产业增加值(万亿元)
            "gdp_share": 35.0,                  # 占GDP比重(%)
            # 国家统计局2024年分类数据 (2025年分类数据暂未发布，使用2024年数据)
            "industry_breakdown": {
                "数字技术应用业": 61928,  # 亿元 (44.0%)
                "数字产品制造业": 48145,  # 亿元 (34.2%)
                "数字要素驱动业": 26519,  # 亿元 (18.8%)
                "数字产品服务业": 4298,   # 亿元 (3.1%)
            },
            # 中国信通院: 各省数字经济规模估算(万亿元)
            "province_scale": {
                "广东": 6.83, "江苏": 5.72, "浙江": 4.18, "山东": 3.95,
                "北京": 3.22, "上海": 2.85, "福建": 2.68, "四川": 2.45,
                "湖北": 2.30, "河南": 2.15, "湖南": 1.95, "安徽": 1.80,
                "河北": 1.68, "重庆": 1.55, "陕西": 1.35, "江西": 1.20,
                "辽宁": 1.05, "天津": 1.08, "广西": 0.92, "贵州": 0.85,
                "云南": 0.78, "山西": 0.72, "黑龙江": 0.65, "吉林": 0.58,
                "内蒙古": 0.52, "新疆": 0.48, "甘肃": 0.42, "海南": 0.32,
                "宁夏": 0.22, "青海": 0.15, "西藏": 0.08,
            },
            # 国家统计局第五次经济普查: 三产数字经济渗透率
            "penetration_by_industry": {
                "第三产业": 45.63, "第二产业": 25.03, "第一产业": 10.78,
            },
            # 工信部2024年: 软件业14.2万亿, 电子信息制造业16.3万亿, 互联网3.5万亿, 通信业1.7万亿
            "digital_sector_revenue": {
                "软件和信息技术服务": 14.2,
                "电子信息制造业": 16.3,
                "互联网和相关服务": 3.5,
                "通信业": 1.7,
            },
            # 各行业公开数据: 网上零售额15.52万亿(2024), 云计算/大数据6800亿, AI 5200亿等
            "key_sectors": {
                "电子商务": 15.52, "云计算/大数据": 6.80,
                "人工智能": 5.20, "工业互联网": 4.35,
                "区块链": 0.85, "其他": 2.10,
            },
            # 2020-2025 国家统计局数据
            "yearly_trend": {
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "core_value": [8.1, 9.6, 10.8, 12.8, 14.1, 14.7],     # 万亿元
                "gdp_ratio": [7.8, 8.3, 9.2, 9.9, 10.5, 10.5],         # %
            },
            # 赛迪《2025中国城市数字经济百强》
            "city_ranking": {
                "北京": 92.5, "上海": 90.8, "深圳": 89.5, "广州": 86.2,
                "杭州": 84.8, "成都": 78.2, "南京": 76.5, "武汉": 72.8,
            },
            # 各城市数字经济占GDP比重(%)
            "city_gdp_share": {
                "北京": 42.5, "上海": 38.8, "深圳": 36.2, "杭州": 31.5, "广州": 28.8,
            },
        }


class NewEnergyExtractor:
    """新能源数据抽取 — 国家能源局 (2026.01.30 发布会)"""

    @staticmethod
    def extract():
        return {
            # 可再生能源总装机23.4亿千瓦, 发电量4.0万亿千瓦时
            "total_capacity": 23.4,  # 亿千瓦
            "total_generation": 4.0,  # 万亿千瓦时
            "capacity_breakdown": {
                "太阳能发电": 12.0,   # 亿千瓦 (1200GW), 同比+35.4%
                "风力发电": 6.4,      # 亿千瓦 (640GW), 同比+22.9%
                "水力发电": 4.36,     # 亿千瓦
                "生物质发电": 0.60,   # 亿千瓦
            },
            # 2025年新增: 光伏3.17亿千瓦, 风电1.19亿千瓦, 储能约58GW
            "new_additions": {
                "光伏新增": 317,  # GW = 3.17亿千瓦
                "风电新增": 119,  # GW = 1.19亿千瓦
                "储能新增": 58,   # GW
            },
            # 陆上风电5.74亿千瓦, 海上风电0.66亿千瓦
            "wind_structure": {
                "陆上风电": 57400,  # 万千瓦
                "海上风电": 6600,   # 万千瓦
            },
            # 新型储能: 累计1.36亿千瓦, 同比+84%, 锂离子电池占92%
            "storage_structure": {
                "锂离子电池": 92, "压缩空气": 3, "液流电池": 2, "飞轮/其他": 3,
            },
            # 光伏装机TOP8省份(万千瓦)
            "province_pv_top": {
                "山东": 7850, "河北": 6820, "江苏": 5920, "浙江": 5180,
                "河南": 4850, "安徽": 4320, "广东": 3980, "内蒙古": 3650,
            },
            # 月度光伏新增(万千瓦) 2025年
            "monthly_pv": {
                "months": ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"],
                "光伏": [1850,1620,2150,2480,2850,3200,3580,3820,3120,2680,2250,2010],
                "风电": [820,650,920,1050,1180,1320,1480,1250,980,880,750,910],
            },
            # 海上风电装机TOP8城市(万千瓦)
            "offshore_wind_city": {
                "南通": 1250, "盐城": 1180, "阳江": 1050, "大连": 920,
                "汕头": 780, "福州": 680, "唐山": 550, "宁波": 480,
            },
            # 光伏组件出货量市占率(%) - CPIA中国光伏行业协会
            "pv_market_share": {
                "隆基绿能": 22, "晶科能源": 18, "天合光能": 15,
                "晶澳科技": 12, "通威股份": 8,
            },
            # 各省可再生能源总装机(万千瓦)
            "province_capacity": {
                "山东": 16800, "内蒙古": 15800, "河北": 14500, "江苏": 13200,
                "广东": 11200, "浙江": 10800, "新疆": 10500, "河南": 9500,
                "山西": 8800, "甘肃": 8200, "青海": 7800, "陕西": 7200,
                "宁夏": 6500, "云南": 6200, "安徽": 5800, "四川": 5500,
                "辽宁": 5200, "福建": 4800, "湖北": 4500, "贵州": 4200,
                "湖南": 3800, "江西": 3500, "吉林": 3200, "广西": 3100,
                "黑龙江": 2800, "重庆": 2200, "上海": 1800, "天津": 1600,
                "北京": 1500, "海南": 1200, "西藏": 980,
            },
        }


class AITalentExtractor:
    """AI人才数据抽取 — 智联招聘《2025年人工智能产业人才发展报告》"""

    @staticmethod
    def extract():
        return {
            "total_positions": 486720,       # 前三季度AI岗位招聘总数
            "avg_salary_ai_engineer": 21439,  # AI工程师平均月薪(元)
            "hot_positions": {
                "算法工程师": 35, "AI产品经理": 22, "数据分析师": 18,
                "计算机视觉": 12, "数据标注/AI训练": 8, "NLP工程师": 5,
            },
            "company_size": {
                "20-99人": 41, "100-299人": 31, "20人以下": 13,
                "300-999人": 9, "1000人以上": 6,
            },
            "education_requirement": {
                "本科": 56, "硕士": 25, "博士": 9, "大专及以下": 10,
            },
            "experience_requirement": {
                "1-3年": 28, "3-5年": 35, "5-10年": 22,
                "应届/不限": 10, "10年以上": 5,
            },
            "competition_index": {
                "AI产品经理": 68, "算法工程师": 47, "数据分析师": 38,
                "NLP工程师": 42, "CV工程师": 35, "AI训练师": 43,
            },
            "salary_by_education": {
                "labels": ["大专", "本科", "硕士(普)", "硕士(985/211)", "博士", "博士(C9)"],
                "average": [8500, 15800, 19500, 26800, 35200, 52000],
                "position_ratio": [10, 56, 25, 9, 3, 1],
            },
            "city_salary_top": {
                "上海": 26876, "北京": 25600, "杭州": 23800, "深圳": 22500,
                "广州": 19200, "成都": 16800, "南京": 17500, "武汉": 15200,
            },
            "city_demand_share": {
                "北京": 18.6, "深圳": 9.0, "上海": 8.5, "杭州": 6.5, "广州": 5.2,
            },
            "city_positions": {
                "北京": 90500, "上海": 68200, "深圳": 43800, "杭州": 29500,
                "广州": 24800, "成都": 18500, "西安": 15200, "武汉": 13500,
                "南京": 12800, "苏州": 10500, "合肥": 8500, "重庆": 7800,
                "长沙": 7200, "天津": 6500, "郑州": 5500, "济南": 4800,
                "青岛": 3800, "厦门": 3200, "福州": 2800, "大连": 2500,
                "沈阳": 2200, "昆明": 2000, "哈尔滨": 1800, "南昌": 1800,
                "贵阳": 1500, "石家庄": 1500, "南宁": 1200, "太原": 1000,
                "海口": 800, "兰州": 700,
            },
        }


# ============================================================
# 第二阶段: 数据转换 (Transform)
# 将原始数据点转换为 ECharts 图表所需的格式
# ============================================================

class ChartDataTransformer:
    """通用图表数据转换器"""

    @staticmethod
    def to_bar_data(title: str, data_dict: dict) -> dict:
        """{name: value} → 柱状图 {title, data: [{name, value}]}"""
        return {
            "title": title,
            "data": [{"name": k, "value": v} for k, v in data_dict.items()]
        }

    @staticmethod
    def to_pie_data(title: str, data_dict: dict) -> dict:
        """{name: value} → 饼图 {title, data: [{name, value}]}"""
        return {
            "title": title,
            "data": [{"name": k, "value": v} for k, v in data_dict.items()]
        }

    @staticmethod
    def to_line_data(title: str, names: list, x_axis: list, values: list) -> dict:
        """→ 折线图 {title, data: [{name, value:[]}], xAxis}"""
        return {
            "title": title,
            "data": [{"name": n, "value": v} for n, v in zip(names, values)],
            "xAxis": x_axis,
        }

    @staticmethod
    def to_ring_data(title: str, data_dict: dict) -> list:
        """{name: percent} → 环形图 [{name, value, value2, color, radius}]"""
        colors = ["01", "02", "03", "04", "05"]
        radii = [
            ['59%', '70%'], ['49%', '60%'], ['39%', '50%'], ['29%', '40%'], ['20%', '30%']
        ]
        items = list(data_dict.items())
        return [
            {
                "name": items[i][0],
                "value": items[i][1],
                "value2": 100 - items[i][1],
                "color": colors[i],
                "radius": radii[i],
            }
            for i in range(min(len(items), 5))
        ]

    @staticmethod
    def to_map_data(data_dict: dict, symbol_size: int = 30) -> list:
        """{name: value} → 地图散点 [{name, value}]"""
        return [{"name": k, "value": v} for k, v in data_dict.items()]


# ============================================================
# 第三阶段: 数据组装 (Assemble)
# 将转换后的数据组装为最终的大屏数据格式
# ============================================================

def build_digital_economy_data() -> dict:
    """组装数字经济大屏数据 → 写入 data.py 的 SourceDataDemo"""
    raw = DigitalEconomyExtractor.extract()
    T = ChartDataTransformer

    # 组装为 SourceDataDemo 所需格式（仅返回数据部分，不包含 @property 方法）
    lines = []
    lines.append("# 以下数据由 data_pipeline.py 自动生成")
    lines.append(f"# 数据来源: 国家统计局、国家数据局、中国信通院")
    lines.append(f"# 生成时间: 请查看 git log")
    lines.append("")
    lines.append(f"self.title = '2025年中国数字经济数据可视化大屏'")
    lines.append(f"self.counter = {{'name': '数字经济核心产业增加值(万亿元)', 'value': {int(raw['core_industry_value'] * 1000)}}}  # {raw['core_industry_value']}万亿")
    lines.append(f"self.counter2 = {{'name': '数字经济占GDP比重(%)', 'value': {int(raw['gdp_share'])}}}")

    # echart1: 核心产业构成
    data = T.to_bar_data("核心产业构成(亿元)", raw["industry_breakdown"])
    lines.append(f"self.echart1_data = {json.dumps(data, ensure_ascii=False)}")

    # echart2: 省份规模TOP7
    items = sorted(raw["province_scale"].items(), key=lambda x: x[1], reverse=True)[:7]
    data = T.to_bar_data("数字经济规模TOP7省份(万亿元)", {
        k: int(v * 100) for k, v in items
    })
    lines.append(f"self.echart2_data = {json.dumps(data, ensure_ascii=False)}")

    # echarts3_1: 产业渗透率
    data = T.to_pie_data("产业数字化渗透率(%)", {
        k: int(v * 100) for k, v in raw["penetration_by_industry"].items()
    })
    lines.append(f"self.echarts3_1_data = {json.dumps(data, ensure_ascii=False)}")

    # echarts3_2: 数字产业收入构成
    data = T.to_pie_data("数字产业收入构成(万亿元)", {
        k: int(v * 10) for k, v in raw["digital_sector_revenue"].items()
    })
    lines.append(f"self.echarts3_2_data = {json.dumps(data, ensure_ascii=False)}")

    # echarts3_3: 重点领域
    data = T.to_pie_data("重点领域规模(万亿元)", {
        k: int(v * 100) for k, v in raw["key_sectors"].items()
    })
    lines.append(f"self.echarts3_3_data = {json.dumps(data, ensure_ascii=False)}")

    # echart4: 年度趋势
    trend = raw["yearly_trend"]
    data = T.to_line_data(
        "核心产业增加值年度趋势(万亿元)",
        ["核心产业增加值", "占GDP比重(%)"],
        [str(y) for y in trend["years"]],
        [trend["core_value"], trend["gdp_ratio"]],
    )
    lines.append(f"self.echart4_data = {json.dumps(data, ensure_ascii=False)}")

    # echart5: 城市排名
    data = T.to_bar_data("城市数字经济百强TOP8", {
        k: int(v * 10) for k, v in raw["city_ranking"].items()
    })
    lines.append(f"self.echart5_data = {json.dumps(data, ensure_ascii=False)}")

    # echart6: 城市GDP占比(环形图)
    ring_data = T.to_ring_data("重点城市数字经济占GDP比重(%)", {
        k: int(v * 10) for k, v in raw["city_gdp_share"].items()
    })
    data = {
        "title": "重点城市数字经济占GDP比重(%)",
        "data": ring_data,
    }
    lines.append(f"self.echart6_data = {json.dumps(data, ensure_ascii=False)}")

    # map_1: 各省数字经济规模
    data = {
        "symbolSize": 30,
        "data": T.to_map_data({
            k: int(v * 100) for k, v in raw["province_scale"].items()
        }),
    }
    lines.append(f"self.map_1_data = {json.dumps(data, ensure_ascii=False)}")

    return lines


def build_new_energy_data() -> dict:
    """组装新能源大屏数据 → 输出到 static_data/corp.json"""
    raw = NewEnergyExtractor.extract()
    T = ChartDataTransformer

    return {
        "title": "2025年中国新能源产业数据大屏",
        "counter": {
            "name": "可再生能源总装机(亿千瓦)",
            "value": int(raw["total_capacity"] * 10),
        },
        "counter2": {
            "name": "可再生能源发电量(万亿千瓦时)",
            "value": int(raw["total_generation"] * 10),
        },
        "echart1_data": T.to_bar_data("可再生能源装机分布(亿千瓦)", {
            k: int(v * 100) for k, v in raw["capacity_breakdown"].items()
        }),
        "echart2_data": T.to_bar_data("光伏装机TOP8省份(万千瓦)", raw["province_pv_top"]),
        "echarts3_1_data": T.to_pie_data("2025年新增装机(GW)", raw["new_additions"]),
        "echarts3_2_data": T.to_pie_data("风电装机结构(万千瓦)", raw["wind_structure"]),
        "echarts3_3_data": T.to_pie_data("新型储能装机结构", raw["storage_structure"]),
        "echart4_data": T.to_line_data(
            "2025年月度光伏新增装机(万千瓦)",
            ["光伏", "风电"],
            raw["monthly_pv"]["months"],
            [raw["monthly_pv"]["光伏"], raw["monthly_pv"]["风电"]],
        ),
        "echart5_data": T.to_bar_data(
            "海上风电装机城市TOP8(万千瓦)", raw["offshore_wind_city"]
        ),
        "echart6_data": {
            "title": "光伏组件出货量市占率(%)",
            "data": T.to_ring_data("", raw["pv_market_share"]),
        },
        "map_1_data": {
            "symbolSize": 20000,
            "data": T.to_map_data(raw["province_capacity"]),
        },
    }


def build_ai_talent_data() -> dict:
    """组装AI人才大屏数据 → 输出到 static_data/job.json"""
    raw = AITalentExtractor.extract()
    T = ChartDataTransformer

    return {
        "title": "2025年人工智能人才市场数据大屏",
        "counter": {
            "name": "AI岗位招聘总数(前三季度)",
            "value": raw["total_positions"],
        },
        "counter2": {
            "name": "AI工程师平均月薪(元)",
            "value": raw["avg_salary_ai_engineer"],
        },
        "echart1_data": T.to_pie_data("热门AI岗位招聘占比(%)", raw["hot_positions"]),
        "echart2_data": T.to_pie_data("招聘企业规模分布(%)", raw["company_size"]),
        "echarts3_1_data": T.to_pie_data(
            "AI工程师学历要求(%)", raw["education_requirement"]
        ),
        "echarts3_2_data": T.to_pie_data(
            "AI工程师经验要求占比(%)", raw["experience_requirement"]
        ),
        "echarts3_3_data": T.to_pie_data(
            "岗位竞争指数(投递/职位)", raw["competition_index"]
        ),
        "echart4_data": T.to_line_data(
            "AI工程师薪资与学历(元/月)",
            ["平均月薪", "岗位数量占比(%)"],
            raw["salary_by_education"]["labels"],
            [
                raw["salary_by_education"]["average"],
                raw["salary_by_education"]["position_ratio"],
            ],
        ),
        "echart5_data": T.to_bar_data(
            "AI工程师城市薪资TOP8(元/月)", raw["city_salary_top"]
        ),
        "echart6_data": {
            "title": "AI工程师城市需求占比(%)",
            "data": T.to_ring_data("", {
                k: int(v * 10) for k, v in raw["city_demand_share"].items()
            }),
        },
        "map_1_data": {
            "symbolSize": 2000,
            "data": T.to_map_data(raw["city_positions"]),
        },
    }


# ============================================================
# 第四阶段: 输出 (Load)
# 生成 JSON 文件和 Python 数据类代码
# ============================================================

def export_json(data: dict, filepath: str):
    """输出JSON文件"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    size_kb = os.path.getsize(filepath) / 1024
    print(f"  [OK] {filepath} ({size_kb:.1f} KB)")


def update_data_py(lines: list):
    """将生成的数据代码写入 data.py 的 SourceDataDemo.__init__ 方法"""
    data_py_path = os.path.join(os.path.dirname(__file__), 'data.py')
    with open(data_py_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找到 SourceDataDemo.__init__ 方法的起止位置
    start_marker = "class SourceDataDemo:\n\n    def __init__(self):"
    end_marker = "\n    @property\n    def echart1(self):"

    assert start_marker in content, f"未找到 {start_marker}"
    assert end_marker in content, f"未找到 {end_marker}"

    start_idx = content.index(start_marker) + len(start_marker)
    end_idx = content.index(end_marker)

    new_body = "\n" + "\n".join(f"        {line}" for line in lines) + "\n    "
    new_content = content[:start_idx] + new_body + content[end_idx:]

    with open(data_py_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  [OK] {data_py_path} (SourceDataDemo 已更新)")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static_data")

    print("=" * 60)
    print("  Data Pipeline: Public Data -> Visualization")
    print("=" * 60)

    # 1. 生成新能源 JSON
    print("\n[1/3] new energy data...")
    corp_data = build_new_energy_data()
    export_json(corp_data, os.path.join(static_dir, "corp.json"))

    # 2. 生成AI人才 JSON
    print("\n[2/3] AI talent data...")
    job_data = build_ai_talent_data()
    export_json(job_data, os.path.join(static_dir, "job.json"))

    # 3. 更新 data.py
    if "--all" in sys.argv:
        print("\n[3/3] update data.py SourceDataDemo...")
        digital_lines = build_digital_economy_data()
        update_data_py(digital_lines)
    else:
        print("\n[3/3] Skip data.py update (use --all flag to sync)")

    print("\n" + "=" * 60)
    print("  Pipeline done. Run: python app.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
