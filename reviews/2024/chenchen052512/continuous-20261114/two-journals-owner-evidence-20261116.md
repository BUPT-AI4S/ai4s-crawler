# 两刊2024逐条筛选收尾

本轮新增303条交付记录，并复核此前待定记录。原始字段、其他来源及他人工作保留。全部665条已逐条检查或有历史判定，仍有待定，不能视为665条均已完成最终判定。

| 期刊 | 官网/快照 | 纳入 | 排除 | 待定 | 未审 |
|---|---:|---:|---:|---:|---:|
| Robotics and Computer-Integrated Manufacturing | 170 | 62 | 100 | 8 | 0 |
| Remote Sensing of Environment | 495 | 181 | 274 | 40 | 0 |

官网目录逐文章号匹配：RCIM第85—90卷170条；RSE第300—315卷495条，无缺项或额外项。正式卷期年为2024，DOI中2023的在线优先记录仍计入。

本轮依次尝试正常浏览器、询问人工核验；负责人表示目前无法人工核验，随后采用可读出版方原摘要、作者机构原文和OpenAlex收录的原摘要。摘要/方法未充分取得的条目仍待定，公开PDF与代码未全面核实。

## 仍待补证

| 期刊 | 文章号 | 论文 | 仍缺证据 |
|---|---|---|---|
| RCIM | 102609 | [Knowledge graph and function block based Digital Twin modeling for robotic machining of large-scale components](https://doi.org/10.1016/j.rcim.2023.102609) | 知识图谱表示机器人加工参数与误差，功能块集成自适应调节并做铣削验证；需原文确认知识推理/学习机制，区分图式数据表示与AI对物理加工的实质作用。 |
| RCIM | 102627 | [Evaluating a self-manageable architecture for industrial automation systems](https://doi.org/10.1016/j.rcim.2023.102627) | 正式摘要和页面已核对；工业输送多智能体架构仍需方法原文区分自主推理决策与一般软件服务/消息编排，暂不据agent术语直接纳入。 |
| RCIM | 102626 | [Human Digital Twin in the context of Industry 5.0](https://doi.org/10.1016/j.rcim.2023.102626) | 综述提出人数字孪生架构及使能技术，但原摘要未指出具体AI及其直接研究贡献；需使能技术或应用章节确认。 |
| RCIM | 102625 | [Semantic models and knowledge graphs as manufacturing system reconfiguration enablers](https://doi.org/10.1016/j.rcim.2023.102625) | 已有原摘要支持知识图谱与语义能力匹配，但需正文明确推理机制和物理制造研究贡献；本轮摘要预览访问仍报内容错误。 |
| RCIM | 102649 | [An ontology-based data-model coupling approach for digital twin](https://doi.org/10.1016/j.rcim.2023.102649) | 本体数据模型耦合描述物实一致性，但摘要未说明学习或知识推理算法，且实验任务未具体展开；需方法及实验判断。 |
| RCIM | 102670 | [A closed-loop bin picking system for entangled wire harnesses using bimanual and dynamic manipulation](https://doi.org/10.1016/j.rcim.2023.102670) | 双臂动态摆动、触觉闭环解缠绕线束有明确物理任务，但摘要未说明感知或策略中的学习/推理机制；需方法确认是否仅规则反馈操控。 |
| RCIM | 102693 | [Towards a circular economy for electrical products: A systematic literature review and research agenda for automated recycling](https://doi.org/10.1016/j.rcim.2023.102693) | 电子产品自动回收综述覆盖目标识别、分选、机器人和调度，但摘要未明确AI方法及其研究权重；需正文区分实质AI综述与自动化概览。 |
| RCIM | 102724 | [Adaptive automation: Status of research and future challenges](https://doi.org/10.1016/j.rcim.2024.102724) | 已读输入完整综述摘要，但仍未明确具体AI方法；出版方预览页返回CPE00002，需综述方法及应用章节确认实质AI研究覆盖。 |
| RSE | 113922 | [Water availability and atmospheric dryness controls on spaceborne sun-induced chlorophyll fluorescence yield](https://doi.org/10.1016/j.rse.2023.113922) | 作者机构库原摘要可读部分研究SIF产额与水分/VPD及冠层导度，提及数据驱动导度产品但未明确AI训练及实质作用，需完整方法证据。 |
| RSE | 113935 | [Arctic tundra shrubification can obscure increasing levels of soil erosion in NDVI assessments of land cover derived from satellite imagery](https://doi.org/10.1016/j.rse.2023.113935) | 完整原摘要仍未明确UAV地表分类器，需分类方法章节确认是否学习式AI而非人工/传统分类流程。 |
| RSE | 113931 | [Inter- and intra-year forest change detection and monitoring of aboveground biomass dynamics using Sentinel-2 and Landsat](https://doi.org/10.1016/j.rse.2023.113931) | 森林TIIC变化检测和扰动归因任务明确，但公开摘要及可读片段未明确分类模型，需方法算法证据。 |
| RSE | 113952 | [A method for estimating high spatial resolution total precipitable water in all-weather condition by fusing satellite near-infrared and microwave observations](https://doi.org/10.1016/j.rse.2023.113952) | 微波/近红外水汽敏感指标和两步融合估计全天候可降水量，但可读原摘要未明确融合器模型，需方法确认是否学习式AI。 |
| RSE | 113964 | [Phytoplankton composition from sPACE: Requirements, opportunities, and challenges](https://doi.org/10.1016/j.rse.2023.113964) | 已补齐PACE浮游植物群落综述原摘要，但仍未明确AI方法的实质覆盖；需方法综述章节，不能因遥感主题直接纳入。 |
| RSE | 114013 | [Towards a standardized, ground-based network of hyperspectral measurements: Combining time series from autonomous field spectrometers with Sentinel-2](https://doi.org/10.1016/j.rse.2024.114013) | NDVI时序聚类评估地面光谱站空间代表性，但公开片段未注明具体聚类算法；引用/推荐论文的深度学习文字不作本论文证据。 |
| RSE | 114003 | [Satellite observations reveal a decreasing albedo trend of global cities over the past 35 years](https://doi.org/10.1016/j.rse.2024.114003) | 直接估计城市反照率并提到训练样本代表性，未说明估计器/训练算法；需核对是否采用AI学习。 |
| RSE | 114019 | [Detecting tree mortality using waveform features of airborne LiDAR](https://doi.org/10.1016/j.rse.2024.114019) | 以LiDAR波形特征二分类活/死树并评价准确度，需具体分类器及训练/验证方法确认AI角色。 |
| RSE | 114026 | [Ecoregion-wise fractional mapping of tree functional composition in temperate mixed forests with sentinel data: Integrating time-series spectral and radar data](https://doi.org/10.1016/j.rse.2024.114026) | 可读原摘要提出Fisher变换光谱雷达时序混合分解森林功能类型，但摘要被截断，尚不能确定是否含学习式AI，需完整方法/摘要。 |
| RSE | 114055 | [Pakistan's 2022 floods: Spatial distribution, causes and future trends from Sentinel-1 SAR observations](https://doi.org/10.1016/j.rse.2024.114055) | 已读洪水分布与成因原摘要可用部分，但其增强全国洪水检测算法未明确构成，需方法确认是否学习式AI或传统图像阈值处理。 |
| RSE | 114066 | [Spatial-temporal patterns of land surface evapotranspiration from global products](https://doi.org/10.1016/j.rse.2024.114066) | 已补得原摘要开头，研究比较25种ET产品；需方法确认是否实质评价或应用AI模型，而非仅采用上游产品。 |
| RSE | 114083 | [A study of annual tree-wise LiDAR intensity patterns of boreal species observed using a hyper-temporal laser scanning time series](https://doi.org/10.1016/j.rse.2024.114083) | LiDAR强度时序用于树种分类，摘要未说明分类器及训练，需具体方法以确认AI作用。 |
| RSE | 114051 | [Imaging spectroscopy investigations in wet carbon ecosystems: A review of the literature from 1995 to 2022 and future directions](https://doi.org/10.1016/j.rse.2024.114051) | 原摘要为湿碳生态系统成像光谱综述，未明确AI内容，需正文确认是否有实质AI方法综述。 |
| RSE | 114079 | [Efficacy of the SDGSAT-1 glimmer imagery in measuring sustainable development goal indicators 7.1.1, 11.5.2, and target 7.3](https://doi.org/10.1016/j.rse.2024.114079) | GLI去噪及路灯类型分类未交代算法，部分任务为经济/社会指标；需辨明AI是否实质用于物理照明/能效研究，不能泛纳所有SDG业务。 |
| RSE | 114096 | [Detecting early winter open-water zones on Alaska rivers using dual-polarized C-band Sentinel-1 synthetic aperture radar (SAR)](https://doi.org/10.1016/j.rse.2024.114096) | PCA配合训练式冰水监督分类，但末段又描述双极化阈值定制；需具体分类器以区分学习分类与阈值规则。 |
| RSE | 114102 | [Detection of soil and canopy freeze/thaw state in the boreal region with L and C Band Synthetic Aperture Radar](https://doi.org/10.1016/j.rse.2024.114102) | 零阶森林物理模型后对冻融后向散射做分类，需具体分类规则及有无学习过程证据。 |
| RSE | 114103 | [Detection of Land Surface Temperature anomalies using ECOSTRESS in Olkaria geothermal field](https://doi.org/10.1016/j.rse.2024.114103) | 以核尺度自适应检测地热温度异常，未说明核是空间窗口还是学习核方法；需算法细节。 |
| RSE | 114108 | [Remote sensing of diverse urban environments: From the single city to multiple cities](https://doi.org/10.1016/j.rse.2024.114108) | 多城市遥感八领域综述摘要未明确AI方法的实质内容，需正文确认AI科学研究综述覆盖程度。 |
| RSE | 114119 | [A transferable approach to assessing green infrastructure types (GITs) and their effects on surface urban heat islands with multi-source geospatial data](https://doi.org/10.1016/j.rse.2024.114119) | 多级绿地类型分类结合遥感温度和统计降温分析，但原摘要未明确分类器，需方法核实AI参与。 |
| RSE | 114120 | [Quantifying decadal stability of lake reflectance and chlorophyll-a from medium-resolution ocean color sensors](https://doi.org/10.1016/j.rse.2024.114120) | 比较9种Chla算法及按光学水体类型参数化，未列算法；需确认是否实质应用AI反演，而非纯经验/半分析方法。 |
| RSE | 114117 | [Monitoring of chlorophyll content in local saltwort species Suaeda salsa under water and salt stress based on the PROSAIL-D model in coastal wetland](https://doi.org/10.1016/j.rse.2024.114117) | 可读摘要主要为水盐控制生长实验及PROSAILD光学反演背景，后续反演/学习方法未完整取得，需补证AI角色。 |
| RSE | 114147 | [Four-decades of sediment transport variations in the Yellow River on the Loess Plateau using Landsat imagery](https://doi.org/10.1016/j.rse.2024.114147) | 原摘要建立Landsat悬沙浓度模型并分析四十年输沙，但未给出反演模型形式，需方法区分学习模型与经验光谱关系。 |
| RSE | 114151 | [Mangrove species mapping in coastal China using synthesized Sentinel-2 high-separability images](https://doi.org/10.1016/j.rse.2024.114151) | 合成高可分Sentinel2并以概率分类形成全国红树物种图，但原摘要未明确分类学习器，需模型训练/分类方法证据。 |
| RSE | 114194 | [Unmixing-based forest recovery indicators for predicting long-term recovery success](https://doi.org/10.1016/j.rse.2024.114194) | 光谱解混恢复指标预测森林长期恢复，未说明解混及预测算法；需核对是否为AI学习而非阈值/经验回归。 |
| RSE | 114195 | [A multi-source change detection algorithm supporting user customization and near real-time deforestation detections](https://doi.org/10.1016/j.rse.2024.114195) | 多源近实时砍伐概率检测及延迟精度权衡任务清楚，但原摘要未明确学习式分类器或统计判别构成，需算法方法证据。 |
| RSE | 114174 | [Repeat GEDI footprints measure the effects of tropical forest disturbances](https://doi.org/10.1016/j.rse.2024.114174) | GEDI近重合足迹检测与扰动参数-生物量关系建模，摘要未说明关联模型；需核对有无AI学习及其科学作用。 |
| RSE | 114244 | [Novel 3D photosynthetic traits derived from the fusion of UAV LiDAR point cloud and multispectral imagery in wheat](https://doi.org/10.1016/j.rse.2024.114244) | 以无人机光谱指标估算小麦光合参数并投影到LiDAR三维空间，原摘要未明确预测器是否AI或经验回归，需方法。 |
| RSE | 114276 | [Intercomparison of global foliar trait maps reveals fundamental differences and limitations of upscaling approaches](https://doi.org/10.1016/j.rse.2024.114276) | 比较多种统计升尺度叶性状地图及回归制图误差，但未列模型；需确认是否对AI模型进行实质科学评测。 |
| RSE | 114299 | [Heterogeneity in ice-wedge permafrost degradation revealed across spatial scales](https://doi.org/10.1016/j.rse.2024.114299) | 以相似沟宽/淹水特征聚类冻土退化地貌，但未给聚类算法；需核对是否AI学习及制图方法。 |
| RSE | 114346 | [Patterns and Trends in Northern Hemisphere River Ice Phenology from 2000 to 2021](https://doi.org/10.1016/j.rse.2024.114346) | 北半球河冰物候图与气候因子贡献研究的原摘要未明确冰像元识别及贡献模型，需要方法确认AI作用。 |
| RSE | 114354 | [Global mapping of human-transformed dike-pond systems](https://doi.org/10.1016/j.rse.2024.114354) | 完整原摘要描述全球堤塘时空图和环境影响，但未明示制图分类模型，需方法区分学习式分类与规则测图。 |
| RSE | 114376 | [Increase in gross primary production of boreal forests balanced out by increase in ecosystem respiration](https://doi.org/10.1016/j.rse.2024.114376) | 通量塔监督训练遥感碳通量模型并研究北方森林收支，未列具体学习算法；需方法证据。 |
| RSE | 114378 | [Urbanization-induced spatial and temporal patterns of local drought revealed by high-resolution fused remotely sensed datasets](https://doi.org/10.1016/j.rse.2024.114378) | 两步地面栅格/点栅格融合生成气象数据并分析城市干旱，但原摘要未说明融合模型，需方法确认AI实质作用。 |
| RSE | 114382 | [Monitoring spatially heterogeneous riparian vegetation around permanent waterholes: A method to integrate LiDAR and Landsat data for enhanced ecological interpretation of Landsat fPAR time-series](https://doi.org/10.1016/j.rse.2024.114382) | LiDAR植被结构分类结合Landsat fPAR时序分解研究河岸生态，未说明分类算法；需确认AI作用。 |
| RSE | 114414 | [Mobile laser scanning as reference for estimation of stem attributes from airborne laser scanning](https://doi.org/10.1016/j.rse.2024.114414) | 以移动激光扫描参考数据训练树干胸径/体积估计器，摘要未说明模型类别；需具体算法确认AI学习。 |
| RSE | 114406 | [Mapping global drought-induced forest mortality based on multiple satellite vegetation optical depth data](https://doi.org/10.1016/j.rse.2024.114406) | 原摘要说明训练点优化及死亡率预测模型，但具体模型未明确，需方法补证。 |
| RSE | 114428 | [Dynamic assessment of the impact of compound dry-hot conditions on global terrestrial water storage](https://doi.org/10.1016/j.rse.2024.114428) | 干热复合事件水储量风险框架未说明具体估计方法，无法判定AI作用。 |
| RSE | 114448 | [Potential of SDGSAT-1 nighttime light data in extracting urban main roads](https://doi.org/10.1016/j.rse.2024.114448) | 主方法为地形骨架几何提取，仅提及对比U-Net；需核实AI实验是否实质用于科学任务。 |
| RSE | 114440 | [Stability of cloud detection methods for Land Surface Temperature (LST) Climate Data Records (CDRs)](https://doi.org/10.1016/j.rse.2024.114440) | 比较完全贝叶斯、naïve probabilistic及阈值云掩膜；需方法区分学习式朴素贝叶斯分类与先验辐射物理概率推断。 |
| RSE | 114457 | [Observation-based quantification of aerosol transport using optical flow: A satellite perspective to characterize interregional transport of atmospheric pollution](https://doi.org/10.1016/j.rse.2024.114457) | 以计算机视觉光流及气溶胶物理约束估算污染输送；需方法确认是否学习式AI或仅传统变分/解析光流。 |
