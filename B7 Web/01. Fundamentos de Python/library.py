posts = [    {"title": "DragonBall Z", "author": "Akira Toriyama"},    
             {"title": "Yu Yu Hakusho", "author": "Yoshihiro Togashi"},
             {"title": "Naruto Shippuden", "author": "Masashi Kishimoto"}
]   

for post in posts:    
    print(post["title"])    
    print(f"Autor: {post["author"]}")    
    print("------------------")