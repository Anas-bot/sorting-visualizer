import pygame
import random
pygame.font.init()

class Display:
    pygame.init()
    display_width = 1000
    display_height = 1000
    screen = pygame.display.set_mode((display_width, display_height))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("SORTING ALGORITHMS VISUALIZER")
    clock = pygame.time.Clock()
    fps = 60
    delay = 50
    game_menu = pygame.surface.Surface((600, 60))


    @staticmethod
    def draw_lines(rects_dimensions, index):
        pygame.draw.rect(Display.screen, (0, 0, 0),
                         pygame.Rect(rects_dimensions[index]["left"], 0, Rect.rect_width,
                                     Display.display_height))
class Rect:
    base_rect_height = 8
    rect_width = 10
    distance_rect = 12
    rects_dimensions = {}

class CollectData:
    # def __init__(self):
    #     self.array = self.random_list()
    @staticmethod
    def compare_numbers(array, base):
        increase_dict = {}
        array_copy = array.copy()
        for num in array_copy:
            increase = num - base
            increase_percentage = (increase / base) * 100
            increase_dict[num] = increase_percentage

        return increase_dict

    @staticmethod
    def random_list():
        random.seed("seed")
        array = [i * 3 for i in range(1, 83)]
        random.shuffle(array)
        return array

    array = random_list.__func__()

    def collect_data(self, shuffle = None):
        if shuffle:
            random.shuffle(self.array)
        increase_dict = self.compare_numbers(self.array, min(self.array))
        distance_increase = 0
        for key in increase_dict:
            height = Rect.base_rect_height + (Rect.base_rect_height * (increase_dict[key]/100))
            left = 10 + distance_increase
            top = Display.display_height - height
            Rect.rects_dimensions[key] = {"left": left, "top": top, "height": height}
            distance_increase += Rect.distance_rect
        return Rect.rects_dimensions

