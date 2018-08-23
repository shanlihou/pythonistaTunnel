from ftplib import FTP
import os


class Tunnel(object):
    def __init__(self, ip, port=None):
        self.ip = ip
        self.port = port
        ftp = FTP()
        ftp.connect(self.ip)
        ftp.login('123')
        self.ftp = ftp
        self.fileList = []

    def fileInfoCB(self, fileInfo):
        infoList = fileInfo.split()
        fileName = infoList[-1]
        if not fileName.endswith('.py'):
            return

        self.fileList.append(fileName)
        return
        with open(fileName, 'wb') as fw:
            # downName = 'RETR ' + os.path.join(self.downPath, fileName)
            downName = 'RETR ' + fileName
            self.ftp.retrbinary(downName, fw)

    def test(self):
        self.downPath = r'python\pythonFunc\theirFTP'
        self.ftp.cwd(self.downPath)
        self.ftp.dir(self.fileInfoCB)
        for fileName in self.fileList:
            with open(fileName, 'wb') as fw:
                downName = 'RETR ' + fileName
                self.ftp.retrbinary(downName, fw.write)


if __name__ == '__main__':
    tunnel = Tunnel('192.168.16.67')
    tunnel.test()
