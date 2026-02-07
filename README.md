<div align="center">

# 🎓 Object-Oriented Programming - Mastery Journey

<img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="300"/>

### From OOP Fundamentals to Complete Game Development

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Learning](https://img.shields.io/badge/Type-Educational-orange?style=for-the-badge)](https://github.com)

[About](#-about) • [Learning Path](#-learning-progression) • [Projects](#-major-projects) • [Skills](#-skills-acquired)

---

</div>

## 📖 About

This repository chronicles my intensive journey through **Object-Oriented Programming** in Python. Over several days of focused learning, I progressed from basic class concepts to building complete, functional games with advanced OOP architectures.

**Learning Institution:** La Plateforme_  
**Duration:** 4-day intensive OOP bootcamp  
**Outcome:** 2 complete game projects + full OOP mastery

<div align="center">
  <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="400"/>
</div>

---

## 📚 Learning Progression

### 📅 Day 01 - OOP Fundamentals

**Focus:** Classes, Objects, and Methods

**Concepts Mastered:**
- ✅ Class definition with `class` keyword
- ✅ Constructor method `__init__()`
- ✅ Instance attributes and `self`
- ✅ Creating and calling methods
- ✅ Instance creation and manipulation
- ✅ String representation with `__str__()`

**Practice Project:** Product & VAT Calculator

**What I Built:**
A `Product` class managing:
- Product name and price (HT - without VAT)
- VAT percentage calculation
- Price with VAT computation
- Dynamic price and name modification
- Display methods with formatted output

**Key Learning:**
```python
# First class ever created
class Product:
    def __init__(self, name, priceHT, vat):
        self.name = name
        self.priceHT = priceHT
        self.vat = vat
    
    def CalculatePriceVAT(self):
        # Method that performs calculation
        return self.priceHT + (self.priceHT * self.vat / 100)
```

Understanding that objects are **instances with state and behavior**.

---

### 📅 Day 02 - Encapsulation & Data Privacy

**Focus:** Private Attributes, Getters/Setters, and Business Logic

**Concepts Mastered:**
- ✅ Private attributes with `__attribute`
- ✅ Getter and Setter methods
- ✅ Data validation and protection
- ✅ Enum for constants
- ✅ Private methods
- ✅ Dictionary management within classes

**Practice Project:** Restaurant Order Management System

**What I Built:**
A complete order system with:
- Order ID and dish tracking
- Status management (In Progress, Finished, Canceled)
- Dynamic dish addition with prices
- Automatic VAT calculation (20%)
- Protection against modifications on closed orders
- Total price computation

**Key Learning:**
```python
class Command:
    def __init__(self, idOrder):
        self.__idOrder = idOrder           # Private!
        self.__ordered_dishes = {}         # Hidden
        self.__order_statut = Status.IN_PROGRESS
    
    def add_dish(self, dish, price):
        # Only works if order is still in progress
        if self.__order_statut == Status.IN_PROGRESS:
            self.__ordered_dishes[dish] = price
```

Understanding that **encapsulation protects data integrity**.

---

### 📅 Day 03 - Composition & Object Relationships

**Focus:** Objects Containing Objects, References, and Shared State

**Concepts Mastered:**
- ✅ Composition (objects as attributes)
- ✅ Object references vs copies
- ✅ Modifying shared objects
- ✅ Complex object relationships
- ✅ Reference-based modifications

**Practice Projects:**

**City & Person System:**
- `City` class with population management
- `Person` class containing a `City` object reference
- Adding population updates the shared City object
- Demonstrating how multiple Persons can modify the same City

**Rectangle with Encapsulation:**
- Private length and width
- Complete getter/setter implementation
- Controlled attribute access

**Key Learning:**
```python
# Person HAS A City (composition)
class Person:
    def __init__(self, name, age, city_object):
        self.__city_object = city_object  # Reference!
    
    def addPerson(self, count):
        # Modifies the SAME city object
        current = self.__city_object.get_inhabitants()
        self.__city_object.set_inhabitants(current + count)
```

Understanding that **objects can share references and modify each other**.

---

### 📅 Day 04 - Advanced Concepts & Complete Projects

**Focus:** Inheritance, Game State Management, Complex Logic

**Concepts Mastered:**
- ✅ Class inheritance with `class Child(Parent)`
- ✅ Method inheritance and override
- ✅ `super()` for parent class access
- ✅ Complex game loops and state machines
- ✅ Random number generation in OOP
- ✅ Turn-based logic
- ✅ Win/loss condition checking

**Practice Projects:**

**Person → Student Hierarchy:**
- Base `Person` class with age management
- `Student` class extending Person with student-specific methods
- `Professor` class with private subject attribute
- Demonstrating inheritance and polymorphism

**Key Learning:**
Understanding that **inheritance enables code reuse and specialization**.

---

## 🎮 Major Projects

### 🃏 Project 1: Blackjack Card Game

**Complexity:** High | **Classes:** 4 | **Lines:** ~150

A fully functional casino-style Blackjack game demonstrating complete OOP mastery.

#### Features Implemented

**Game Mechanics:**
- 🎴 Complete 52-card deck (4 suits × 13 values)
- 🔀 Card shuffling with `random.shuffle()`
- 🎯 Player vs Dealer gameplay
- 💯 Automatic score calculation
- 🃏 Smart Ace handling (11 → 1 when needed)
- 🏆 Win/Draw/Loss detection
- 🔄 Replay functionality

**Class Architecture:**

```
Cards
├── Attributes: color, value
├── Logic: Face cards = 10, Aces = 11
└── __str__(): Display representation

Deck
├── Contains: 52 Card objects
├── Methods: create_cards(), shuffle(), choose_card()
└── Manages: Card drawing and deck state

Player
├── Attributes: name, score, main (hand)
├── Methods: give_card(), calculate_score()
└── Logic: Ace adjustment when score > 21

Game
├── Contains: Deck, Player, Dealer
├── Methods: play(), check_winner(), start_blackjack()
└── Controls: Game flow and turn logic
```

#### OOP Concepts Applied

1. **Composition:** Game contains Deck and Players
2. **Encapsulation:** Card value logic hidden in Cards class
3. **Methods:** Each class has clear responsibilities
4. **Object Interaction:** Players draw from Deck, Game checks Players
5. **State Management:** Tracking current game state
6. **Loops and Logic:** Turn-based gameplay

#### Technical Highlights

**Smart Ace Handling:**
```python
def calculate_score(self):
    total = 0
    as_number = 0
    
    for card in self.main:
        total += card.value
        if card.value == 11:
            as_number += 1
    
    # Reduce Aces from 11 to 1 if needed
    while total > 21 and as_number > 0:
        total -= 10
        as_number -= 1
    
    return total
```

**Game Flow Control:**
```python
def play(self):
    # Initial deal
    for _ in range(2):
        self.player.give_card(self.deck.choose_card())
        self.dealer.give_card(self.deck.choose_card())
    
    # Player turn (hit or stand)
    while self.player.score <= 21:
        choice = input("Hit or Stand? ")
        if choice == "hit":
            self.player.give_card(self.deck.choose_card())
        else:
            break
    
    # Dealer turn (must hit until 17)
    while self.dealer.score < 17:
        self.dealer.give_card(self.deck.choose_card())
    
    self.check_winner()
```

---

### ⚔️ Project 2: Battle Arena Game

**Complexity:** High | **Classes:** 2 | **Lines:** ~100

A turn-based combat game with difficulty levels and random damage mechanics.

#### Features Implemented

**Game Mechanics:**
- 🎮 Three difficulty levels (Easy, Medium, Hard)
- ⚔️ Random damage system (10-50 per attack)
- 💀 Health point tracking
- 🎯 Automatic turn alternation
- 🏆 Victory/defeat detection
- 📊 Real-time stat display

**Difficulty Levels:**

| Level | Hero | Health | Enemy | Health | Challenge |
|-------|------|--------|-------|--------|-----------|
| **Easy** | Frodo | 100 HP | Orc | 50 HP | 🟢 Beginner |
| **Medium** | Aragorn | 90 HP | Smaug | 120 HP | 🟡 Balanced |
| **Hard** | Gandalf | 50 HP | Balrog | 200 HP | 🔴 Expert |

#### Class Architecture

```
Character
├── Attributes: name, life
├── Methods:
│   ├── attack(opponent): Deal random damage
│   ├── is_alive(): Check if still in fight
│   └── __str__(): Display current health
└── Logic: Health management and combat

Game
├── Attributes: level, player, enemy
├── Methods:
│   ├── choose_level(): Difficulty selection
│   ├── startGame(): Initialize characters
│   ├── check_winner(): Determine outcome
│   └── Battle loop: Turn management
└── Controls: Complete game flow
```

#### OOP Concepts Applied

1. **Object Interaction:** Characters attack each other
2. **State Management:** Tracking health and game status
3. **Polymorphism:** Same Character class for different heroes/enemies
4. **Game Loop:** Complex turn-based logic
5. **Input Validation:** Try/except for user input
6. **Boolean Methods:** `is_alive()` for state checking

#### Technical Highlights

**Random Combat System:**
```python
def attack(self, player):
    damage = random.randint(10, 50)
    player.life -= damage
    print(f"{self.name} attacked {player.name} for {damage} damage!")
```

**Game Flow with Level Selection:**
```python
def choose_level(self):
    print("1. Easy - Frodo (100) vs Orc (50)")
    print("2. Medium - Aragorn (90) vs Smaug (120)")
    print("3. Hard - Gandalf (50) vs Balrog (200)")
    
    level = int(input("Choose level: "))
    
    if level == 1:
        self.player = Character("Frodo", 100)
        self.enemy = Character("Orc", 50)
    # ... etc
```

**Turn-Based Battle Loop:**
```python
while self.player.is_alive() and self.enemy.is_alive():
    print(f"{self.player} | {self.enemy}")
    
    input("Press 1 to attack: ")
    
    self.player.attack(self.enemy)
    
    if self.enemy.is_alive():
        self.enemy.attack(self.player)
    
    self.check_winner()
```

---

## 🏆 Skills Acquired

### Core OOP Principles

```
Classes & Objects         ████████████████████ 100%
Encapsulation            ████████████████████ 100%
Inheritance              ████████████████████ 100%
Composition              ████████████████████ 100%
Polymorphism             ███████████████████░  95%
```

### Technical Skills

**Python Mastery:**
- ✅ Class definition and instantiation
- ✅ `__init__()` constructors
- ✅ Magic methods (`__str__()`)
- ✅ Private attributes (`__attribute`)
- ✅ Getters and Setters
- ✅ Inheritance with `super()`
- ✅ Method override
- ✅ Object references and composition

**Advanced Concepts:**
- ✅ Game state machines
- ✅ Turn-based logic
- ✅ Random number generation
- ✅ Input validation and error handling
- ✅ Complex data structures (lists, dictionaries)
- ✅ Boolean logic and conditionals
- ✅ Loop control (while, for)

**Software Design:**
- ✅ Separation of concerns
- ✅ Single Responsibility Principle
- ✅ Clear class hierarchies
- ✅ Descriptive naming conventions
- ✅ Code organization and modularity

---

## 📊 Learning Metrics

### Project Complexity Evolution

| Day | Focus | Project | Classes | Complexity |
|-----|-------|---------|---------|------------|
| 1 | Basics | Product/VAT | 1 | 🟢 Simple |
| 2 | Encapsulation | Order System | 1 | 🟡 Medium |
| 3 | Composition | City/Person, Rectangle | 2 | 🟡 Medium |
| 3 | Game Logic | Battle Arena | 2 | 🟠 Advanced |
| 4 | Inheritance | Person/Student | 3 | 🟡 Medium |
| 4 | **Complete Project** | **Blackjack** | **4** | 🔴 **Complex** |

### Code Volume

- **Total Classes Created:** 10+
- **Total Methods Written:** 40+
- **Lines of Code:** 500+
- **Complete Games:** 2

---

## 💡 Key Takeaways

### What I Learned

1. **OOP isn't just syntax** - It's a way of thinking about problems
2. **Encapsulation protects integrity** - Private attributes prevent bugs
3. **Composition enables complexity** - Objects can contain and modify other objects
4. **Inheritance reduces repetition** - Share code between related classes
5. **Game development teaches OOP** - Interactive systems require proper architecture

### From Theory to Practice

**Day 1:** "What is a class?"  
**Day 4:** Building complete, playable games with multiple interacting classes

**Progression:**
- Started with simple Product class
- Ended with complex game architectures
- Learned to think in objects and interactions
- Understood when to use each OOP principle

---

## 🎯 Real-World Applications

### Skills Transferable to Professional Development

**Architecture Design:**
- Breaking complex systems into classes
- Defining clear responsibilities
- Managing object relationships

**Code Quality:**
- Writing maintainable, reusable code
- Implementing data protection
- Following best practices

**Problem Solving:**
- Translating requirements into classes
- Designing object interactions
- Managing state and behavior

---

## 🚀 What's Next

### Future Improvements
- [ ] Add graphical interfaces (Pygame GUI)
- [ ] Implement save/load functionality
- [ ] Add network multiplayer
- [ ] Create unit tests
- [ ] Build web versions with Flask

### Advanced OOP to Explore
- [ ] Abstract classes and interfaces
- [ ] Multiple inheritance
- [ ] Metaclasses
- [ ] Design patterns (Factory, Singleton, Observer)
- [ ] SOLID principles

---

## 📄 License

Educational project - Free to learn from and adapt.

---

## 👤 Author

**Mahira Manico**
- GitHub: [@mahira-manico](https://github.com/mahira-manico)
- Student at: **La Plateforme_**

---

## 🙏 Acknowledgments

- 🎓 **La Plateforme_** for the intensive, project-based OOP training
- 🎮 Classic card and combat games for inspiration
- 📚 Python community for excellent documentation

---

<div align="center">

### 🎓 4 Days. 10+ Classes. 2 Complete Games. 100% OOP Mastery.

<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="200"/>

**From theory to functional games - The power of Object-Oriented Programming**

*Made with 🧠 and Python by Mahira*

</div>
