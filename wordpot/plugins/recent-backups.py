from wordpot.plugins_manager import BasePlugin
import re

RECENTBACKUPS_RE     = re.compile('recent-backups|downloadfile', re.I)

class Plugin(BasePlugin):
    def run(self):
        # Logic
            # Message to log
#            log = '%s probed for recent-backups: %s' % (self.inputs['request'].x_forward_for, self.inputs['subpath'])
	 #if 'HTTP_X_FORWARDED_FOR' in request.META:
         # request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        if RECENTBACKUPS_RE.search(self.inputs['subpath']) is not None:
	        log = '%s probed for recent-backups: %s' % (self.inputs['request'].remote_addr, self.inputs['subpath'])
	       	self.outputs['log'] = log
  		self.outputs['log_json'] = self.to_json_log(filename=self.inputs['subpath'], plugin='recent-backups')
            # Template to render
	   	self.outputs['template'] = 'recent-backups.html'
        return
