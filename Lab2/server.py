from xmlrpc.server import SimpleXMLRPCServer
import base64

def receive_file(encoded_file, file_name):
    """
    Receives a file from the client as a base64-encoded string and saves it to the server.
    """
    try:
        file_data = base64.b64decode(encoded_file)
        with open(file_name, 'wb') as file:
            file.write(file_data)
        print(f"File '{file_name}' received and saved successfully.")
        return "File received successfully"
    except Exception as e:
        print(f"Error receiving file: {e}")
        return str(e)

def start_rpc_server(host='0.0.0.0', port=6969):
    """
    Starts the RPC server to receive files.
    """
    server = SimpleXMLRPCServer((host, port))
    print(f"RPC Server listening on {host}:{port}...")
    server.register_function(receive_file, "receive_file")
    server.serve_forever()

if __name__ == "__main__":
    start_rpc_server()
