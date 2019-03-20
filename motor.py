import pygame
import random
import time

pygame.init()


white=(250,250,250)
red=(250,0,0)
bright_red=(200,0,0)
black=(0,0,0)
green=(0,250,0)
bright_green=(0,200,0)
blue=(75,0,250)
yello=(250,250,0)

game=pygame.display.set_mode((500,800))

pygame.display.set_caption("MOTOR BAZY")

clock=pygame.time.Clock()


pygame.mixer.music.load("world-m.ogg")
crash_sound=pygame.mixer.Sound("lose-m.wav")




def crash():
    pygame.mixer.music.stop()

    pygame.mixer.Sound.play(crash_sound)


    font=pygame.font.SysFont(None,70)
    text=font.render("YOU CRASHED",True,black)
    game.blit(text,(100,300))

    score=0
    

    pygame.display.update()
    time.sleep(4)
    gameloop()

    
    






def menu():

    heart=0
    
    while True:
        game.fill(white)

 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        a=mouse[0]
        b=mouse[1]
        c=click[0]




        font=pygame.font.SysFont(None,70)
        text=font.render("LET`S PLAY",True,black)
        game.blit(text,(10,200))


        pygame.draw.rect(game,green,[100,500,50,50])

        font=pygame.font.SysFont(None,20)
        text=font.render("PLAY!!",True,black)
        game.blit(text,(110,520))



        
        if a>100 and a<150 and b>500 and b<550 :
            pygame.draw.rect(game,bright_green,[100,500,50,50])

            font=pygame.font.SysFont(None,20)
            text=font.render("PLAY!!",True,black)
            game.blit(text,(110,520))

            if c==1:
                gameloop()






        pygame.draw.rect(game,red,[350,500,50,50])


        font=pygame.font.SysFont(None,20)
        text=font.render("QUIT",True,black)
        game.blit(text,(360,520))


        
        if a>350 and a<400 and b>500 and b<550 :
            pygame.draw.rect(game,bright_red,[350,500,50,50])


            font=pygame.font.SysFont(None,20)
            text=font.render("QUIT",True,black)
            game.blit(text,(360,520))


            if c==1:
                pygame.quit()
                quit()












        pygame.display.update()










def gameloop():

    pygame.mixer.music.play(-1)

    motorx=100
    motory=500
    speed_motory=0

    instagram_x1=850
    instagram_x2=5000
    instagram_width1=48
    instagram_width2=48
    speed_instagramx=-1


    
    

    score=0
    
    
    
    

    while True:
        game.fill(blue)


        car=game.blit(pygame.image.load("Bug.png"),(motorx,motory))



        pygame.draw.rect(game,green,[0,548,500,300])



        font=pygame.font.SysFont(None,25)
        text=font.render("score :"+str(score),True,black)
        game.blit(text,(10,10))









        pygame.draw.rect(game,yello,[instagram_x2,500,instagram_width1,48])

        instagram_x2+=speed_instagramx
        

        if instagram_x2<-instagram_width2:
            instagram_x2=600
            instagram_width1=random.randrange(10,48)






        pygame.draw.rect(game,red,[instagram_x1,500,instagram_width2,48])


        instagram_x1+=speed_instagramx


        if instagram_x1<-instagram_width1:
            instagram_x1=500
            instagram_width2=random.randrange(10,48)







        speed_instagramx-=0.00005





        




        




        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if motory==500:
                        speed_motory=-1
                    if motory<=380:
                        speed_motory=1

            #if event.type==pygame.KEYUP:
                #if event.key==pygame.K_UP:
                #    if motory>405:
                #       speed_motory=-1
                #  if motory<=405:
                #     speed_motory=1
                    #if motory>500:
                    #   speed_motory=0


        if motory<380:
            speed_motory=1
        
        if motory>500:
            speed_motory=0
            motory=500

        motory=speed_motory+motory







        if motorx+33>instagram_x1 and motorx+15<instagram_x1+instagram_width1 and motory+48>500 :
            score-=5
            instagram_x1=600


        if motorx+44>instagram_x2 and motorx+4<instagram_x2+instagram_width2 and motory+44>=500 :
            score+=2
            instagram_x2=700

        


        if score<0:
            crash()




        clock.tick(900)

        pygame.display.update()








menu()

pygame.quit()
quit()