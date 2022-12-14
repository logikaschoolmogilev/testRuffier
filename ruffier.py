''' Модуль для розрахунку результатів проби Руф'є.
 
Сума вимірювань пульсу у трьох спробах (до навантаження, одразу після та після короткого відпочинку)
в ідеалі має бути не більше 200 ударів на хвилину.
Ми пропонуємо дітям вимірювати свій пульс протягом 15 секунд,
і наводимо результат до ударів за хвилину множенням на 4:
   S = 4 * (P1 + P2 + P3)
Що далі цей результат від ідеальних 200 ударів, то гірше.
Традиційно таблиці даються для величини, поділеної на 10.
 
Індекс Руф'є  
   IR = (4 * (P1 + P2 + P3) - 200) / 10
оцінюється за таблицею відповідно до віку:
            7-8           9-10              11-12               13-14               15+ (тільки для підлітків!)
чуд.    6.4 і менше    4.9 і менше       3.4 і менше         1.9 і менше               0.4 і менше
добр.   6.5 - 11.9     5 - 10.4          3.5 - 8.9           2 - 7.4                   0.5 - 5.9
задов.  12 - 16.9      10.5 - 15.4       9 - 13.9            7.5 - 12.4                6 - 10.9
слабк.  17 - 20.9      15.5 - 19.4       14 - 17.9           12.5 - 16.4               11 - 14.9
незад.  21 і більше    19.5 і більше     18 і більше         16.5 і більше             15 і більше
 
для всіх вікових груп результат "незад." відстає від "слабкого" на 4,
той від "задовільного" на 5, а "добрий" від "чуд" - на 5.5
 
тому напишемо функцію ruffier_result(r_index, level), яка отримуватиме
розрахований індекс Руф'є та рівень "незадовільно" для віку тестованого, і віддавати результат
 
'''
table = {
   7:[21,17,12,6.5,6.4],
   9:[19.5,15.5,10.5,5,4.9],
   11:[18,14,9,3.5,3.4],
   13:[16.5,12.5,7.5,2,1.9],
   15:[15,11,6,0.5,0.4]
}
# тут задаються рядки, за допомогою яких викладено результат:
txt_index = "Ваш індекс Руф'є: "
txt_workheart = "Працездатність серця: "
txt_nodata = '''Немає даних для такого віку'''
txt_res = []
txt_res.append('''Низька. Терміново зверніться до лікаря!''')
txt_res.append('''Задовільна. Зверніться до лікаря!''')
txt_res.append('''Середня. Можливо, варто додатково обстежитись у лікаря.''')
txt_res.append('''Вище середнього''')
txt_res.append('''Висока''')
class Ruffier:
   def __init__(self):
      self.P1, self.P2, self.P3 = None, None, None
      self.NAME = None
      self.AGE = None
   def ruffier_index(self):
      index = (4 * (self.P1 + self.P2 + self.P3) - 200) / 10
      self.INDEX = index

   def neud_level(self):
      ''' варіанти з віком менше 7 і дорослим треба обробляти окремо,
      тут підбираємо рівень "незадовільно" тільки всередині таблиці:
      у віці 7 років "незад" - це індекс 21, далі кожні 2 роки він знижується на 1.5 до значення 15 в 15-16 років '''
      norm_age = (min(self.AGE, 15) - 7) // 2  # кожні 2 роки різниці від 7 років перетворюються на одиницю - аж до 15 років
      result = 21 - norm_age * 1.5 # множимо кожні 2 роки різниці на 1.5, так розподілені рівні у таблиці
      self.LEVEL = result

      
   def ruffier_result(self):
      ''' функція отримує індекс Руф'є та інтерпретує його,
      повертає рівень готовності: число від 0 до 4
      (що вище рівень готовності, то краще).  '''
      if self.INDEX >= self.LEVEL:
         self.TXT = txt_res[0]
      else:
         self.LEVEL = self.LEVEL - 4 # это не будет выполняться, если мы уже вернули ответ "неуд"
         if self.INDEX >= self.LEVEL:
            self.TXT = txt_res[1]
         else:
            self.LEVEL = self.LEVEL - 5 # аналогично, попадаем сюда, если уровень как минимум "уд"
            if self.INDEX >= self.LEVEL:
               self.TXT = txt_res[2]
            else:
               self.LEVEL = self.LEVEL - 5.5 # следующий уровень
               if self.INDEX >= self.LEVEL:
                  self.TXT = txt_res[3]
               else:
                  self.TXT = txt_res[4]

   def test(self):
      ''' цю функцію можна використовувати зовні модуля для підрахунків індексу Руф'є.
      Повертає готові тексти, які залишається намалювати у потрібному місці
      Використовує для текстів константи, задані на початку цього модуля. '''
      self.ruffier_index()
      self.neud_level()
      self.ruffier_result()
      if self.AGE <7:
         self.TXT = txt_nodata
      self.TXT = f"  {self.NAME }\n {txt_index}: {self.INDEX} \n {txt_workheart}: {self.TXT}"

   def test2(self):
      self.ruffier_index()
      if self.AGE >= 7:
         for age in table:
            if age == self.AGE or age+1 == self.AGE:
               for i in range(len(table[age])):
                  if i == 0:
                     if self.INDEX >= table[age][i]:
                        self.TXT =  txt_res[i]
                  elif self.INDEX >= table[age][i] and self.INDEX < table[age][i-1]:
                     self.TXT = txt_res[i]
      else:
         self.TXT = txt_nodata
      self.TXT = f" {self.NAME }\n {txt_index}: {self.INDEX} \n {txt_workheart}: {self.TXT}"

# rf = Ruffier()
# rf.NAME = "Maria"
# rf.AGE = 13
# rf.P1 = 23
# rf.P2 = 23
# rf.P3 = 23
# rf.test()
# print(rf.TXT)
# print("====================")
# rf.test2()
# print(rf.TXT)

