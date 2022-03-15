from ftplib import FTP
import os, pathlib, multiprocessing

# set the shapes_dir variable to the folder where you want
# to download your files to
script_dir = pathlib.Path(os.path.dirname(__file__))
shapes_dir = os.path.join(script_dir.parent,"data/shapes")

# remote dir - setting this to the TRACT shape files dir
remote_dir = "/geo/tiger/TIGER2020/TRACT"

class FTPDownloader:

    def __init__(self, server: str, user="anonymous", passwd="anonymous"):
        """ Creates an FTPDownloader object for paralell downloading of files
            from an FTP server

            Args:
                server (str): Hostname of server e.g. ftp2.census.gov
                user (str): username to log in wtth (defaults to 'anonymous')
                passwd (str): password to log in with (defaults to 'anonymous')

        """
        self._login = multiprocessing.Manager().dict()
        self._login['server'] = server
        self._login['user'] =  user
        self._login['passwd'] = passwd

    def list_remote_files(self, remote_dir: str):
        """Gets a list of files available for download at a remote ftp server

            Args:
                remote_dir (str): Folder to list on the remote server

            Returns:
                (list): A list of all the files available
        """
        ftp_client = FTP(host=self._login['server'], user=self._login['user'], passwd=self._login['passwd'])
        ftp_client.cwd(remote_dir)
        return ftp_client.nlst()

    def download(self, files: list, local_dir: pathlib.Path) -> None:
        ftp_client = FTP(host=self._login['server'], user=self._login['user'], passwd=self._login['passwd'])
        ftp_client.cwd(remote_dir)
        for file in files:
            local_filename = os.path.join(local_dir,file)
            print(f"Downloading {file} to {local_filename}")
            with open(local_filename, "wb") as local_file:
                ftp_client.retrbinary(f"RETR {file}", local_file.write)
        ftp_client.quit()

    @staticmethod
    def _split_list(to_split: list, size: int):
        k, m = divmod(len(to_split), size)
        return (to_split[i * k + min(i, m) : (i + 1) * k + min(i + 1, m) ] for i in range(size))

    def download_shape_files(self, remote_dir: str, local_dir: pathlib.Path, concurrent_workers=5) -> int:
        """Downloads all of the files from the ftp server folder to the local folder
        
            Args:
            remote_dir (str): The folder on the FTP server to download from
            local_dir (pathlib.Path): The local folder where you want files saved
            concurrent_workers (int): Number of paralell downloads to run (defaults to 5)
            
            Returns:
                (int): The number of files downloaded
        """
        # Create the local folder if it doesn't exist
        os.makedirs(local_dir, exist_ok=True)

        # get a list of all remote files
        remote_files = self.list_remote_files(remote_dir)

        # split the list evenly into multiple lists - one per worker
        split_list = list(FTPDownloader._split_list(remote_files, concurrent_workers))

        # Create a pool of workers and assign the task of downloading one of our
        # split lists to each worker - downloads will happen in parallell
        # hopefully this makes things go faster
        workers = []
        for i in range(len(split_list)):
            worker = multiprocessing.Process(target=self.download, args=(split_list[i],local_dir))
            workers.append(worker)
            worker.start()

        for worker in workers:
            worker.join()
            
        return(len(remote_files))

if __name__ == "__main__":
    downloader = FTPDownloader("ftp2.census.gov")
    count = downloader.download_shape_files(remote_dir, shapes_dir)
    print(f"Downloaded {count} files")
