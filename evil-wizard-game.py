import random   # To randomize attack damage 

def separator():
    print("=" * 60)
    
# BASE CHARACTER CLASS:
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        
        # State Effects:
        self.is_evading = False 
        self.is_blocking = False 
        self.is_frozen = False
        
# METHODS (core combat logic):
    # 1. CENTRAL DAMAGE SYSTEM:
    def take_damage(self, damage, attacker):
        
        # 1. Evade defense:
        if self.is_evading:
            print(f"{self.name} evaded the attack!")
            self.is_evading = False # reset
            return
        
        # 2. Block defense: 
        if self.is_blocking:
          print(f"{self.name} blocked the attack!")
          self.is_blocking = False
          return
        
        # Health damage:
        self.health -= damage
        print(f"{attacker.name} deals {damage} damage to {self.name}!")
        
    # 2. ATTACK:
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) # randomized damage.
        opponent.take_damage(damage, self)
          

    # 3. HEAL:
    def heal(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"\n{self.name} heals for {heal_amount} HP! ({self.health}/{self.max_health})")

    # 4. DISPLAY STATS:
    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
    
# SUBCLASSES:
# 1. Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 140, 25)
        
    # 1. Power Strike - extra damage.
    def power_strike(self, opponent):
        damage = self.attack_power + 15
        print(f"\n{self.name} uses Power Strike!")
        opponent.take_damage(damage,self)
        
    # 2. Berserk - high damage but w/ health cost.
    def berserk(self, opponent):
        damage = self.attack_power + 25
        self.health -= 10  # risk factor
        print(f"\n{self.name} goes Berserk! Loses 10 HP!")
        opponent.take_damage(damage,self)


# 2. Mage class 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 35)
        
    # 1. Fireball - strong attacks.
    def fireball(self, opponent):
        damage = self.attack_power + 20
        print(f"\n{self.name} casts Fireball!")
        opponent.take_damage(damage,self)
        
    # 2. Freeze - stops attack.
    def freeze(self, opponent):
        opponent.is_frozen = True
        print(f"\n{self.name} freezes {opponent.name}! They can't attack next turn!")
    

# 3. Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 30)
        
    # 1. Quick Shot - double damage.
    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        print(f"\n{self.name} uses Quick Shot!")
        opponent.take_damage(damage,self)
      
    # 2. Evade - evades next attack.
    def evade(self):
        self.is_evading = True
        print(f"\n{self.name} will evade the next attack!")

# 4. Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 170, 20)

    # 1. Holy Strike - adds bonus damage.
    def holy_strike(self, opponent):
        damage = self.attack_power + 10
        print(f"\n{self.name} uses Holy Strike!")
        opponent.take_damage(damage,self)
      
    # 2. Divine Shield - blocks next attack.
    def divine_shield(self):
        self.is_blocking = True
        print(f"\n{self.name} activates Divine Shield!")
  
  
# EVIL WIZARD CLASS (enemy)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, 150, 20)
    
    # Regenerates health after each turn.
    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 HP! (Current health: {self.health}/{self.max_health})")
        
  
# Welcome Message:
print("\n")
print("=" * 60)
print("============================================================")
print("                 DEFEAT THE EVIL WIZARD!")
print("============================================================")
print("=" * 60)

# MENU SYSTEM: 
# 1. Character Selection
def create_character():
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    # KeyboardInterrupt error catch:
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
      
# BATTLE:
def battle(player, wizard):
    
    # Main Game Loop:
    while wizard.health > 0 and player.health > 0:
        wizard_action = False   # To ensure wizard only acts if player acts.
        
        # Turn-based gameplay menu:
        print("\n=== YOUR TURN ===\n")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("\nChoose an action: ")
        if choice == '1':
            print("\n")
            player.attack(wizard)
            separator()
            wizard_action = True
            
        elif choice == '2':
            print("\n=== YOUR TURN ===\n")
          
            # 1. Warrior abilities:
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
                  
            # 2. Mage abilities:
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
          
            # 3. Archer abilities:
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
                
            # 4. Paladin abilities:
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
              
        elif choice == '3':
            player.heal()
            separator()
            wizard_action = True  # wizard still takes its turn. 
          
        elif choice == '4':
            
            player.display_stats() 
            separator()
            
        else:
            print("\nInvalid choice. Try again...\n")

        # GAME ENDS:
        if wizard_action and wizard.health > 0:
            
            # freeze ability logic:
            if wizard.is_frozen:
                print(f"{wizard.name} is frozen and cannot act!")
                wizard.is_frozen = False
                wizard_action = False
            else:
                wizard.regenerate()
                wizard.attack(player)
                wizard_action = False # reset
            separator()
        
        # VICTORY/DEFEAT MESSAGES:
        if player.health <= 0:
            print(f"\n{player.name} has been defeated! Better luck next time!")
            print(f"\n\n======================== GAME OVER =========================\n\n\n")
            break

        elif wizard.health <= 0:
            print(f"\nVICTORY! {wizard.name} has been defeated by {player.name}!")
            print(f"\n\n======================== GAME OVER =========================\n\n\n")

            break
            

# !> MAIN FUNCTION:
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()