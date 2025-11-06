#encoding=utf8

class Rule(): 
    '''
    predefined state rule, these state no need to be explored.
    '''

    def __init__(self): 
        '''
        init
        '''
        self.reset()


    def reset(self): 
        '''
        reset some variables.
        '''
        self.is_attack = False
        self.is_parry_after_attack = False


    def apply(self, state, env): 
        '''
        apply rule, get action id(not game action id)
        this method might be called multi times.
        '''
        # 10
        base_offset = env.action_space + env.RULE_COUNT

        # predefined state
        # state 10-19
        if state.state_id in env.state_manager.arr_parry_after_attack_state_id:  
            # 7
            action_id = base_offset - 3

            last_state = env.state_manager.get_last_state()
            if last_state.is_attack or last_state.is_parry_after_attack: 
                self.is_parry_after_attack = True

            return action_id

        # state-6: 
        if state.state_id == env.state_manager.HULU_STATE_ID: 
            # 9
            action_id = base_offset - 1
            return action_id

        # state-5: 
        if state.state_id == env.state_manager.PLAYER_HP_DOWN_STATE_ID: 
            # 8
            action_id = base_offset - 2
            return action_id

        # classification model
        # state-0: class-0
        if state.state_id == env.state_manager.NORMAL_STATE_ID: 
            # 7
            action_id = base_offset - 3

            last_state = env.state_manager.get_last_state()
            if last_state.is_attack or last_state.is_parry_after_attack: 
                self.is_parry_after_attack = True

            return action_id

        # state-4: class-4
        if state.state_id == env.state_manager.BAD_TUCI_STATE_ID: 
            # 7
            action_id = base_offset - 3

            last_state = env.state_manager.get_last_state()
            if last_state.is_attack or last_state.is_parry_after_attack: 
                self.is_parry_after_attack = True

            return action_id

        # no rule found
        self.is_attack = True
        return None


    def is_attack_state(self, state, env): 
        '''
        if an attack state
        '''
        self.reset()
        self.apply(state, env)
        return self.is_attack


    def is_parry_after_attack_state(self, state, env): 
        '''
        if a parry after attack state
        '''
        self.reset()
        self.apply(state, env)
        return self.is_parry_after_attack
