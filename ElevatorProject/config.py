from threading import Lock

order_matrix_lock = Lock()

N_ELEVATORS = 2
N_FLOORS = 4
N_BUTTONS = 3
ELEV_ID = 0
BASE_ELEVATOR_PORT = 20000 

#elevator direction
DIRN_DOWN = -1
DIRN_STOP = 0
DIRN_UP = 1

#buttons
BUTTON_CALL_UP = 0
BUTTON_CALL_DOWN = 1
BUTTON_COMMAND = 2
BUTTON_UP_DOWN = 3
BUTTON_IN_UP = 4
BUTTON_IN_DOWN = 5
BUTTON_MULTI = 6

N_DISTINCT_ORDERS = 7

#states
UNDEFINED = -1
IDLE = 0
RUN = 1
DOOR_OPEN = 2

NUMBER_OF_ELEVATORS = 2
