
room=str(input())
if room == 'треугольник':
        side_triangle_1=int(input())
        side_triangle_2=int(input())
        side_triangle_3=int(input())
        P_triangle=(side_triangle_1+side_triangle_2+side_triangle_3)/2
        S_triangle=(P_triangle*(P_triangle-side_triangle_1)*(P_triangle-side_triangle_2)*(P_triangle-side_triangle_3))**(0.5)
        print(S_triangle)
elif room == 'прямоугольник':
        side_rec_1=int(input())
        side_rec_2=int(input())
        S_rec=side_rec_1*side_rec_2
        print(S_rec)
elif room == 'круг':
        r=int(input())
        pidar=3.14 
        S_circle=pidar*(r*r)
        print(S_circle)
