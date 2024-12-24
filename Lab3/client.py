from mpi4py import MPI

def send_file(file_path):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 1:  # Client role
        print("Client reading file and sending data...")
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()

            comm.send(file_data, dest=0, tag=11)  # Send file data to server
            print("File sent successfully!")
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Exiting.")

if __name__ == "__main__":
    send_file("transferfile.txt")
