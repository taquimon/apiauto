import pymsteams
import xml.etree.ElementTree as ET

WEB_HOOK = "https://jalacorp.webhook.office.com/webhookb2/f258aa5b-882d-4f85-91f7-d441b4ccb2f4@67fc19c4-301c-4f98-aab9-827d7e165edc/IncomingWebhook/f20ee1df654e4f6fb2212c5b0f4ea8e6/3ae1ea10-c6c9-411c-990f-35cdbbd64224"

team_message = pymsteams.connectorcard(WEB_HOOK)

with open("xml-report/nose2-unit.xml", encoding="utf-8") as report_html:
    report = report_html.read()

tree = ET.parse("xml-report/nose2-unit.xml")
root = tree.getroot()
# summary of results
summary = []
for child in root.iter():
    if child.tag == "testsuite":
        summary = [list(x) for x in child.items()]

automation_summary = f"""
**Automation Results:**

**Duration**	{summary[5][1]} sec <br>
**Tests**	    {summary[4][1]} <br>
**Passed**	    {int(summary[4][1]) - int(summary[2][1])} <br>
**Failures**	{summary[2][1]}  <br>
"""
test_cases = []
for tc in root.findall("testcase"):
    test = {}
    test["Test Name"] = tc.get("name")
    test["Test Status"] = "Passed"
    failure = tc.find("failure")
    if failure is not None:
        test["Test Status"] = "Failed"
        test["Error Message"] = failure.text
    test_cases.append(test)
automation_results = []
for t in test_cases:
    automation_results.append(f"""<br>
    **Test Name:**     {t["Test Name"]} 
    **Test Status:**   {t["Test Status"]} <br>
    """)
    if "Error Message" in t:
        automation_results.append(f"""
        ** ErrorMessage: ** {t["Error Message"]}
        """)

print(automation_results)

team_message.text(automation_summary + str(automation_results))
team_message.send()
