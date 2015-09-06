import xml.etree.ElementTree as ET
import json

def parseQuestion(question):

		tree = ET.parse('Resources/question_' + question + '.xml') # e.g. question_10940477.xml
		root = tree.getroot()

		quesId = root.attrib['identifier']
		crap = "{http://www.imsglobal.org/xsd/imsqti_v2p1}"

		#responseDeclaration contains the answer
		ans = root.find(crap+"responseDeclaration")[0][0].text
		ansIndex = int(list(ans)[-1])

		#itemBody contains the choiceInteraction and modalFeedback
		itemBody = root.find(crap+"itemBody")[0]

		# gets the list of question prompts
		prompts = list(list(itemBody)[0])[0]
		promptVals = list()
		for val in prompts:
			promptVals.append(val.find(crap + 'div').text)
		#print promptVals[-1]

		# get all question choices into a list
		choices = itemBody.findall(crap+'simpleChoice')
		choiceVals = list()
		for val in choices:
			choiceVals.append(val.find(crap + 'div').text)
		#print choiceVals

		answer = choiceVals[ansIndex]
		#print answer

		# gets the appropriate feedback for question
		modalFeedback = root.find(crap+"modalFeedback")[0]
		feedback = ""
		for line in modalFeedback.itertext():
			feedback = feedback + line
		feedback = feedback.replace('\n', ' ').replace('\r', '')
		feedback = ' '.join(feedback.split())
		#print feedback

		response = json.dumps({'quesId': quesId, 'answer': answer, 'feedback': feedback, 'promptVals': promptVals, 'choiceVals': choiceVals}, sort_keys=True, indent=4, separators=(',', ': '))
		print response
		'''with open(quesId + '.json', 'w') as f:
		     json.dump(response, f)'''
		return response