# 2025年中国数字经济数据可视化大屏

基于 Flask + ECharts 构建的数据大屏可视化项目，涵盖数字经济、新能源产业、人工智能人才三大主题。

## 功能特性

- **三大数据主题**：数字经济、新能源产业、AI人才市场
- **8 种图表类型**：柱状图、折线图、饼图、环形图、中国地图散点图
- **实时数据模拟**：API 每 3 秒自动刷新，数字滚动动画效果
- **响应式布局**：rem 自适应，适配 1920×1080 及以上分辨率
- **纯前端渲染**：ECharts 可视化，深色科技风主题

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Python Flask |
| 数据可视化 | ECharts 5 |
| 前端 | jQuery + HTML5 + CSS3 |
| 地图 | ECharts 中国地图 |

## 快速开始

```bash
# 安装依赖
pip install flask

# 启动服务
python app.py
```

## 数据来源

| 页面 | 数据来源 | 数据年份 |
|------|----------|----------|
| 数字经济大屏 | 国家统计局、国家数据局、中国信通院 | 2020–2025 |
| 新能源产业大屏 | 国家能源局《2025年电力统计数据》 | 2025 |
| AI人才市场大屏 | 智联招聘《2025年人工智能产业人才发展报告》 | 2025 |

浏览器访问：

| 页面 | 地址 |
|------|------|
| 数字经济大屏 | http://127.0.0.1:5000/ |
| 新能源产业大屏 | http://127.0.0.1:5000/corp |
| AI人才市场大屏 | http://127.0.0.1:5000/job |

## 项目结构

```
big_screen/
├── app.py              # Flask 入口，路由定义
├── data.py             # 数据模型（SourceData / CorpData / JobData）
├── data_simulator.py   # 实时数据增长模拟
├── templates/
│   └── index.html      # 大屏 HTML 模板
├── static/
│   ├── css/            # 样式文件
│   ├── js/             # ECharts / jQuery / 中国地图
│   └── picture/        # 静态图片
└── static_data/
    ├── corp.json       # 新能源产业数据
    └── job.json        # AI人才市场数据
```

## 数据管道

项目包含完整的数据处理管道，演示 ETL 流程：

```bash
# 从公开数据源重新生成 JSON 文件
python data_pipeline.py

# 同时更新 data.py 中的 SourceDataDemo
python data_pipeline.py --all
```

管道结构：

```
data_pipeline.py
  ├── Extract   → 从公开报告中提取原始数据点
  ├── Transform → 转换为 ECharts 图表格式
  └── Load      → 输出 static_data/*.json + 更新 data.py
```

## 自定义数据

编辑 `data.py` 中的 `SourceData` 类，替换 `echart*_data` 和 `map_1_data` 内的数据即可。格式参照已有的 `SourceDataDemo`。

新增页面：在 `data.py` 中新增数据类 → 在 `static_data/` 放入 JSON → 在 `app.py` 新增路由。

## License

MIT
