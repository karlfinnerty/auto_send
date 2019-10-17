from gui_send import GUISender
import sys

def main():
	sender = GUISender()
	receivers = sender.read_recievers(sys.argv[1])
	print(receivers)

if __name__ == '__main__':
	main()