import sys
import smtplib, ssl

class GUISender():

	sender = sys.argv[1] #info@nandplinks

	def read_recipients(self, filename):
		recipients = []
		with open(filename, "r") as f:
			for line in f.readlines():
				tokens = line.split(":")
				entry = (tokens[0], tokens[1])
				recipients.append(entry)
			return recipients

	# def send_email(self, sender_address, reciever_address, message):
	# 	self.server.sendmail(sender_address, reciever_address, message)
	# 	print("<Sending email from {} to {}> \n with message: \n {}. \n".format(sender_address, reciever_address, message))


	def loop(self):
		try:
			recipients = self.read_recipients(sys.argv[2])
			print("Initializing smtp server...")

			password = SLogin().get_pass()
			server = smtplib.SMTP_SSL("smtp.gmail.com", SLogin().port, context = SLogin().context)
			server.login(self.sender, password)

			print("Sending Emails....")

			i = 0
			while i < len(recipients):
				message = "Hi {}, \n I'm sending you this email to let you know that your GUI card is available for collection in the pro shop. Feel free to call in any day from nine to five. \n Kind Regards, \n Karl Finnerty \n Narin & Portnoo Links".format(recipients[i][0])
				server.sendmail(self.sender, recipients[i][1], message) #send email from sender to reciever with message
				i += 1

			server.quit()

		except:
			with Exception as e:
				print(e)

class SLogin():

	port = 465
	context = ssl.create_default_context()

	def get_pass(self):
		password = input("Enter password: ")
		return password


def main():
	sender = GUISender()
	sender.loop()

if __name__ == '__main__':
	main()