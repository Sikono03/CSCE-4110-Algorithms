import tkinter as tk
from valid import validate
from lcs_solver import create_table
from reconstruct import get_lcs
from brute_force import brute_force_lcs
from substring import longest_common_substring
from measure import measure
from explain import explain_cell

BLUE = "#1E90FF"    # match
RED = "#FF6347"     # mismatch
ORANGE = "#FFA500"  # traceback
BRUTE_MAX = 14      # brute force is too slow above this length


class LCSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Longest Common Subsequence (LCS) Explorer")
        self.dp = None

        # Input row: two entry boxes and the buttons
        top = tk.Frame(root, padx=10, pady=10)
        top.pack()
        tk.Label(top, text="X:").pack(side="left")
        self.entry_x = tk.Entry(top, width=22)
        self.entry_x.pack(side="left", padx=5)
        tk.Label(top, text="Y:").pack(side="left")
        self.entry_y = tk.Entry(top, width=22)
        self.entry_y.pack(side="left", padx=5)
        tk.Button(top, text="Solve", command=self.solve).pack(side="left", padx=3)
        tk.Button(top, text="Next Step", command=self.next_step).pack(side="left", padx=3)
        tk.Button(top, text="Show Traceback", command=self.show_traceback).pack(side="left", padx=3)
        tk.Button(top, text="Run Checks", command=self.run_checks).pack(side="left", padx=3)

        self.error = tk.Label(root, text="", fg="red")
        self.error.pack()
        self.table_frame = tk.Frame(root, padx=10, pady=5)
        self.table_frame.pack()
        self.output = tk.Text(root, height=12, width=80)
        self.output.pack(padx=10, pady=10)

    # Add a line to the output box
    def log(self, text, clear=False):
        if clear:
            self.output.delete("1.0", "end")
        self.output.insert("end", text + "\n")
        self.output.see("end")

    # Check the input, build the table, and draw it empty
    def solve(self):
        x = self.entry_x.get().strip()
        y = self.entry_y.get().strip()
        ok, message = validate(x, y)
        self.error.config(text="" if ok else message)
        if not ok:
            return
        self.x = x
        self.y = y
        self.dp = create_table(x, y)
        self.lcs, self.path, self.matches = get_lcs(self.dp, x, y)
        # cells are revealed one at a time in this order
        self.order = [(i, j) for i in range(1, len(x) + 1) for j in range(1, len(y) + 1)]
        self.step = 0
        self.draw_table()
        self.log("Click Next Step to compute one cell at a time.", clear=True)

    # One label per cell, with the letters of Y on top and X down the side
    def draw_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.cells = {}
        for j, letter in enumerate(self.y, start=1):
            tk.Label(self.table_frame, text=letter).grid(row=0, column=j + 1)
        for i, letter in enumerate(self.x, start=1):
            tk.Label(self.table_frame, text=letter).grid(row=i + 1, column=0)
        for i in range(len(self.x) + 1):
            for j in range(len(self.y) + 1):
                is_base = (i == 0 or j == 0)   # row 0 and column 0 are always 0
                cell = tk.Label(self.table_frame, width=3, relief="solid", fg="black",
                                text="0" if is_base else "",
                                bg="#e0e0e0" if is_base else "white")
                cell.grid(row=i + 1, column=j + 1)
                self.cells[(i, j)] = cell

    # Fill in the next cell and explain how it was computed
    def next_step(self, explain=True):
        if self.dp is None or self.step >= len(self.order):
            return
        i, j = self.order[self.step]
        self.step += 1
        is_match = self.x[i - 1] == self.y[j - 1]
        self.cells[(i, j)].config(text=str(self.dp[i][j]), bg=BLUE if is_match else RED)
        if explain:
            self.log(explain_cell(self.dp, self.x, self.y, i, j))

    # Fill in any remaining cells, color the path, and show the answer
    def show_traceback(self):
        if self.dp is None:
            self.error.config(text="Click Solve first")
            return
        while self.step < len(self.order):
            self.next_step(explain=False)
        for cell in self.path:
            self.cells[cell].config(bg=ORANGE)
        positions = ", ".join(f"x[{i}]=y[{j}]={self.x[i - 1]}" for i, j in self.matches)
        self.log(f"\nLCS length: {self.dp[len(self.x)][len(self.y)]}\n"
                 f"One LCS: {self.lcs}\n"
                 f"Matched positions: {positions}")

    # Brute-force check, substring comparison, and timing
    def run_checks(self):
        if self.dp is None:
            self.error.config(text="Click Solve first")
            return
        length = self.dp[len(self.x)][len(self.y)]
        if max(len(self.x), len(self.y)) <= BRUTE_MAX:
            brute = brute_force_lcs(self.x, self.y)
            result = "MATCH" if brute == length else "MISMATCH"
            self.log(f"\nBrute force: {brute}, DP: {length} -> {result}")
        else:
            self.log(f"\nBrute force skipped: strings longer than {BRUTE_MAX} are too slow.")
        sub_len, sub = longest_common_substring(self.x, self.y)
        self.log(f"LCS length {length} vs longest common substring length {sub_len} ({sub})")
        self.log("\nTiming (n, cells, seconds):")
        for n, cells, seconds in measure([100, 200, 400, 800]):
            self.log(f"  {n:>4} {cells:>8} {seconds:.4f}")


if __name__ == "__main__":
    root = tk.Tk()
    LCSApp(root)
    root.mainloop()