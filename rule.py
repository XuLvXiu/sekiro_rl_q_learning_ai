#encoding=utf8
'''
predefined state rule, these states have no need to be explored.
ONLY Rule class knows state->action rules.
'''
class Rule(): 

    def apply(self, state, env): 
        '''
        apply rule, get action id(not game action id), which is always 0.
        this method might be called multi times.
        '''
        # predefined state
        # state 11-19
        if state.state_id in env.state_manager.arr_parry_after_attack_state_id:  
            return 0

        # state-6: 
        if state.state_id == env.state_manager.HULU_STATE_ID: 
            return 0

        # state-5: 
        if state.state_id == env.state_manager.PLAYER_HP_DOWN_STATE_ID: 
            return 0

        # classification model
        # state-0: class-0
        if state.state_id == env.state_manager.NORMAL_STATE_ID: 
            return 0

        # state-4: class-4
        if state.state_id == env.state_manager.BAD_TUCI_STATE_ID: 
            return 0

        # state-1/2/3/10
        # no rule found, will use Q
        return None


    def is_parry_after_attack_state(self, state, state_manager): 
        '''
        if a parry after attack state
        '''
        # check parry
        arr_parry_state_id = []
        # 11-19
        arr_parry_state_id.extend(state_manager.arr_parry_after_attack_state_id)
        # 0
        arr_parry_state_id.append(state_manager.NORMAL_STATE_ID)
        # 4
        arr_parry_state_id.append(state_manager.BAD_TUCI_STATE_ID)

        if state.state_id in arr_parry_state_id: 
            last_state = state_manager.get_last_state()
            if last_state.is_attack or last_state.is_parry_after_attack: 
                return True

        # state 1/2/3 is attack
        # state 5/6 is neither parry nor attack.
        # state 10 is special, not parry.
        return False


    def generate_action_space_key(self, state, state_manager): 
        '''
        generate action space key
        '''
        obj = {
            # 0-4
            state_manager.NORMAL_STATE_ID: 'parry',
            state_manager.TUCI_STATE_ID: 'shipo_attack',
            state_manager.QINNA_STATE_ID: 'simple_attack',
            state_manager.FUZHOU_STATE_ID: 'simple_attack',
            state_manager.BAD_TUCI_STATE_ID: 'parry',

            # 5-6
            state_manager.PLAYER_HP_DOWN_STATE_ID: 'player_hp_down',
            state_manager.HULU_STATE_ID: 'hulu',

            # 10
            state_manager.POSTURE_DOWN_STATE_ID: 'player_posture_down',

            # 11-19
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_1: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_2: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_3: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_4: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_5: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_6: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_7: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_8: 'parry',
            state_manager.PARRY_AFTER_ATTACK_STATE_ID_9: 'parry',
        }

        key = state.state_id
        return obj[key]
