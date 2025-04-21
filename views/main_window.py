import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
from typing import Optional, Callable

from models.family_tree import FamilyTree
from views.person_dialogue import PersonDialogue
from controllers.app_controller import AppController

class MainWindow:
    def __init__(Self, root: tk.Tk, controller: AppController):
        """Initialise the main window of the application"""
        self.root = root
        self.controller = controller

        # set window properties
        self.root.title("Family Tree Builder")
        self.root.geometry("1200x800")

        # create menu bar
        self._create_menu_bar()

        # create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=true)

        # create toolbar
        self._create_toolbar()

        # create status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tkl.BOTTOM, fill=tk.X)

        # create content area with notebook for different views
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # tree view tab
        self.tree_view_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tree_view_frame, text="Tree View")

        # list view tab
        self.tree_view_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.list_view_Frame, text="List View")
        self._setup_list_view()

        # timeline view tab
        self.timeline_view_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.timeline_view_frame, text="Timeline")

        # update status
        self.set_status("Ready")
    
    def _create_menu_bar(self):
        """Create the application menu bar"""
        self.menu_bar = tk.Menu(self.root)

        # file menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New Family Tree", command=self.controller.new_family_tree)
        file_menu.add_command(label="Open...", command=self.controller.open_family_tree)
        file_menu.add_command(label="Save", command=self.controller.save_family_tree)
        file_menu.add_command(label="Save As...", command=self.controller.save_family_tree_as)
        file_menu.add_separator()
        file_menu.add_command(label="Export as Image...", command=self.controller.export_as_image)
        file_menu.add_command(label="Print...", command=self.controller.print_tree)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Add Person...", command=self.controller.add_person)
        edit_menu.add_command(label="Add Relationship...", command=self.controller.add_relationship)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # View menu
        view_menu = tk.Menu(self.menu_bar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.controller.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.controller.zoom_out)
        view_menu.add_command(label="Reset View", command=self.controller.reset_view)
        self.menu_bar.add_cascade(label="View", menu=view_menu)
        
        # Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=self.menu_bar)