class Visualize(CollectData):
    def __init__(self):
        # super().__init__()
        # self.array_copy = self.array.copy()
        self.rects_dimensions = CollectData().collect_data()
    @staticmethod
    def draw(algo_used = None):
        pygame.draw.rect(Display.screen, (255, 255, 255), pygame.Rect(0, 0, 1000, 94))
        fnt = pygame.font.SysFont("comicsans", 30)
        fnt1 = pygame.font.SysFont("comicsans", 20)
        # Text should be rendered
        txt = fnt.render("PRESS"
                            " 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0))
         # Position where text is placed
        Display.screen.blit(txt, (20, 20))
        txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.",
                              1, (0, 0, 0))
        Display.screen.blit(txt1, (20, 40))
        if algo_used:
            txt2 = fnt1.render("ALGORITHM USED: "
                                   f"{algo_used}", 1, (0, 0, 0))
        else:
            txt2 = fnt1.render("ALGORITHM USED: "
                               "", 1, (0, 0, 0))
        Display.screen.blit(txt2, (550, 60))
        txt3 = fnt.render("PRESS 'L' TO CHANGE THE ALGORITHM.", 1, (0, 0, 0))
        Display.screen.blit(txt3, (550, 20))
        pygame.draw.line(Display.screen, (0, 0, 0),
                             (0, 95), (1000, 95), 6)

    def draw_rects(self, rects_dimensions, shuffle = None):
        if shuffle:
            rects_dimensions = CollectData().collect_data(shuffle = True)
            for num in self.array:
                pygame.draw.rect(Display.screen, (0, 0, 0),
                                 pygame.Rect(rects_dimensions[num]["left"], rects_dimensions[num]["top"],
                                             Rect.rect_width, rects_dimensions[num]["height"]))
        else:
            for num in self.array:
                pygame.draw.rect(Display.screen, (0, 0, 0),
                                 pygame.Rect(rects_dimensions[num]["left"], rects_dimensions[num]["top"],
                                             Rect.rect_width, rects_dimensions[num]["height"]))
    @staticmethod
    def draw_black_lines(rects_dimensions, element):
        pygame.draw.rect(Display.screen, (255, 255, 255),
                         pygame.Rect(rects_dimensions[element]["left"], 100,
                                     Rect.rect_width, Display.display_height - 100))
    @staticmethod
    def draw_colors(rects_dimensions, element):
        pygame.draw.rect(Display.screen, (0, 255, 0),
                         pygame.Rect(rects_dimensions[element]["left"], rects_dimensions[element]["top"],
                                     Rect.rect_width, rects_dimensions[element]["height"]))
        pygame.display.flip()

        pygame.draw.rect(Display.screen, (0, 0, 0),
                         pygame.Rect(rects_dimensions[element]["left"], rects_dimensions[element]["top"],
                                     Rect.rect_width, rects_dimensions[element]["height"]))

    def bubble_sort(self):
        array_sorted = False
        indexing_length = len(self.array) - 1
        while not array_sorted:
            array_sorted = True
            for i in range(0, indexing_length):
                if self.array[i] > self.array[i + 1]:
                    array_sorted = False
                    self.draw_black_lines(self.rects_dimensions, self.array[i])
                    # pygame.draw.rect(Display.screen, (255, 255, 255)    ,
                    #                  pygame.Rect(self.rects_dimensions[self.array[i]]["left"], 0, Rect.rect_width,
                    #                              Display.display_height))
                    self.rects_dimensions[self.array[i]]["left"], self.rects_dimensions[self.array[i + 1]]["left"] = \
                        self.rects_dimensions[self.array[i + 1]]["left"], self.rects_dimensions[self.array[i]]["left"]
                    self.draw_rects(self.rects_dimensions)
                    pygame.display.flip()
                    pygame.time.delay(50)
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]

    def partition(self, sequence, head, tail, rects_dimensions):
        border = head
        pivot = sequence[tail]
        for j in range(head, tail):
            if sequence[j] < pivot:
                self.draw_black_lines(self.rects_dimensions, sequence[border])

                rects_dimensions[sequence[border]]["left"], rects_dimensions[sequence[j]]["left"] = \
                    rects_dimensions[sequence[j]]["left"], rects_dimensions[sequence[border]]["left"]
                self.draw_rects(rects_dimensions)
                sequence[border], sequence[j] = sequence[j], sequence[border]
                pygame.display.flip()
                pygame.time.delay(50)

                border += 1

        self.draw_black_lines(self.rects_dimensions, sequence[border])

        rects_dimensions[sequence[border]]["left"], rects_dimensions[sequence[tail]]["left"] = \
            rects_dimensions[sequence[tail]]["left"], rects_dimensions[sequence[border]]["left"]
        self.draw_rects(rects_dimensions)
        pygame.display.flip()
        pygame.time.delay(50)
        sequence[border], sequence[tail] = sequence[tail], sequence[border]
        return border

    def quick_sort_adaptation(self, sequence, head, tail, rects_dimensions):
        if head < tail:
            partition_index = self.partition(sequence, head, tail, rects_dimensions)
            self.quick_sort_adaptation(sequence, head, partition_index - 1, rects_dimensions)  # left
            self.quick_sort_adaptation(sequence, partition_index + 1, tail, rects_dimensions)  # right

        return sequence

    def merge_sort(self, array, rects_dimensions):

        if len(array) > 1:
            left_array = array[:len(array) // 2]
            right_array = array[len(array) // 2:]

            self.merge_sort(left_array,rects_dimensions)
            self.merge_sort(right_array, rects_dimensions)

            temp = []
            for element in array:
                temp.append(element)

            i = 0
            j = 0
            k = 0  # merged array index

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    self.draw_black_lines(self.rects_dimensions, array[k])
                    pygame.time.delay(10)
                    pygame.draw.rect(Display.screen, (0, 0, 0), pygame.Rect(rects_dimensions[array[k]]["left"], rects_dimensions[left_array[i]]["top"],
                                                                            Rect.rect_width, rects_dimensions[left_array[i]]["height"]))
                    pygame.display.flip()
                    array[k] = left_array[i]
                    i += 1
                else:
                    self.draw_black_lines(self.rects_dimensions, array[k])

                    pygame.time.delay(10)
                    pygame.draw.rect(Display.screen, (0, 0, 0),
                                     pygame.Rect(rects_dimensions[array[k]]["left"], rects_dimensions[right_array[j]]["top"],
                                                 Rect.rect_width, rects_dimensions[right_array[j]]["height"]))
                    pygame.display.flip()
                    array[k] = right_array[j]

                    j += 1


                k += 1
            while i < len(left_array):
                self.draw_black_lines(self.rects_dimensions, array[k])

                pygame.time.delay(10)
                pygame.draw.rect(Display.screen, (0, 0, 0),
                                 pygame.Rect(rects_dimensions[array[k]]["left"], rects_dimensions[left_array[i]]["top"],
                                             Rect.rect_width, rects_dimensions[left_array[i]]["height"]))
                pygame.display.flip()
                array[k] = left_array[i]

                i += 1
                k += 1

            while j < len(right_array):
                self.draw_black_lines(self.rects_dimensions, array[k])

                pygame.time.delay(10)
                pygame.draw.rect(Display.screen, (0, 0, 0),

                                 pygame.Rect(rects_dimensions[array[k]]["left"], rects_dimensions[right_array[j]]["top"],
                                             Rect.rect_width, rects_dimensions[right_array[j]]["height"]))
                pygame.display.flip()
                array[k] = right_array[j]
                j += 1
                k += 1

    def start_sorting(self, algorithm):
        if algorithm == "MERGE SORT":
            self.merge_sort(self.array, self.rects_dimensions)
        elif algorithm == "QUICK SORT":
            self.quick_sort_adaptation(self.array, 0, len(self.array) - 1, self.rects_dimensions)
        else:
            self.bubble_sort()
    def visualize(self):
        running = True
        self.draw()
        self.draw_rects(self.rects_dimensions, shuffle = False)
        i = 0
        algorithm = ["MERGE SORT", "QUICK SORT", "BUBBLE SORT"]
        # self.merge_sort(self.array, self.rects_dimensions)
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.draw.rect(Display.screen, (255, 255, 255), pygame.Rect(0, 100, Display.display_width, Display.display_height - 100))
                        pygame.display.flip()
                        self.draw_rects(self.rects_dimensions, shuffle = True)
                    if event.key == pygame.K_l:
                        if i == 3:
                            i = 0
                        current_algorithm = algorithm[i]
                        self.draw(algo_used= current_algorithm)
                        i += 1
                    if event.key == pygame.K_RETURN:
                        self.start_sorting(algorithm[i - 1])

            # self.draw()
            pygame.display.flip()
            Display.clock.tick(60)

if __name__ == "__main__":
    Visualize().visualize()