--- agent.py.orig	2015-12-05 17:19:37 UTC
+++ agent.py
@@ -46,7 +46,6 @@ from utils.profile import AgentProfiler
 
 # Constants
 PID_NAME = "dd-agent"
-PID_DIR = "/var/run/datadog"
 WATCHDOG_MULTIPLIER = 10
 RESTART_INTERVAL = 4 * 24 * 60 * 60  # Defaults to 4 days
 START_COMMANDS = ['start', 'restart', 'foreground']
@@ -291,7 +290,7 @@ def main():
         deprecate_old_command_line_tools()
 
     if command in COMMANDS_AGENT:
-        agent = Agent(PidFile(PID_NAME, PID_DIR).get_path(), autorestart, in_developer_mode=in_developer_mode)
+        agent = Agent(PidFile('dd-agent').get_path(), autorestart, in_developer_mode=in_developer_mode)
 
     if command in START_COMMANDS:
         log.info('Agent version %s' % get_version())