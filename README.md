# 图表分析平台

一个功能强大的图表分析和分享平台，支持多种图表类型和数据分析功能。

## 功能特点

- 多种图表类型支持
  - 基础图表：柱状图、折线图、饼图、散点图
  - 高级图表：雷达图、漏斗图、仪表盘、热力图
  - 企业图表：树图、旭日图、桑基图、箱线图等

- 数据分析功能
  - 基础统计分析
  - 趋势分析
  - 预测分析
  - 自定义分析

- 用户管理
  - 多角色支持
  - 权限控制
  - 订阅计划

- 分享功能
  - 多平台分享
  - 二维码生成
  - 分享统计

## 技术栈

- 前端
  - Vue 3
  - Element Plus
  - ECharts
  - Vue Router
  - Axios

- 后端
  - Spring Boot
  - Spring Security
  - MySQL
  - Redis
  - JWT

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/your-username/chart-platform.git
cd chart-platform
```

2. 安装依赖
```bash
# 前端
cd frontend
npm install

# 后端
cd ../backend
mvn install
```

3. 运行开发服务器
```bash
# 前端
npm run dev

# 后端
mvn spring-boot:run
```

## 部署

本项目使用 Vercel 进行前端部署，后端可以部署在任何支持 Java 的服务器上。

### 前端部署

1. Fork 本仓库
2. 在 Vercel 中导入项目
3. 配置环境变量
4. 部署

### 后端部署

1. 配置数据库
2. 配置 Redis
3. 设置环境变量
4. 构建并运行

## 订阅计划

- 免费版
  - 基础图表功能
  - 最多5个图表
  - PNG格式导出
  - 100MB存储空间

- 高级版
  - 高级图表功能
  - 最多20个图表
  - 多格式导出
  - 1GB存储空间

- 企业版
  - 企业级图表功能
  - 最多100个图表
  - 全格式导出
  - 10GB存储空间

## 贡献指南

欢迎提交 Pull Request 和 Issue。

## 许可证

MIT License 