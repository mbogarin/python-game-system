import random   # To randomize attack damage 

def separator():
    print("=" * 60)
    
# [Base Character class]
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        
        # Temporary states (boolean flag) - Note: tracks the character's state across turns (store & check later in attack method since this affects future actions).
        self.is_evading = False 
        self.is_blocking = False 
        self.is_frozen = False
        

    # !> METHODS:
    # Step 4: Modify: Randomize attack damage
    # ATTACK:
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)

        # Freeze attack:
        if self.is_frozen:
          print(f"- {self.name} is frozen and cannot attack!")
          self.is_frozen = False # reset
          return
          
        # Evade attack:
        if opponent.is_evading:
          print(f"{opponent.name} evaded the attack!")
          opponent.is_evading = False
          return
        
        # Block attack: 
        if opponent.is_blocking:
          print(f"{opponent.name} blocked the attack!")
          opponent.is_blocking = False
          return
      
        # # show player's health status after attack:
        # def player_health(self):
        #     print(f"{self.name} ")
        
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
         
# - (Step 3: Add Healing Mechanic:)
    # HEAL:
    def heal(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"\n{self.name} heals for {heal_amount}! Current health: {self.health}/{self.max_health}")

    # DISPLAY STATS:
    def display_stats(self):
        # print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power} ")
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
    

# [Warrior class (inherits from Character)]
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    # Unique abilities:
    # 1. Power Strike
    def power_strike(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"\n{self.name} uses Power Strike for {damage} damage!")
        
    # 2. Berserk (w/ risk factor)
    def berserk(self, opponent):
        damage = self.attack_power + 25
        self.health -= 10  # risk factor
        opponent.health -= damage
        print(f"\n{self.name} goes Berserk! Deals {damage} damage but loses 10 health!")


# [Mage class (inherits from Character)]
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    
    # Unique abilities:
    # 1. Fireball
    def fireball(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"\n{self.name} casts Fireball for {damage} damage!")
        
    # 2. Freeze
    def freeze(self, opponent):
        opponent.is_frozen = True
        print(f"{self.name} freezes {opponent.name}! They can't attack next turn!")
        
    

# [EvilWizard class (inherits from Character)]

# Step 6: Evil wizard logic: regenerate health & attack player after each turn.
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")

# Steps 1-2: Add 2 new character classes + 2 unique abilities for each.
# + Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
      
  # Unique abilities:
    # 1. Quick Shot - double arrow attack. 
    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"\n{self.name} uses Quick Shot for {damage} damage!")
      
    # 2. Evade - evades next attack.
    def evade(self):
        self.is_evading = True
        print(f"\n{self.name} will evade the next attack!")

# + Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=170, attack_power=20)

  # Unique abilities:
    # 1. Holy Strike - bonus damage.
    def holy_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"\n{self.name} uses Holy Stike for {damage} damage!")
      
      
    # 2. Divine Shield - blocks next attack.
    def divine_shield(self):
        self.is_blocking = True
        print(f"\n{self.name} activates Divine Shield!")
  
  
# [Menu System]

# !> 1. CREATE CHARACTER:
def create_character():
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    # KeyboardInterrup error catch:
    try:
        class_choice = input("\nEnter the number of your class choice: ")
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!\n")
        exit()
        
    name = input("\nEnter your character's name: ")
    print("\n")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("\nInvalid choice. Defaulting to Warrior...\n")
        return Warrior(name)
      
      
# !> 2. BATTLE EVIL WIZARD:
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
    
        wizard_action = False # wizard only acts if player attacks.
        
        print("\n=== YOUR TURN ===\n")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("\nChoose an action: ")

        # =! Step 5: Build Turn-Based Battle System:
        if choice == '1':
            print("\n")
            player.attack(wizard)
            separator()
            wizard_action = True
            
        
        # Implement Special Abilities:
        elif choice == '2':
            print("\n=== YOUR TURN ===\n")
          
            # Warrior
            if isinstance(player, Warrior):
                print("1. Power Strike")
                print("2. Berserk")
                ability = input("\nChoose ability: ")
                
                if ability == "1":
                    player.power_strike(wizard)
                    separator()
                    wizard_action = True
                elif ability == "2":
                    player.berserk(wizard)
                    separator()
                    wizard_action = True
                  
            # Mage
            elif isinstance(player, Mage):
                print("1. Fireball")
                print("2. Freeze")
                ability = input("\nChoose ability: ")
                
                if ability == "1":
                    player.fireball(wizard)
                    separator()
                    wizard_action = True
                elif ability == "2":
                    player.freeze(wizard)
                    separator()
                    wizard_action = True
          
            # Archer
            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability = input("\nChoose ability: ")
                
                if ability == "1":
                    player.quick_shot(wizard)
                    separator()
                    wizard_action = True
                elif ability == "2":
                    player.evade()
                    separator()
                    wizard_action = True
                
            # Paladin
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability = input("\nChoose ability: ")
              
                if ability == "1":
                    player.holy_strike(wizard)
                    separator()
                    wizard_action = True
                elif ability == "2":
                    player.divine_shield()
                    separator()
                    wizard_action = True
                  
            else: 
              print("\nInvalid ability choice. Try again...")
              
        # = Implement Heal Method:    
        elif choice == '3':
            
            player.heal()
            separator()
          
        elif choice == '4':
            
            player.display_stats() 
            separator()
            
        else:
            print("\nInvalid choice. Try again...\n")

        if wizard_action:
            wizard.regenerate()
            wizard.attack(player)
            wizard_action = False # reset
            
            # Show player stats after wizard's turn:
            print(f"\n{player.name}'s current health: {player.health}/{player.max_health}")
            
            separator()
        
    
    # =! Step 7: Victory/Defeat Messages:
        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            print("\n=== GAME OVER ===\n")
            break

    if wizard.health <= 0:
        print("\n=== GAME OVER ===")
        print(f"\n{wizard.name} has been defeated by {player.name}!\n\n")
    

# !> MAIN FUNCTION:
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()