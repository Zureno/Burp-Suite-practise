from burp import IBurpExtender
from burp import IScannerCheck
from burp import IScanIssue
from jarray import array
import re

class BurpExtender(IBurpExtender,IScannerCheck):
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks = callbacks
        self._callbacks.setExtensionName("SonySecret")
        self._callbacks.registerScannerCheck(self)
        print("Show some love for the plugin")
        print("Passive scanner to extract Secrets")
        print("By: Pranshu")
        return
    def consolidateDuplicateIssues(self,existingIssue, newIssue):
        if (existingIssue.getIssueDetail() == newIssue.getIssueDetail()):
            return -1
        else:
            return 0 
    def doPassiveScan(self,baseRequestResponse):
        scan_issues = []
        tmp_issues = []
    
        self._CustomScans = CustomScans(baseRequestResponse, self._callbacks)

        keywords = [

        ]
        for key in keywords:
            regex = "(?i)"+key+"['\"]?\s?(=|:)?\s?['\"]?([^\s\"'&]+)"
            issuename = "SecretsScanner ["+key+"]"
            issuelevel = ""
            issuedetail = """[$key$]: <b>$value$</b><br><br><b>Info:</b> Got a sensitive info"""
            tmp_issues = self._CustomScans.findRegEx(regex,key,issuename,issuelevel,issuedetail)
            scan_issues = scan_issues + tmp_issues
        if len(scan_issues) > 0:
            return scan_issues
        else:
            return None