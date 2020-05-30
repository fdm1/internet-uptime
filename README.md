# internet-uptime

Log internet connectivity to determine just how flaky the internet _really_ is.

Run via a cron (or whatever scheduler you want), every N minutes, log if a connection can be made to the router, as well as an external host (google).

### Running on cron

[Resource for enabling cron on windows 10 with wsl2](https://blog.snowme34.com/post/schedule-tasks-using-crontab-on-windows-10-with-wsl/index.html)

```bash
# Log status every 3 minutes
*/3 * * * * /path/to/repo/docker-run.sh
```

### TODO

* hook up to some monitoring server (e.g. grafana)
* log to something more substantial than a csv (maybe??? depends on what is needed for monitoring service input)
