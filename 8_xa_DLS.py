import tkinter as tk
import random
import copy
from PIL import Image, ImageTk
from collections import deque

class eight_xa:
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        self.n = 8

        self.frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_left.grid(row=0, column=0, padx=10, pady=5)

        self.frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_right.grid(row=0, column=1, padx=10, pady=5)

        white_xa = Image.open("./whiteX.png").resize((60, 60))
        black_xa = Image.open("./blackX.png").resize((60, 60))
        self.whiteX = ImageTk.PhotoImage(white_xa)
        self.blackX = ImageTk.PhotoImage(black_xa)
        
        self.img_null = tk.PhotoImage(width=1, height=1)
        
        #Vị trí quân xe mục tiêu cần đạt được
        self.node_goal = []
        _ = [col for col in range(self.n)]
        random.shuffle(_)
        for i in range(self.n):
            j = _.pop()
            self.node_goal.append((i, j))
            
        #Đặt xe vào ma trận với các tọa độ từ node
        node = self.set_xa_DLS(self.n - 1)
        self.pos_xa = [[0] * self.n for _ in range(self.n)]
        for x, y in node:
            self.pos_xa[x][y] = 1

        #Vẽ lên giao diện
        self.buttons_left = self.create_widget(self.frame_left, False)
        self.buttons_right = self.create_widget(self.frame_right, True)
        
    def create_widget(self, frame, draw_xa):
        buttons = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                
                if draw_xa and self.pos_xa[i][j] == 1:
                    img = self.whiteX if color == "black" else self.blackX
                else:
                    img = self.img_null
                
                btn = tk.Button(frame, image=img, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0)
                    
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        
        return buttons
    
    def set_xa_DLS(self, limit):
        x, y = self.node_goal[0]
        node = [(x, y)]
        return self.recursive_DLS(node, limit)
    
    #Hàm đặt xe bằng DLS
    def recursive_DLS(self, node, limit):
        if self.check_goal(node):
            return node
        elif limit == 0:
            return "cutoff"
        else:
            cutoff_occurred = False
            x = node[len(node) - 1][0] + 1
            for y in range(self.n):
                child = self.child_node(node, x, y)
                result = self.recursive_DLS(child, limit - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != False:
                    return result
            if cutoff_occurred:
                return "cutoff"
            else:
                return False
    
    def check_goal(self, node):     #Kiểm tra điều kiện đạt goal: số lượng đã đủ và ko 2 quân nào khắc nhau
        if node == self.node_goal:
            return True
        return False
    
    def child_node(self, node, x, y):       #Sinh ra nhánh con child
        child = []
        child = copy.deepcopy(node)
        child.append((x, y))
        return child  

if __name__ == "__main__":
    root = tk.Tk()
    game = eight_xa(root)
    root.mainloop()