import hashlib
import datetime as date
import tkinter as tk
from tkinter import simpledialog, messagebox

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, date.datetime.now(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class BlockchainGUI:
    def __init__(self, root, blockchain):
        self.root = root
        self.root.title("Blockchain GUI")
        self.blockchain = blockchain

        self.create_widgets()
        self.display_chain()

    def create_widgets(self):
        self.add_block_button = tk.Button(self.root, text="Add Block", command=self.add_block, bg="lightblue", fg="black")
        self.add_block_button.pack(pady=10)

        self.chain_display = tk.Text(self.root, height=20, width=80, bg="white", fg="black", bd=2, relief="solid")
        self.chain_display.pack(pady=10)

    def display_chain(self):
        self.chain_display.delete(1.0, tk.END)
        for block in self.blockchain.chain:
            self.chain_display.insert(tk.END, f"Block #{block.index}\n", "header")
            self.chain_display.insert(tk.END, f"Timestamp: {block.timestamp}\n")
            self.chain_display.insert(tk.END, f"Data: {block.data}\n")
            self.chain_display.insert(tk.END, f"Hash: {block.hash}\n")
            self.chain_display.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            self.chain_display.insert(tk.END, "\n")

    def add_block(self):
        data = simpledialog.askstring("Input", "Enter block data:")
        if data:
            self.blockchain.add_block(data)
            self.display_chain()
            if self.blockchain.is_valid():
                messagebox.showinfo("Blockchain Status", "Block added successfully and blockchain is valid.")
            else:
                messagebox.showerror("Blockchain Status", "Blockchain is invalid.")


blockchain = Blockchain()
root = tk.Tk()
gui = BlockchainGUI(root, blockchain)
root.configure(bg="lightgray")
root.mainloop()
