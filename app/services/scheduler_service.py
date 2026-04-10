from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone


def start_scheduler(bot):
    scheduler = BackgroundScheduler(timezone=timezone("America/Sao_Paulo"))

    def job():
        print("Rotina diária 06:00 executada")

    scheduler.add_job(job, 'cron', hour=6, minute=0)
    scheduler.start()
