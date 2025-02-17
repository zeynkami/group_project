# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:10:08 2025

@author: haoooyu
"""
import tkinter as tk

class Calculator:
    def __init__(self,):
        self.root = tk.Tk()
        self.root.title("CACULATOR")
        
        #create entry
        self.entry = tk.Entry(self.root, width=30, font=("Arial", 20), borderwidth=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        #create button
        self.button = self.build_button()
        
        #lunch the window
        self.root.mainloop()
        
    #append something which is pressed by users to the entry
    def append_entry(self,text):
        current_text = self.entry.get()
        
        #prevent adding ")"before"("
        if text == ")" and current_text.count("(") <= current_text.count(")"):
            return
        
        #ensure every numbers only have one "."
        if current_text and text == "." and "." in current_text.split()[-1]:
            return
        
        #add the text into the entry
        self.entry.insert(tk.END, text)
        
    def scientific_operate(self, operator):
        current_text = self.entry.get()
        
        try:
        
        #other group member's part
        
        #it will delete the text in entry and only display result
        self.entry.delete(0.tk.END)
        self.entry.insert(tk.END, result)
        
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            

    def operate(self):
        current_text = self.entry.get()
        try:
            
            #other group member's part
            
        #it will delete the text in entry and only display result
        self.entry.delete(0.tk.END)
        self.entry.insert(tk.END, result)
        
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            
    #clean the entry when users press "AC"
    def clean_entry(self):
        self.entry.delete(0, tk.END)
        
    #delete the last character when users press "delete"
    def delete_last_character(self):
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text)-1)
        
    #build the button. while pressing the button, call the function
    def build_button(self):
        button_text = [
                      ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2),("square", 1, 3),
                      ("arcsin", 2, 0), ("arccos", 2, 1), ("arctan", 2, 2), ("sqrt", 2, 3),
                      ("AC", 3, 0), ("(", 3, 1), (")", 3, 2), ("/", 3, 3),
                      ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
                      ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3),
                      ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
                      ("delete", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3)
                      ]
        basic_text = ["1" , "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "(", ")", "/", "*", "-", "+"]
        scientific_text = ["sin", "cos", "tan", "square", "arcsin", "arccos", "arctan", "sqrt"]
        for text, row, col in button_text:
            if text in basic_text:
                button = tk.Button(self.root, text = text, width = 6, height = 2, command = lambda t = text: self.append_entry(t))
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            elif text in scientific_text:
                button = tk.Button(self.root, text = text, width = 6, height = 2, command = lambda operator = text: self.scientific_operate(operator))
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            elif text == "AC":
                button = tk.Button(self.root, text = text, width = 6, height = 2, 
                                   fg = "red",
                                   command = self.clean_entry)
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            elif text == "delete":
                button = tk.Button(self.root, text = text, width = 6, height = 2, 
                                   fg = "red",
                                   command = self.delete_last_character)
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            elif text == "=":
                button = tk.Button(self.root, text = text, width = 6, height = 2,
                                   command = self.operate)
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

Calculator()