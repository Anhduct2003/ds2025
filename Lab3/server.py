from mpi4py import MPI

def start_server(file_name="received_file.txt"):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:  # Server role
        print("Server waiting for file data...")
        file_data = comm.recv(source=1, tag=11)  # Receive file data from client
        print("File data received. Writing to file...")

        with open(file_name, "wb") as file:
            file.write(file_data)
        
        print(f"File '{file_name}' received successfully!")

if __name__ == "__main__":
    start_server()
