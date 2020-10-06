from socket import *
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = 'smtp.gmail.com'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfrom = 'MAIL FROM: <sh5827@nyu.edu>\r\n.'
    clientSocket.send(mailfrom.encode())
    recv2 = clientSocket.recv(1024)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptto = 'RCPT TO: <alexrobin2000@gmail.com>\r\n'
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send('SUBJECT: Greeting To you!\r\n'.encode())
    clientSocket.send('test again'.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitcommand = 'QUIT\r\n'
    clientSocket.send(quitcommand.encode())
    recv6 = clientSocket.recv(1024)
    # Fill in end


if __name__ == '__main__':
    smtp_client(587, 'smtp.gmail.com')
