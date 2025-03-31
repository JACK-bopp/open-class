import os
from crawler.utils.logger import logger
from crawler.utils.database import db_manager
from crawler.utils.scheduler import scheduler
from crawler.utils.alert import alert_manager
from crawler.monitoring.spider_monitor import SpiderMonitor

def main():
    """主程序入口"""
    try:
        # 初始化日志
        logger.info("正在启动爬虫系统...")
        
        # 初始化数据库连接
        logger.info("正在连接数据库...")
        db_manager.db.command("ping")
        logger.info("数据库连接成功")
        
        # 初始化监控系统
        logger.info("正在初始化监控系统...")
        monitor = SpiderMonitor(
            mongo_uri=os.getenv("MONGO_URI"),
            database=os.getenv("MONGO_DATABASE")
        )
        
        # 启动定时任务
        logger.info("正在启动定时任务...")
        scheduler.start()
        
        # 启动告警系统
        logger.info("正在启动告警系统...")
        # 添加定时检查任务
        scheduler.scheduler.add_job(
            alert_manager.check_errors,
            'interval',
            hours=1,
            id='error_check'
        )
        scheduler.scheduler.add_job(
            alert_manager.check_performance,
            'interval',
            hours=1,
            id='performance_check'
        )
        scheduler.scheduler.add_job(
            alert_manager.check_data_quality,
            'interval',
            hours=1,
            id='quality_check'
        )
        
        logger.info("爬虫系统启动完成")
        
        # 保持程序运行
        try:
            while True:
                pass
        except KeyboardInterrupt:
            logger.info("正在关闭爬虫系统...")
            scheduler.stop()
            db_manager.close()
            logger.info("爬虫系统已关闭")
    
    except Exception as e:
        logger.error(f"系统启动失败: {str(e)}")
        raise

if __name__ == "__main__":
    main() 