import base64
from xmlrpc.client import ServerProxy

def send_file(server_host, server_port, file_path):
    """
    Sends a file to the server by encoding it in base64.
    """
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encoded_file = base64.b64encode(file_data).decode('utf-8')
        
        server_url = f"http://{server_host}:{server_port}/"
        proxy = ServerProxy(server_url)
        
        file_name = file_path.split('/')[-1]  # Extract file name from path
        response = proxy.receive_file(encoded_file, file_name)
        
        print(response)
    except Exception as e:
        print(f"Error sending file: {e}")

if __name__ == "__main__":
    send_file("192.168.12.253", 6969, "transferfile.txt")
