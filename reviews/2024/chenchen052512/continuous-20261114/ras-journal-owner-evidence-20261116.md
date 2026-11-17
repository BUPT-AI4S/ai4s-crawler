# Robotics and Autonomous Systems 2024整刊筛选

本轮新增156条记录，保留此前43条判定。
累计199条：纳入69、排除119、待定11、未审0。所有条目已检查或有历史判定；11条仍缺最终判定证据。

## 官网目录核对

正式出版年2024，第171—182卷，分别20、23、10、19、21、14、9、9、21、14、15、24条，共199条。完整目录与采集快照逐文章号对应，无缺项/额外项。含174篇研究、9篇简评综述、12条编委名单、2条社论及2条更正。

15篇输入摘要逐篇阅读；正常浏览器补读13篇出版方原摘要；其他112篇逐条查可读原摘要/方法。原摘要及原文没读出的信息不作补造。部分页面出现CPE00002，按负责人此前无法人工核验的答复使用可读出版方和作者公开原文继续补证。候选文件2条，缺摘要0，未将全量书目缺漏冒充候选指标。

## 待补证11篇

| 文章号 | 论文 | 缺少的证据 |
|---|---|---|
| 104555 | [Shared autonomy and positive power control for powered exoskeletons](https://doi.org/10.1016/j.robot.2023.104555) | 共享自主外骨骼通过接受度更新任务目标，需具体更新算法确认学习机制，不能仅凭learn术语纳入。 |
| 104603 | [Dual-stage planner for autonomous radioactive source localization in unknown environments](https://doi.org/10.1016/j.robot.2023.104603) | 双阶段机器人放射源定位有明确物理任务，需源项估计和行动规划方法确认是否学习/概率AI或几何数值估计。 |
| 104618 | [Adaptation of hand exoskeletons for occupational augmentation: A literature review](https://doi.org/10.1016/j.robot.2024.104618) | 手外骨骼设计综述涉及优化及生成设计，但摘要未明确AI方法，需正文核实AI内容是否实质。 |
| 104620 | [Defense against smart invaders with swarms of sweeping agents](https://doi.org/10.1016/j.robot.2024.104620) | 仅取得原摘要首段，防御策略任务明确但缺具体方法，不能据smart/swarm术语判断AI。 |
| 104644 | [JPMDP: Joint base placement and multi-configuration path planning for 3D surface disinfection with a UV-C robotic system](https://doi.org/10.1016/j.robot.2024.104644) | UV-C消毒机器人基座与覆盖路径联合优化任务明确，但未给具体智能搜索/学习机制，需方法部分。 |
| 104653 | [An overview of transfer nursing robot: Classification, key technology, and trend](https://doi.org/10.1016/j.robot.2024.104653) | 转运护理机器人综述涉及机器感知和控制，但摘要未明确实质AI方法，需正文补证。 |
| 104634 | [DynaTM-SLAM: Fast filtering of dynamic feature points and object-based localization in dynamic indoor environments](https://doi.org/10.1016/j.robot.2024.104634) | DynaTM-SLAM目标检测与模板匹配滤除动态点，需明确检测器是否为学习模型及训练/推理证据。 |
| 104701 | [Compensation-corrective adaptive control strategy for upper-limb rehabilitation robots](https://doi.org/10.1016/j.robot.2024.104701) | 康复机器人导纳控制中两个估计器评估运动意图及代偿辅助，需估计器方法确认是否学习模型。 |
| 104744 | [A review of advances in underwater humanoid robots for human–machine cooperation](https://doi.org/10.1016/j.robot.2024.104744) | 水下类人机器人感知决策执行综述未明确具体AI方法，需正文确认实质AI研究覆盖。 |
| 104757 | [Climbing robot for advanced high-temperature weld bead inspection](https://doi.org/10.1016/j.robot.2024.104757) | 高温焊缝超声检测机器人有感知识别焊缝功能，需具体识别算法确认AI而非传统图像几何。 |
| 104814 | [Approximate sequential optimization for informative path planning](https://doi.org/10.1016/j.robot.2024.104814) | 高斯过程信息指标、动态规划与凸松弛的信息路径方法明确，但摘要未给具体科学/物理机器人任务，需应用实验补证直接研究贡献。 |

## 本轮新增纳入52篇

| 文章号 | 论文 | AI与工程研究作用 |
|---|---|---|
| 104536 | [Base position and task assignment optimization concerning productivity and machining performance for multi-robot systems in aerospace manufacturing](https://www.sciencedirect.com/science/article/pii/S0921889023001756) | 初筛漏筛补录。改造NSGA-II交叉修正算子联合搜索机器人基座与任务分配，优化航天部件加工刚度及效率，直接服务物理加工性能。 |
| 104560 | [3D traversability analysis and path planning based on mechanical effort for UGVs in forest environments](https://www.sciencedirect.com/science/article/pii/S0921889023001999) | 初筛漏筛补录。原文系统实现明确A*全局规划和trajectory rollout，机械功耗代价图直接引导森林UGV节能通行路径。 |
| 104572 | [Mask-VRDet: A robust riverway panoptic perception model based on dual graph fusion of vision and 4D mmWave radar](https://www.sciencedirect.com/science/article/pii/S0921889023002117) | 初筛漏筛补录。Mask-VRDet以图神经网络融合视觉及4D毫米波雷达，完成无人船内河环境目标检测与语义分割。 |
| 104570 | [Improved RRT global path planning algorithm based on Bridge Test](https://www.sciencedirect.com/science/article/pii/S0921889023002099) | 初筛漏筛补录。Bridge Test引导多树RRT搜索和点云聚类定位窄通道，经真实机器人验证改进避障路径规划。 |
| 104580 | [Towards comprehensive understanding of pedestrians for autonomous driving: Efficient multi-task-learning-based pedestrian detection, tracking and attribute recognition](https://www.sciencedirect.com/science/article/pii/S0921889023002191) | 初筛漏筛补录。多任务共享特征模型学习行人检测、跟踪和属性，直接支持自动驾驶与行人安全交互感知。 |
| 104581 | [Overcome the Fear Of Missing Out: Active sensing UAV scanning for precision agriculture](https://www.sciencedirect.com/science/article/pii/S0921889023002208) | 初筛漏筛补录。深度分割模型识别作物和杂草，按检测数量与置信度调整无人机主动扫描速度，支持精准农业采样。 |
| 104584 | [Autonomous hierarchy creation for computationally feasible near-optimal path planning in large environments](https://lamor.fer.hr/images/50036607/2024-jrogina-Hgraf-RAS.pdf) | 初筛漏筛补录。自动生成分层H图并以E*搜索部分路径，在建筑、仓储和城市机器人场景减少路径规划搜索节点。 |
| 104567 | [A novel end-to-end vision-based architecture for agricultural human–robot collaboration in fruit picking operations](https://www.sciencedirect.com/science/article/abs/pii/S0921889023002063) | 初筛漏筛补录。CNN及RNN检测跟踪分类果园采摘者活动并估计位置，直接驱动辅助采摘物流机器人协作。 |
| 104587 | [Intelligent decision-making system for multiple marine autonomous surface ships based on deep reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0921889023002269) | 初筛漏筛补录。PPO结合船舶领域、操纵特性及BiGRU，实现遵循避碰规则的多船自主航行决策。 |
| 104592 | [Mobile robot’s path-planning and path-tracking in static and dynamic environments: Dynamic programming approach](https://www.sciencedirect.com/science/article/pii/S0921889023002312) | 初筛漏筛补录。原文引言明确Bellman动态规划搜索静态障碍最短路径，结合NMPC跟踪处理动态避障，直接服务移动机器人导航。 |
| 104600 | [A visual imitation learning algorithm for the selection of robots’ grasping points](https://www.sciencedirect.com/science/article/abs/pii/S0921889023002397) | 初筛漏筛补录。CNN从视频人类抓取示范学习抓取姿态，以双臂机器人验证快速新任务学习。 |
| 104606 | [R2: Optimal vector-based and any-angle 2D path planning with non-convex obstacles](https://linkinghub.elsevier.com/retrieve/pii/S0921889023002452) | 初筛漏筛补录。R2/R2E以伪目标和进展规则引导启发式转折点搜索，直接改进机器人避障路径规划。 |
| 104607 | [A novel hedge algebra formation control for mobile robots](https://www.sciencedirect.com/science/article/abs/pii/S0921889023002464) | 初筛漏筛补录。原文引言明确HA对语言变量语义及人类知识推理进行代数插值表达，构造机器人编队控制并与模糊控制比较。 |
| 104616 | [Path Inference based on Voronoi Graph for Unmanned Maritime Vehicles](https://www.sciencedirect.com/science/article/abs/pii/S0921889023002555) | 初筛漏筛补录。Voronoi图与高效深度优先路径推断搜索满足距离约束的海事机器人巡逻和搜救路径。 |
| 104629 | [A review of perception sensors, techniques, and hardware architectures for autonomous low-altitude UAVs in non-cooperative local obstacle avoidance](https://www.sciencedirect.com/science/article/pii/S0921889024000125) | 初筛漏筛补录。低空无人机避障综述明确将AI方法作为四类核心技术之一，直接综述自主无人机无碰撞感知及控制。 |
| 104619 | [A heterogeneous attention fusion mechanism for the cross-environment scene classification of the home service robot](https://www.sciencedirect.com/science/article/pii/S0921889024000022) | 初筛漏筛补录。注意力及全连接网络融合整体和对象属性，以跨环境机器人视角数据训练测试家用服务机器人场景感知。 |
| 104613 | [iCORPP: Interleaved commonsense reasoning and probabilistic planning on robots](https://www.sciencedirect.com/science/article/abs/pii/S092188902300252X) | 初筛漏筛补录。iCORPP以P-log常识逻辑概率推理动态构造POMDP，支持真实机器人室内导航与服务决策。 |
| 104633 | [A Collision-free path planning approach based on rule guided lazy-PRM with repulsion field for gantry welding robots](https://www.sciencedirect.com/science/article/pii/S0921889024000162) | 初筛漏筛补录。规则引导Lazy-PRM与斥力场搜索双臂龙门焊接机器人无碰撞路径，含实际焊接应用验证。 |
| 104651 | [A hybrid technique linked FOPID for a nonlinear system based on closed-loop settling time of plant](https://www.sciencedirect.com/science/article/abs/pii/S0921889024000344) | 初筛漏筛补录。FAT-AOS混合智能优化搜索FOPID增益，研究风电及水电非线性系统扰动控制性能。 |
| 104656 | [Informed sampling space driven robot informative path planning](https://www.sciencedirect.com/science/article/pii/S0921889024000393) | 初筛漏筛补录。启发式采样空间引导RRT*信息路径搜索，同时优化机器人危险环境导航和重点区域探索。 |
| 104654 | [MARLIN: A cloud integrated robotic solution to support intralogistics in retail](https://www.sciencedirect.com/science/article/pii/S092188902400037X) | 初筛漏筛补录。作者DFKI公开原文Task Planning明确ROSPlan/POPF知识库规划，与语义数字孪生同步，真实机器人完成门店补货导航与拖车操作。 |
| 104659 | [A Reinforcement Learning Approach to Find Optimal Propulsion Strategy for Microrobots Swimming at Low Reynolds Number](https://www.sciencedirect.com/science/article/pii/S0921889024000423) | 初筛漏筛补录。Q-learning学习低雷诺数球杆微型游泳机器人最优推进周期，研究几何配置及不确定环境中的推进物理。 |
| 104655 | [A new approach to smooth path planning of Ackerman mobile robot based on improved ACO algorithm and B-spline curve](https://www.sciencedirect.com/science/article/abs/pii/S0921889024000381) | 初筛漏筛补录。改进蚁群启发式和信息素机制搜索Ackermann机器人平滑路径，满足最小转弯半径与运动学约束。 |
| 104661 | [Modeling, design and control of a 4-arm delta parallel manipulator employing type-1 and interval type-2 fuzzy logic-based techniques for precision applications](https://www.sciencedirect.com/science/article/pii/S0921889024000447) | 初筛漏筛补录。一型与区间二型TSK模糊PD/PID控制四臂Delta机器人，比较轨迹跟踪及外扰抑制性能。 |
| 104662 | [Design and stabilization of a Coandă effect-based UAV: Comparative study between fuzzy logic and PID control approaches](https://linkinghub.elsevier.com/retrieve/pii/S0921889024000459) | 初筛漏筛补录。Sugeno模糊控制稳定Coanda效应无人机，并以软硬件实验与PID比较。 |
| 104664 | [Feature Aware Re-weighting (FAR) in Bird’s Eye View for LiDAR-based 3D object detection in autonomous driving applications](https://www.sciencedirect.com/science/article/pii/S0921889024000472) | 初筛漏筛补录。FAR注意力神经网络重加权鸟瞰点云特征，改进自动驾驶LiDAR三维环境目标检测。 |
| 104674 | [Object-aware interactive perception for tabletop scene exploration](https://research.itu.edu.tr/en/publications/object-aware-interactive-perception-for-tabletop-scene-exploratio/) | 初筛漏筛补录。联合主动传感与物体操作行动空间按体素效用选择下一行动，真实Baxter机器人验证遮挡桌面场景探索。 |
| 104678 | [A novel hybrid swarm intelligence algorithm for solving TSP and desired-path-based online obstacle avoidance strategy for AUV](https://www.sciencedirect.com/science/article/pii/S0921889024000617) | 初筛漏筛补录。海鸥优化与蚁群及2Opt混合搜索AUV巡航路径，海试验证海洋工程任务及声呐避障。 |
| 104673 | [Wiring connector-terminated cables based on manipulation planning with collision-free EMD net](https://linkinghub.elsevier.com/retrieve/pii/S0921889024000563) | 初筛漏筛补录。扩展EMD编码操控解码网络预测柔性电缆形变，规划无碰撞布线并验证真实线缆操控。 |
| 104663 | [Towards field deployment of MAVs in adaptive exploration of GPS-denied subterranean environments](https://linkinghub.elsevier.com/retrieve/pii/S0921889024000460) | 初筛漏筛补录。双层前沿目标选择及风险感知网格路径规划支持无人机地下洞穴自主探索，结合MPC与人工势场。 |
| 104681 | [Sequential control barrier functions for mobile robots with dynamic temporal logic specifications](https://www.sciencedirect.com/science/article/pii/S0921889024000642) | 初筛漏筛补录。时序逻辑任务分解及可行执行序列生成结合CBF，支持真实空中机器人动态目标任务规划与控制。 |
| 104700 | [TEFu-Net: A time-aware late fusion architecture for robust multi-modal ego-motion estimation](https://www.sciencedirect.com/science/article/abs/pii/S0921889024000836) | 初筛漏筛补录。TEFu-Net以LSTM深度融合立体图像、LiDAR和GNSS/IMU运动估计，增强真实自动驾驶定位鲁棒性。 |
| 104698 | [Collision-free path planning for multiple robots using efficient turn-angle assignment](https://www.sciencedirect.com/science/article/pii/S0921889024000812) | 初筛漏筛补录。在离散转向候选空间中周期性求解多机器人无碰撞角度分配，以任务时间和能耗验证协同路径规划。 |
| 104712 | [Convergent wheeled robot navigation based on an interpolated potential function and gradient](https://www.sciencedirect.com/science/article/pii/S0921889024000952) | 初筛漏筛补录。网格搜索生成连续势函数并与MPC结合，引导真实Husky机器人动态环境中收敛无碰撞导航。 |
| 104721 | [A method for grasp detection of flexible four-finger gripper](https://www.sciencedirect.com/science/article/pii/S0921889024001040) | 初筛漏筛补录。AGNN融合RGB-D和空洞空间金字塔预测柔性四指夹爪抓取姿态，并用真实机械臂验证未知物体抓取。 |
| 104723 | [“Reinforcement learning particle swarm optimization based trajectory planning of autonomous ground vehicle using 2D LiDAR point cloud”](https://www.sciencedirect.com/science/article/pii/S0921889024001064) | 初筛漏筛补录。RLPSO利用环境反馈适应轨迹规划，以LiDAR占据图及真实AGV实验研究动态避障导航。 |
| 104724 | [Long-term navigation for autonomous robots based on spatio-temporal map prediction](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001076) | 初筛漏筛补录。原摘要与原文贡献段确认时变A*搜索预测代价图，支持多周真实轮椅机器人导航；地图预测本身是ARMA，不标学习方法。 |
| 104730 | [UAV path planning algorithm based on Deep Q-Learning to search for a floating lost target in the ocean](https://www.sciencedirect.com/science/article/pii/S0921889024001143) | 初筛漏筛补录。Deep Q-learning学习真实海流数据驱动漂浮目标动力学，规划无人机群海上搜救搜索路径。 |
| 104748 | [Cooperative path planning study of distributed multi-mobile robots based on optimised ACO algorithm](https://www.sciencedirect.com/science/article/pii/S0921889024001325) | 初筛漏筛补录。萤火虫、启发函数及人工势场改进蚁群，直接研究二维三维多机器人协同路径规划。 |
| 104760 | [A versatile door opening system with mobile manipulator through adaptive position-force control and reinforcement learning](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001441) | 初筛漏筛补录。CNN识别门把手和门特征，深度RL学习低作用力开门策略，并与自适应位置力控制实际比较。 |
| 104771 | [Optimizing robotic arm control using deep Q-learning and artificial neural networks through demonstration-based methodologies: A case study of dynamic and static conditions](https://www.sciencedirect.com/science/article/pii/S0921889024001556) | 初筛漏筛补录。以示范训练DQN、ANN及ADQN控制机械臂，比较静态与动态目标任务成功率及学习收敛。 |
| 104774 | [Learning continuous multi-UAV controls with directed explorations for flood area coverage](https://www.sciencedirect.com/science/article/pii/S0921889024001581) | 初筛漏筛补录。DDPG融合地表高程驱动DINF洪水流向知识和路径分散策略，学习多无人机洪区覆盖连续控制。 |
| 104773 | [A decoupled solution to heterogeneous multi-formation planning and coordination for object transportation](https://linkinghub.elsevier.com/retrieve/pii/S092188902400157X) | 初筛漏筛补录。冲突搜索结合轨迹优化与去中心协调，解决异质机器人编队实体运输的碰撞与刚性约束。 |
| 104783 | [An improved frontier-based robot exploration strategy combined with deep reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0921889024001672/pdf) | 初筛漏筛补录。深度RL从地图选择前沿目标，训练网络后迁移真实机器人实现未知环境自主探索。 |
| 104782 | [Robust iterative value conversion: Deep reinforcement learning for neurochip-driven edge robots](https://www.sciencedirect.com/science/article/pii/S0921889024001660) | 初筛漏筛补录。RIVC训练可部署神经芯片的脉冲策略，并在真实神经芯片机器人上验证功耗速度与策略训练，直接支持实体边缘机器人控制。 |
| 104794 | [Enhancing radioactive environment exploration with bio-inspired swarm robotics: A comparative analysis of Lévy flight and stigmergy methods](https://www.sciencedirect.com/science/article/pii/S0921889024001787/pdf) | 初筛漏筛补录。比较Levy飞行与环境迹通讯指导机器人群放射性环境探索，研究辐射暴露、覆盖效率及地图生成。 |
| 104797 | [Lane-changing and overtaking trajectory planning for autonomous vehicles with multi-performance optimization considering static and dynamic obstacles](https://www.sciencedirect.com/science/article/pii/S0921889024001817) | 初筛漏筛补录。PSO搜索变道时间、速度及位移，联合车辆安全、舒适、稳定与排放物理性能优化自动超车轨迹。 |
| 104796 | [Multi-objective QoS optimization in swarm robotics](https://www.sciencedirect.com/science/article/pii/S0921889024001805) | 初筛漏筛补录。SVR学习发射功率、距离及包参数到QoS的关系，结合遗传搜索优化机器人群无线通信延迟和可靠性。 |
| 104787 | [GSC: A graph-based skill composition framework for robot learning](https://www.sciencedirect.com/science/article/pii/S0921889024001714) | 初筛漏筛补录。GSC以技能图及Transformer式图更新组合既有RL技能，并在真实四足机器人导航验证。 |
| 104811 | [Model-less optimal visual control of tendon-driven continuum robots using recurrent neural network-based neurodynamic optimization](https://www.sciencedirect.com/science/article/pii/S0921889024001957) | 初筛漏筛补录。逆矩阵无关RNN神经动力优化求解视觉伺服QP，支持腱驱连续体机器人狭窄环境约束目标跟踪。 |
| 104822 | [Improved ACO algorithm fused with improved Q-Learning algorithm for Bessel curve global path planning of search and rescue robots](https://www.sciencedirect.com/science/article/pii/S0921889024002069) | 初筛漏筛补录。融合改进蚁群信息素与Q-learning矩阵、自适应探索和Bessel平滑，规划搜救机器人全局避障路径。 |
| 104819 | [Fusion innovation: Multi-scale dilated collaborative model of ConvNeXt and MSDA for fault diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S0921889024002033) | 初筛漏筛补录。ConvNeXt与多尺度空洞注意力学习轴承和齿轮故障信号，实现跨设备机械状态诊断。 |
