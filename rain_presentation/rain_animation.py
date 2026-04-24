import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
import numpy as np

# ── constants ──────────────────────────────────────────────────────────────────
X_MIN, X_MAX = -30, 30
Y_MIN, Y_MAX = 0, 30
MULT = 3.0
GRID_STEP = 2.0

COVER_X0 = X_MIN
COVER_Y0 = 3 * MULT
COVER_W  = 3 * MULT
COVER_H  = 0.5 * MULT

HUMAN_X0 = X_MAX - MULT
HUMAN_W  = MULT
HUMAN_H  = 2 * MULT

DROP_POSITIONS = [
    (x, y)
    for x in np.arange(X_MIN, X_MAX, GRID_STEP)
    for y in np.arange(Y_MIN, Y_MAX, GRID_STEP)
]

def wrap(val, lo, hi):
    return (val - lo) % (hi - lo) + lo

# ── figure & axes ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.08, bottom=0.30, right=0.95, top=0.92)

ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.set_aspect('equal')
ax.set_title("Czy opłaca się biegać w deszczu?", fontsize=13)
ax.axis('off')

# ── patches ────────────────────────────────────────────────────────────────────
cover = plt.Rectangle((COVER_X0, COVER_Y0), COVER_W, COVER_H,
                       fc='steelblue', label='Schronienie', zorder=3)
human = plt.Rectangle((HUMAN_X0, 0), HUMAN_W, HUMAN_H,
                       fc='tomato', label='Człowiek', zorder=3)
drops = [plt.Circle(pos, 0.15, color='dodgerblue', alpha=0.6, zorder=2)
         for pos in DROP_POSITIONS]

ax.add_patch(cover)
ax.add_patch(human)
for d in drops:
    ax.add_patch(d)
ax.legend(loc='upper right', fontsize=9)

# ── widgets ────────────────────────────────────────────────────────────────────
ax_wind  = plt.axes([0.25, 0.19, 0.65, 0.03])
ax_stage = plt.axes([0.25, 0.13, 0.65, 0.03])
ax_speed = plt.axes([0.25, 0.07, 0.65, 0.03])
ax_btn   = plt.axes([0.05, 0.15, 0.10, 0.06])
ax_loop  = plt.axes([0.05, 0.07, 0.10, 0.06])

wind_slider  = Slider(ax_wind,  'Prędkość wiatru', -3.0, 3.0, valinit=0.0)
stage_slider = Slider(ax_stage, 'Ruch sceny',      -3.0, 3.0, valinit=0.0)
speed_slider = Slider(ax_speed, 'Prędkość',         0.1, 3.0, valinit=1.0)
btn_reset    = Button(ax_btn,  'Reset')
btn_loop     = Button(ax_loop, 'Loop: OFF')

_stopped = False
_loop    = False

def reset(event=None):
    global _stopped
    was_stopped = _stopped
    _stopped = False
    cover.set_x(COVER_X0)
    human.set_x(HUMAN_X0)
    for d, pos in zip(drops, DROP_POSITIONS):
        d.set_center(pos)
    if was_stopped and ani.event_source is not None:
        ani.event_source.start()
    fig.canvas.draw_idle()

def toggle_loop(event=None):
    global _loop
    _loop = not _loop
    btn_loop.label.set_text('Loop: ON' if _loop else 'Loop: OFF')
    fig.canvas.draw_idle()

btn_reset.on_clicked(reset)
btn_loop.on_clicked(toggle_loop)

# ── update ─────────────────────────────────────────────────────────────────────
def update(frame):
    global _stopped
    if _stopped:
        return [cover, human] + drops

    spd      =  speed_slider.val
    v_wind   =  wind_slider.val * 0.1   # horizontal speed added to drops only
    v_stage  =  stage_slider.val * 0.1  # shifts all objects (reference frame)
    v_human  = -0.5 * spd               # human moves left toward shelter
    v_rain_y = -0.3 * spd               # rain falls downward

    cover.set_x(cover.get_x() + v_stage)
    human.set_x(human.get_x() + v_human + v_stage)

    for d in drops:
        x = wrap(d.center[0] + v_wind + v_stage, X_MIN, X_MAX)
        y = wrap(d.center[1] + v_rain_y,          Y_MIN, Y_MAX)
        d.set_center((x, y))

    if human.get_x() <= cover.get_x() + COVER_W:
        if _loop:
            reset()
        else:
            _stopped = True

    return [cover, human] + drops

# ── run ────────────────────────────────────────────────────────────────────────
ani = animation.FuncAnimation(fig, update, interval=30, blit=False, repeat=False,
                              cache_frame_data=False)

plt.show(block=False)
while plt.get_fignums():
    plt.pause(0.01)
