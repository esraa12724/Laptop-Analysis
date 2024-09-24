# Laptop-Analysis



This dataset descripes the inventory of laptop store where they needed to know count of laptops are there and the details of each laptop and the company that produces it.

Credit
----------------------------
source dataset: https://www.kaggle.com/datasets/muhammetvarl/laptop-price/

preprocessing code: https://www.kaggle.com/code/owm4096/laptop-prices-eda-w-ml-models-91-8-high

Columns:
----------------------

Company: Laptop Manufacturer.

Product: Brand and Model.

TypeName: Laptop Type (Notebook, Ultrabook, Gaming, …etc).

Inches: Screen Size.

Ram: Total amount of RAM in laptop (GBs).

OS: Operating System installed.

Weight: Laptop Weight in kilograms.

Price_euros: Price of Laptop in Euros. (Target)

Screen: screen definition (Standard, Full HD, 4K Ultra HD, Quad HD+).

ScreenW: screen width (pixels).

ScreenH: screen height (pixels).

Touchscreen: whether or not the laptop has a touchscreen.

IPSpanel: whether or not the laptop has an IPSpanel.

RetinaDisplay: whether or not the laptop has retina display.

CPU_company

CPU_freq: frequency of laptop CPU (Hz).

CPU_model

PrimaryStorage: primary storage space (GB).

PrimaryStorageType: primary storage type (HDD, SSD, Flash Storage, Hybrid).

SecondaryStorage: secondary storage space if any (GB).

SecondaryStorageType: secondary storage type (HDD, SSD, Hybrid, None).

GPU_company

GPU_model

Formatting Issues
-----------------------------------------------------------------------------------

The dataset contained some issues in datatpes, Nulls, and I dealed with these issues using python.
ChatGPT Auto


During the preprocessing of the dataset, the following issues were identified and addressed:

1. Inconsistent Data Types
Columns affected: inches, cpu_freq, screenH

Solution:
Converted inches and cpu_freq to decimal values for consistency.
Converted screenH to a whole number (integer).


3. Missing Values
Columns affected: inches, cpu_freq, prices_euros, retinadisplay

Solution:
Replaced missing values in inches and cpu_freq with the mean of the respective columns.
Replaced missing values in prices_euros with the median.
Replaced missing values in retinadisplay with the mode.
