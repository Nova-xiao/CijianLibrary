# -*- coding: UTF-8 -*- 
import sys 
import os
import pathlib


file_cont_format = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>此间纪念馆</title>
	  <link href="css/index.css" rel="stylesheet">
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.4.1.css" rel="stylesheet">
	  
	 <script>
		 window.onload = function () {{
			var current = 0;
			var papers = document.querySelectorAll('.paper');
			document.querySelector('#right-btn').addEventListener('click', function () {{
				if(current >= papers.length){{
					return
				}}
				var curentPapper = papers[current];
				curentPapper.classList.add('current');
				curentPapper.classList.add('flip');

				Array.from(papers).forEach(function (paper, index) {{
					if (index !== current) {{
						paper.classList.remove('current');
					}}
				}});

				current += 1;
			}});
			 
			document.querySelector("#left-btn").addEventListener("click", function(){{
				// current paper: current - 1
				// the previous current paper: current - 2
				
				if(current <= 0){{
					return
				}}
				current -= 1
				papers[current].classList.remove("flip")
				if(current <= 0){{
					return
				}}
				papers[current - 1].classList.add("current")
				
				Array.from(papers).forEach(function (paper, index) {{
					if (index !== current - 1) {{
						paper.classList.remove('current');
					}}
				}});
				
			}})
		}}

	 </script>
  </head>
	
	
  <body>

	<header>
	  <div class="jumbotron text-center" id="headerbg">
		<div class="col-12">
				  <h1>{big_header}</h1>
				  <p>{small_header}</p>
		</div>
	   </div>
	</header>
	  
	<div class="content">
		<button type="button" class="btn btn-dark" id="left-btn"><img src="images/left-arrow.png"></button>
			  
        <div class="fakebook"></div>
        <div class="book">
            {papers}  	
        </div>
			  
		<button type="button" class="btn btn-dark" id="right-btn"><img src="images/right-arrow.png"></button>  
    </div>
		
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
    <script src="js/jquery-3.4.1.min.js"></script> 
    <!-- Include all compiled plugins (below), or include individual files as needed --> 
    <script src="js/popper.min.js"></script> 
    <script src="js/bootstrap-4.4.1.js"></script>
  </body> 

</html>
"""

papers_str_format = """
                <div class="paper">
					<div class="page front"><img src="{first}"></div>
					<div class="page back"><img src="{second}"></div>
				</div>

"""

file_name = input("输入文件名：")
header1_str=input("输入大标题：")
header2_str=input("输入小标题：")

img_folder_name=input("输入杂志图片文件夹名：")

pwd_path = pathlib.Path().resolve()
img_folder = os.path.join(pwd_path, "images", img_folder_name)

if not os.path.exists(img_folder):
    print("文件夹不存在。")
    exit(1)

imgs = os.listdir(img_folder)
for img in imgs:
    if not img.endswith(".jpg"):
        imgs.remove(img)
imgs.sort()

imgs_length = len(imgs)
papers_str = ""

for i in range(0, imgs_length, 2):
    if (imgs_length - i )<2 :
        front_page = os.path.join("images/", img_folder_name+"/", imgs[i])
        this_paper = papers_str_format.format(first=front_page, second="END")
    else:
        front_page = os.path.join("images/", img_folder_name+"/", imgs[i])
        back_page = os.path.join("images/", img_folder_name+"/", imgs[i+1])
        this_paper = papers_str_format.format(first=front_page, second=back_page)
        if i == 0:
            this_paper = this_paper.replace("paper", "paper current")
    print(this_paper)
    papers_str = papers_str + this_paper


with open(file_name, "w", encoding="utf-8") as f:
    f.write(file_cont_format.format(big_header=header1_str, small_header=header2_str, papers=papers_str))



