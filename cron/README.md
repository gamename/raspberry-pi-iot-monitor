
You can call the `report.sh` either manually or via a cron job.  Here is a suggested example of a cron job. In this 
particular example, `report.sh` is run every 6 hours. See this [website](https://crontab.guru/) for more information.


0 */6 * * * ~/raspberry_pi_iot_monitor/shell/report.sh & 