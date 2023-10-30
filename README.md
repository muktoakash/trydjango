# trydjango
Attempt at learning django, based on [Django lecture on freeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)

Time spent ~ 20 hours

# Apps Created
- blog
- courses
- pages
- products

# What I learned:
    - Project set up
    - sublime project created
    - Updated Product using CLI
    - Render Data from database model
    - Porduct Form initialized
    - Raw HTML form
    - Django model forms, Form widgets, Form validation methods
    - Initial values for forms, dynamic URL routing
    - Dynamic URL routing, Handle DoesNotExist, Delete and Confirm
    - List of db obj, dynamic linking, url reverse
    - Class Based Views: ListView, CreateView, DetailView, UpdateView, DeleteView
    - Function Based to Class Based: Raw List, Detail, Create, Update, Delete Views, Custom Mixin
    

# Relevant Files:

    ~src


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----        10/29/2023   3:00 AM                blog                                                                               
d-----        10/30/2023   3:30 PM                courses                                                                            
d-----         10/7/2023   1:36 PM                pages                                                                              
d-----        10/12/2023   2:44 PM                products                                                                           
d-----        10/12/2023   2:36 PM                templates                                                                          
d-----         9/15/2023  11:28 PM                trydjango                                                                          
-a----        10/30/2023   4:09 PM         143360 db.sqlite3                                                                         
-a----        10/30/2023   4:31 PM              0 files.txt                                                                          
-a----         10/4/2023   1:33 PM             57 git_config.txt                                                                     
-a----         9/15/2023   8:19 PM            687 manage.py                                                                          
-a----        10/30/2023   4:24 PM           4792 methods.txt                                                                        
-a----        10/30/2023   4:23 PM            822 requirements.txt                                                                   


    ~src\blog


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----        10/29/2023   3:44 AM                migrations                                                                         
d-----        10/29/2023   4:30 AM                templates                                                                          
d-----        10/29/2023   4:49 AM                __pycache__                                                                        
-a----        10/29/2023   2:55 AM            190 admin.py                                                                           
-a----        10/29/2023   2:39 AM            146 apps.py                                                                            
-a----        10/29/2023   3:20 AM            210 forms.py                                                                           
-a----        10/29/2023   4:21 AM            376 models.py                                                                          
-a----        10/29/2023   2:39 AM             63 tests.py                                                                           
-a----        10/29/2023   4:46 AM            582 urls.py                                                                            
-a----        10/29/2023   4:49 AM           1674 views.py                                                                           
-a----        10/29/2023   2:52 AM              0 __init__.py                                                                        


    ~src\blog\templates\articles


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
-a----        10/29/2023   4:03 AM            427 article_create.html                                                                
-a----        10/29/2023   5:00 AM            504 article_delete.html                                                                
-a----        10/29/2023   4:52 AM            180 article_detail.html                                                                
-a----        10/29/2023   4:33 AM            287 article_list.html                                                                  



    ~src\courses


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----        10/30/2023   3:06 PM                migrations                                                                         
d-----        10/30/2023   2:36 PM                templates                                                                          
d-----        10/30/2023   4:20 PM                __pycache__                                                                        
-a----        10/30/2023   3:09 PM            186 admin.py                                                                           
-a----        10/30/2023   2:33 PM            152 apps.py                                                                            
-a----        10/30/2023   3:44 PM            384 forms.py                                                                           
-a----        10/30/2023   3:00 PM            147 models.py                                                                          
-a----        10/30/2023   2:33 PM             63 tests.py                                                                           
-a----        10/30/2023   4:07 PM            780 urls.py                                                                            
-a----        10/30/2023   4:20 PM           5023 views.py                                                                           
-a----        10/30/2023   2:33 PM              0 __init__.py                                                                        

                                                                    

    ~src\courses\templates\courses


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
-a----        10/30/2023   2:54 PM            167 about.html                                                                         
-a----        10/30/2023   3:36 PM            236 course_create.html                                                                 
-a----        10/30/2023   4:08 PM            320 course_delete.html                                                                 
-a----        10/30/2023   3:09 PM            166 course_detail.html                                                                 
-a----        10/30/2023   3:16 PM            227 course_list.html                                                                   
-a----        10/30/2023   4:02 PM            295 course_update.html                                                                 


    ~src\pages


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----         10/7/2023   1:37 PM                migrations                                                                         
d-----         10/7/2023  10:33 PM                __pycache__                                                                        
-a----         10/7/2023   1:31 PM             66 admin.py                                                                           
-a----         10/7/2023   1:31 PM            148 apps.py                                                                            
-a----         10/7/2023   1:31 PM             60 models.py                                                                          
-a----         10/7/2023   1:31 PM             63 tests.py                                                                           
-a----         10/7/2023  10:33 PM            612 views.py                                                                           
-a----         10/7/2023   1:31 PM              0 __init__.py                                                                        


    ~src\products


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----         10/7/2023   1:20 PM                migrations                                                                         
d-----        10/26/2023   5:04 PM                __pycache__                                                                        
-a----         9/18/2023  11:45 AM            127 admin.py                                                                           
-a----         9/16/2023  11:14 PM            154 apps.py                                                                            
-a----        10/20/2023   1:22 PM           1201 forms.py                                                                           
-a----        10/26/2023   5:03 PM            476 models.py                                                                          
-a----         9/16/2023  11:14 PM             63 tests.py                                                                           
-a----        10/26/2023   4:58 PM           2418 views.py                                                                           
-a----         9/16/2023  11:14 PM              0 __init__.py                                                                        



    ~src\templates


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----        10/26/2023   4:52 PM                products                                                                           
-a----         10/7/2023  10:35 PM            492 about.html                                                                         
-a----         10/7/2023  10:01 PM            265 base.html                                                                          
-a----         10/7/2023   9:55 PM            131 contact.html                                                                       
-a----         10/7/2023   9:54 PM            137 home.html                                                                          
-a----         10/7/2023  10:01 PM             83 navbar.html                                                                        


    ~src\templates\products


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
-a----        10/12/2023   5:06 PM            255 detail.html                                                                        
-a----        10/14/2023   2:15 PM            375 product_create.html                                                                
-a----        10/30/2023   4:08 PM            264 product_delete.html                                                                
-a----        10/26/2023   5:01 PM            233 product_list.html                                                                  


    ~src\trydjango


Mode                 LastWriteTime         Length Name                                                                               
----                 -------------         ------ ----                                                                               
d-----        10/30/2023   2:52 PM                __pycache__                                                                        
-a----         9/15/2023   8:19 PM            411 asgi.py                                                                            
-a----        10/30/2023   2:52 PM           3473 settings.py                                                                        
-a----         9/15/2023  11:28 PM            219 trydjango.sublime-project                                                          
-a----        10/25/2023  11:10 AM         573257 trydjango.sublime-workspace                                                        
-a----        10/30/2023   2:49 PM           1574 urls.py                                                                            
-a----         9/15/2023   8:19 PM            411 wsgi.py                                                                            
-a----         9/15/2023   8:19 PM              0 __init__.py                                                                        
