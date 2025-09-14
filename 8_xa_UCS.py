import tkinter as tk
import random
import copy
import heapq
from PIL import Image, ImageTk
from collections import deque

class eight_queen:
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
        node_xa = self.set_xa_UCS()
        path = node_xa[2]
        cost = node_xa[0]
        self.pos_xa = [[0] * self.n for _ in range(self.n)]
        for x, y in path:
            self.pos_xa[x][y] = 1

        #Vẽ lên giao diện
        self.buttons_left = self.create_widget(self.frame_left, False)
        self.buttons_right = self.create_widget(self.frame_right, True)

        cost_txt = tk.Label(self.root, bg="lightgray", text=f"Chi phí: {cost}", font=("Arial", 15))
        cost_txt.grid(row=1, column=0, columnspan=2, pady=5)
        
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
    
    #Hàm đặt xe bằng UCS
    def set_xa_UCS(self):
        #Stack và các biến ban đầu
        frontier = []    #stack
        xst, yst = self.node_goal[0][0], self.node_goal[0][1]
        node = (1, (xst, yst), [(xst, yst)])     #(cost, tọa độ mới nhất, các tọa độ đặt xe)

        heapq.heappush(frontier, node)
        explored = []
        
        while frontier:
            node = heapq.heappop(frontier)
            if self.check_goal(node[2]):
                return node
            explored.append(node)
            cost = node[0]

            #Duyệt từng tọa độ x, y
            x = node[1][0] + 1
            for y in range(self.n):
                can_set = self.canSet(node[2], x, y)
                cost += 1
                if can_set:
                    child = self.child_node(node, cost, x, y)     #Tạo nhánh cây con child 
                    if child not in frontier and child not in explored:
                        heapq.heappush(frontier, child)
    
    def check_goal(self, node):     #Kiểm tra điều kiện đạt goal: trạng thái của node = tạo độ các quân xe đã được định sẵn
        if node == self.node_goal:
            return True
        return False
    
    def child_node(self, node, cost, x, y):       #Sinh ra nhánh con child
        path = node[2].copy()
        path.append((x, y))
        return (cost, (x, y), path)  
    
    def canSet(self, node, x, y):
        for node_x, node_y in node:     #Kiểm tra mỗi tọa độ x, y hiện tại có khắc quân cờ nào trong node ko
            if x == node_x or y == node_y:
                return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()