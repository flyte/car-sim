

def draw_car(screen, car, pos, rotation):
    car = pygame.transform.rotate(car, rotation-180)
    screen.blit(bg, (0, 0))
    screen.blit(car, pos)
    pygame.display.flip()


def turn(screen, car, angle, origin):
    cx, cy = origin
    for i in range(angle + 1):
        ir = radians(i)
        x = cx + r * cos(ir)
        y = cy + r * sin(ir)
        draw_car(screen, car, (x, y), -i)
        sleep(0.01)

