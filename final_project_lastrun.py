#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 30, 2023, at 15:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'final_project'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\urmil\\OneDrive\\Desktop\\final_project_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "TRIAL1" ---
TRIAL_1 = visual.TextStim(win=win, name='TRIAL_1',
    text='Health',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
TestText = visual.TextStim(win=win, name='TestText',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_textbox = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox',
     depth=-1, autoLog=True,
)
submit_text = visual.TextStim(win=win, name='submit_text',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_mouse = event.Mouse(win=win)
x, y = [None, None]
test_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "TRIAL2_3" ---
text = visual.TextStim(win=win, name='text',
    text='Weather',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp2 = keyboard.Keyboard()

# --- Initialize components for Routine "trial2" ---
testtext = visual.TextStim(win=win, name='testtext',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_textbox2 = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox2',
     depth=-1, autoLog=True,
)
submit_text2 = visual.TextStim(win=win, name='submit_text2',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_mouse2 = event.Mouse(win=win)
x, y = [None, None]
test_mouse2.mouseClock = core.Clock()

# --- Initialize components for Routine "TRIAL3_3" ---
TRIAL2_2 = visual.TextStim(win=win, name='TRIAL2_2',
    text='Science',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp3 = keyboard.Keyboard()

# --- Initialize components for Routine "trial3" ---
test_text3 = visual.TextStim(win=win, name='test_text3',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_textbox3 = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox3',
     depth=-1, autoLog=True,
)
submit_text3 = visual.TextStim(win=win, name='submit_text3',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_mouse3 = event.Mouse(win=win)
x, y = [None, None]
test_mouse3.mouseClock = core.Clock()

# --- Initialize components for Routine "TRIAL4_3" ---
TRIAL3_2 = visual.TextStim(win=win, name='TRIAL3_2',
    text='Entertainment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp3_2 = keyboard.Keyboard()

# --- Initialize components for Routine "trial4" ---
test_text4 = visual.TextStim(win=win, name='test_text4',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_textbox4 = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox4',
     depth=-1, autoLog=True,
)
submit_text4 = visual.TextStim(win=win, name='submit_text4',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_mouse4 = event.Mouse(win=win)
x, y = [None, None]
test_mouse4.mouseClock = core.Clock()

# --- Initialize components for Routine "TRIAL5" ---
TRIAL4_2 = visual.TextStim(win=win, name='TRIAL4_2',
    text='Animal',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp4 = keyboard.Keyboard()

# --- Initialize components for Routine "trial5" ---
test_text5 = visual.TextStim(win=win, name='test_text5',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_textbox5 = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox5',
     depth=-1, autoLog=True,
)
submit_text5 = visual.TextStim(win=win, name='submit_text5',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_mouse5 = event.Mouse(win=win)
x, y = [None, None]
test_mouse5.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "TRIAL1" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
TRIAL1Components = [TRIAL_1, key_resp]
for thisComponent in TRIAL1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TRIAL1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TRIAL_1* updates
    
    # if TRIAL_1 is starting this frame...
    if TRIAL_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TRIAL_1.frameNStart = frameN  # exact frame index
        TRIAL_1.tStart = t  # local t and not account for scr refresh
        TRIAL_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TRIAL_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TRIAL_1.started')
        # update status
        TRIAL_1.status = STARTED
        TRIAL_1.setAutoDraw(True)
    
    # if TRIAL_1 is active this frame...
    if TRIAL_1.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TRIAL1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TRIAL1" ---
for thisComponent in TRIAL1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
# the Routine "TRIAL1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semantic priming/Conditions/final_condition1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    TestText.setText(test_word)
    test_textbox.reset()
    # setup some python lists for storing info about the test_mouse
    test_mouse.x = []
    test_mouse.y = []
    test_mouse.leftButton = []
    test_mouse.midButton = []
    test_mouse.rightButton = []
    test_mouse.time = []
    test_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [TestText, test_textbox, submit_text, test_mouse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TestText* updates
        
        # if TestText is starting this frame...
        if TestText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestText.frameNStart = frameN  # exact frame index
            TestText.tStart = t  # local t and not account for scr refresh
            TestText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TestText.started')
            # update status
            TestText.status = STARTED
            TestText.setAutoDraw(True)
        
        # if TestText is active this frame...
        if TestText.status == STARTED:
            # update params
            pass
        
        # if TestText is stopping this frame...
        if TestText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TestText.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                TestText.tStop = t  # not accounting for scr refresh
                TestText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TestText.stopped')
                # update status
                TestText.status = FINISHED
                TestText.setAutoDraw(False)
        
        # *test_textbox* updates
        
        # if test_textbox is starting this frame...
        if test_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox.frameNStart = frameN  # exact frame index
            test_textbox.tStart = t  # local t and not account for scr refresh
            test_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox.started')
            # update status
            test_textbox.status = STARTED
            test_textbox.setAutoDraw(True)
        
        # if test_textbox is active this frame...
        if test_textbox.status == STARTED:
            # update params
            pass
        
        # *submit_text* updates
        
        # if submit_text is starting this frame...
        if submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text.frameNStart = frameN  # exact frame index
            submit_text.tStart = t  # local t and not account for scr refresh
            submit_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text.started')
            # update status
            submit_text.status = STARTED
            submit_text.setAutoDraw(True)
        
        # if submit_text is active this frame...
        if submit_text.status == STARTED:
            # update params
            pass
        # *test_mouse* updates
        
        # if test_mouse is starting this frame...
        if test_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_mouse.frameNStart = frameN  # exact frame index
            test_mouse.tStart = t  # local t and not account for scr refresh
            test_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('test_mouse.started', t)
            # update status
            test_mouse.status = STARTED
            test_mouse.mouseClock.reset()
            prevButtonState = test_mouse.getPressed()  # if button is down already this ISN'T a new click
        if test_mouse.status == STARTED:  # only update if started and not finished!
            buttons = test_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(submit_text, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(test_mouse):
                            gotValidClick = True
                            test_mouse.clicked_name.append(obj.name)
                    x, y = test_mouse.getPos()
                    test_mouse.x.append(x)
                    test_mouse.y.append(y)
                    buttons = test_mouse.getPressed()
                    test_mouse.leftButton.append(buttons[0])
                    test_mouse.midButton.append(buttons[1])
                    test_mouse.rightButton.append(buttons[2])
                    test_mouse.time.append(test_mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('test_textbox.text',test_textbox.text)
    # store data for trials (TrialHandler)
    trials.addData('test_mouse.x', test_mouse.x)
    trials.addData('test_mouse.y', test_mouse.y)
    trials.addData('test_mouse.leftButton', test_mouse.leftButton)
    trials.addData('test_mouse.midButton', test_mouse.midButton)
    trials.addData('test_mouse.rightButton', test_mouse.rightButton)
    trials.addData('test_mouse.time', test_mouse.time)
    trials.addData('test_mouse.clicked_name', test_mouse.clicked_name)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "TRIAL2_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp2.keys = []
key_resp2.rt = []
_key_resp2_allKeys = []
# keep track of which components have finished
TRIAL2_3Components = [text, key_resp2]
for thisComponent in TRIAL2_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TRIAL2_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *key_resp2* updates
    waitOnFlip = False
    
    # if key_resp2 is starting this frame...
    if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp2.frameNStart = frameN  # exact frame index
        key_resp2.tStart = t  # local t and not account for scr refresh
        key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp2.started')
        # update status
        key_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp2_allKeys.extend(theseKeys)
        if len(_key_resp2_allKeys):
            key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
            key_resp2.rt = _key_resp2_allKeys[-1].rt
            key_resp2.duration = _key_resp2_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TRIAL2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TRIAL2_3" ---
for thisComponent in TRIAL2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp2.keys in ['', [], None]:  # No response was made
    key_resp2.keys = None
thisExp.addData('key_resp2.keys',key_resp2.keys)
if key_resp2.keys != None:  # we had a response
    thisExp.addData('key_resp2.rt', key_resp2.rt)
    thisExp.addData('key_resp2.duration', key_resp2.duration)
thisExp.nextEntry()
# the Routine "TRIAL2_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semantic priming/Conditions/final_condtion2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    # update component parameters for each repeat
    testtext.setText(test_word)
    test_textbox2.reset()
    # setup some python lists for storing info about the test_mouse2
    test_mouse2.x = []
    test_mouse2.y = []
    test_mouse2.leftButton = []
    test_mouse2.midButton = []
    test_mouse2.rightButton = []
    test_mouse2.time = []
    test_mouse2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trial2Components = [testtext, test_textbox2, submit_text2, test_mouse2]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testtext* updates
        
        # if testtext is starting this frame...
        if testtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testtext.frameNStart = frameN  # exact frame index
            testtext.tStart = t  # local t and not account for scr refresh
            testtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'testtext.started')
            # update status
            testtext.status = STARTED
            testtext.setAutoDraw(True)
        
        # if testtext is active this frame...
        if testtext.status == STARTED:
            # update params
            pass
        
        # if testtext is stopping this frame...
        if testtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testtext.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                testtext.tStop = t  # not accounting for scr refresh
                testtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'testtext.stopped')
                # update status
                testtext.status = FINISHED
                testtext.setAutoDraw(False)
        
        # *test_textbox2* updates
        
        # if test_textbox2 is starting this frame...
        if test_textbox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox2.frameNStart = frameN  # exact frame index
            test_textbox2.tStart = t  # local t and not account for scr refresh
            test_textbox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox2.started')
            # update status
            test_textbox2.status = STARTED
            test_textbox2.setAutoDraw(True)
        
        # if test_textbox2 is active this frame...
        if test_textbox2.status == STARTED:
            # update params
            pass
        
        # *submit_text2* updates
        
        # if submit_text2 is starting this frame...
        if submit_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text2.frameNStart = frameN  # exact frame index
            submit_text2.tStart = t  # local t and not account for scr refresh
            submit_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text2.started')
            # update status
            submit_text2.status = STARTED
            submit_text2.setAutoDraw(True)
        
        # if submit_text2 is active this frame...
        if submit_text2.status == STARTED:
            # update params
            pass
        # *test_mouse2* updates
        
        # if test_mouse2 is starting this frame...
        if test_mouse2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_mouse2.frameNStart = frameN  # exact frame index
            test_mouse2.tStart = t  # local t and not account for scr refresh
            test_mouse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_mouse2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('test_mouse2.started', t)
            # update status
            test_mouse2.status = STARTED
            test_mouse2.mouseClock.reset()
            prevButtonState = test_mouse2.getPressed()  # if button is down already this ISN'T a new click
        if test_mouse2.status == STARTED:  # only update if started and not finished!
            buttons = test_mouse2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(submit_text, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(test_mouse2):
                            gotValidClick = True
                            test_mouse2.clicked_name.append(obj.name)
                    x, y = test_mouse2.getPos()
                    test_mouse2.x.append(x)
                    test_mouse2.y.append(y)
                    buttons = test_mouse2.getPressed()
                    test_mouse2.leftButton.append(buttons[0])
                    test_mouse2.midButton.append(buttons[1])
                    test_mouse2.rightButton.append(buttons[2])
                    test_mouse2.time.append(test_mouse2.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('test_textbox2.text',test_textbox2.text)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('test_mouse2.x', test_mouse2.x)
    trials_2.addData('test_mouse2.y', test_mouse2.y)
    trials_2.addData('test_mouse2.leftButton', test_mouse2.leftButton)
    trials_2.addData('test_mouse2.midButton', test_mouse2.midButton)
    trials_2.addData('test_mouse2.rightButton', test_mouse2.rightButton)
    trials_2.addData('test_mouse2.time', test_mouse2.time)
    trials_2.addData('test_mouse2.clicked_name', test_mouse2.clicked_name)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "TRIAL3_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp3.keys = []
key_resp3.rt = []
_key_resp3_allKeys = []
# keep track of which components have finished
TRIAL3_3Components = [TRIAL2_2, key_resp3]
for thisComponent in TRIAL3_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TRIAL3_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TRIAL2_2* updates
    
    # if TRIAL2_2 is starting this frame...
    if TRIAL2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TRIAL2_2.frameNStart = frameN  # exact frame index
        TRIAL2_2.tStart = t  # local t and not account for scr refresh
        TRIAL2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TRIAL2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TRIAL2_2.started')
        # update status
        TRIAL2_2.status = STARTED
        TRIAL2_2.setAutoDraw(True)
    
    # if TRIAL2_2 is active this frame...
    if TRIAL2_2.status == STARTED:
        # update params
        pass
    
    # *key_resp3* updates
    waitOnFlip = False
    
    # if key_resp3 is starting this frame...
    if key_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp3.frameNStart = frameN  # exact frame index
        key_resp3.tStart = t  # local t and not account for scr refresh
        key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp3.started')
        # update status
        key_resp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp3_allKeys.extend(theseKeys)
        if len(_key_resp3_allKeys):
            key_resp3.keys = _key_resp3_allKeys[-1].name  # just the last key pressed
            key_resp3.rt = _key_resp3_allKeys[-1].rt
            key_resp3.duration = _key_resp3_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TRIAL3_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TRIAL3_3" ---
for thisComponent in TRIAL3_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp3.keys in ['', [], None]:  # No response was made
    key_resp3.keys = None
thisExp.addData('key_resp3.keys',key_resp3.keys)
if key_resp3.keys != None:  # we had a response
    thisExp.addData('key_resp3.rt', key_resp3.rt)
    thisExp.addData('key_resp3.duration', key_resp3.duration)
thisExp.nextEntry()
# the Routine "TRIAL3_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semantic priming/Conditions/final_condition3.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial3" ---
    continueRoutine = True
    # update component parameters for each repeat
    test_text3.setText(test_word)
    test_textbox3.reset()
    # setup some python lists for storing info about the test_mouse3
    test_mouse3.x = []
    test_mouse3.y = []
    test_mouse3.leftButton = []
    test_mouse3.midButton = []
    test_mouse3.rightButton = []
    test_mouse3.time = []
    test_mouse3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trial3Components = [test_text3, test_textbox3, submit_text3, test_mouse3]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_text3* updates
        
        # if test_text3 is starting this frame...
        if test_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_text3.frameNStart = frameN  # exact frame index
            test_text3.tStart = t  # local t and not account for scr refresh
            test_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_text3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_text3.started')
            # update status
            test_text3.status = STARTED
            test_text3.setAutoDraw(True)
        
        # if test_text3 is active this frame...
        if test_text3.status == STARTED:
            # update params
            pass
        
        # if test_text3 is stopping this frame...
        if test_text3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_text3.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                test_text3.tStop = t  # not accounting for scr refresh
                test_text3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_text3.stopped')
                # update status
                test_text3.status = FINISHED
                test_text3.setAutoDraw(False)
        
        # *test_textbox3* updates
        
        # if test_textbox3 is starting this frame...
        if test_textbox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox3.frameNStart = frameN  # exact frame index
            test_textbox3.tStart = t  # local t and not account for scr refresh
            test_textbox3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox3.started')
            # update status
            test_textbox3.status = STARTED
            test_textbox3.setAutoDraw(True)
        
        # if test_textbox3 is active this frame...
        if test_textbox3.status == STARTED:
            # update params
            pass
        
        # *submit_text3* updates
        
        # if submit_text3 is starting this frame...
        if submit_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text3.frameNStart = frameN  # exact frame index
            submit_text3.tStart = t  # local t and not account for scr refresh
            submit_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text3.started')
            # update status
            submit_text3.status = STARTED
            submit_text3.setAutoDraw(True)
        
        # if submit_text3 is active this frame...
        if submit_text3.status == STARTED:
            # update params
            pass
        # *test_mouse3* updates
        
        # if test_mouse3 is starting this frame...
        if test_mouse3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_mouse3.frameNStart = frameN  # exact frame index
            test_mouse3.tStart = t  # local t and not account for scr refresh
            test_mouse3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_mouse3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('test_mouse3.started', t)
            # update status
            test_mouse3.status = STARTED
            test_mouse3.mouseClock.reset()
            prevButtonState = test_mouse3.getPressed()  # if button is down already this ISN'T a new click
        if test_mouse3.status == STARTED:  # only update if started and not finished!
            buttons = test_mouse3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(submit_text, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(test_mouse3):
                            gotValidClick = True
                            test_mouse3.clicked_name.append(obj.name)
                    x, y = test_mouse3.getPos()
                    test_mouse3.x.append(x)
                    test_mouse3.y.append(y)
                    buttons = test_mouse3.getPressed()
                    test_mouse3.leftButton.append(buttons[0])
                    test_mouse3.midButton.append(buttons[1])
                    test_mouse3.rightButton.append(buttons[2])
                    test_mouse3.time.append(test_mouse3.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial3" ---
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('test_textbox3.text',test_textbox3.text)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('test_mouse3.x', test_mouse3.x)
    trials_3.addData('test_mouse3.y', test_mouse3.y)
    trials_3.addData('test_mouse3.leftButton', test_mouse3.leftButton)
    trials_3.addData('test_mouse3.midButton', test_mouse3.midButton)
    trials_3.addData('test_mouse3.rightButton', test_mouse3.rightButton)
    trials_3.addData('test_mouse3.time', test_mouse3.time)
    trials_3.addData('test_mouse3.clicked_name', test_mouse3.clicked_name)
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# --- Prepare to start Routine "TRIAL4_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp3_2.keys = []
key_resp3_2.rt = []
_key_resp3_2_allKeys = []
# keep track of which components have finished
TRIAL4_3Components = [TRIAL3_2, key_resp3_2]
for thisComponent in TRIAL4_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TRIAL4_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TRIAL3_2* updates
    
    # if TRIAL3_2 is starting this frame...
    if TRIAL3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TRIAL3_2.frameNStart = frameN  # exact frame index
        TRIAL3_2.tStart = t  # local t and not account for scr refresh
        TRIAL3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TRIAL3_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TRIAL3_2.started')
        # update status
        TRIAL3_2.status = STARTED
        TRIAL3_2.setAutoDraw(True)
    
    # if TRIAL3_2 is active this frame...
    if TRIAL3_2.status == STARTED:
        # update params
        pass
    
    # *key_resp3_2* updates
    waitOnFlip = False
    
    # if key_resp3_2 is starting this frame...
    if key_resp3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp3_2.frameNStart = frameN  # exact frame index
        key_resp3_2.tStart = t  # local t and not account for scr refresh
        key_resp3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp3_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp3_2.started')
        # update status
        key_resp3_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp3_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp3_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp3_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp3_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp3_2_allKeys.extend(theseKeys)
        if len(_key_resp3_2_allKeys):
            key_resp3_2.keys = _key_resp3_2_allKeys[-1].name  # just the last key pressed
            key_resp3_2.rt = _key_resp3_2_allKeys[-1].rt
            key_resp3_2.duration = _key_resp3_2_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TRIAL4_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TRIAL4_3" ---
for thisComponent in TRIAL4_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp3_2.keys in ['', [], None]:  # No response was made
    key_resp3_2.keys = None
thisExp.addData('key_resp3_2.keys',key_resp3_2.keys)
if key_resp3_2.keys != None:  # we had a response
    thisExp.addData('key_resp3_2.rt', key_resp3_2.rt)
    thisExp.addData('key_resp3_2.duration', key_resp3_2.duration)
thisExp.nextEntry()
# the Routine "TRIAL4_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semantic priming/Conditions/final_condition4.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial4" ---
    continueRoutine = True
    # update component parameters for each repeat
    test_text4.setText(test_word)
    test_textbox4.reset()
    # setup some python lists for storing info about the test_mouse4
    test_mouse4.x = []
    test_mouse4.y = []
    test_mouse4.leftButton = []
    test_mouse4.midButton = []
    test_mouse4.rightButton = []
    test_mouse4.time = []
    test_mouse4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trial4Components = [test_text4, test_textbox4, submit_text4, test_mouse4]
    for thisComponent in trial4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_text4* updates
        
        # if test_text4 is starting this frame...
        if test_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_text4.frameNStart = frameN  # exact frame index
            test_text4.tStart = t  # local t and not account for scr refresh
            test_text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_text4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_text4.started')
            # update status
            test_text4.status = STARTED
            test_text4.setAutoDraw(True)
        
        # if test_text4 is active this frame...
        if test_text4.status == STARTED:
            # update params
            pass
        
        # if test_text4 is stopping this frame...
        if test_text4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_text4.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                test_text4.tStop = t  # not accounting for scr refresh
                test_text4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_text4.stopped')
                # update status
                test_text4.status = FINISHED
                test_text4.setAutoDraw(False)
        
        # *test_textbox4* updates
        
        # if test_textbox4 is starting this frame...
        if test_textbox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox4.frameNStart = frameN  # exact frame index
            test_textbox4.tStart = t  # local t and not account for scr refresh
            test_textbox4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox4.started')
            # update status
            test_textbox4.status = STARTED
            test_textbox4.setAutoDraw(True)
        
        # if test_textbox4 is active this frame...
        if test_textbox4.status == STARTED:
            # update params
            pass
        
        # *submit_text4* updates
        
        # if submit_text4 is starting this frame...
        if submit_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text4.frameNStart = frameN  # exact frame index
            submit_text4.tStart = t  # local t and not account for scr refresh
            submit_text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text4.started')
            # update status
            submit_text4.status = STARTED
            submit_text4.setAutoDraw(True)
        
        # if submit_text4 is active this frame...
        if submit_text4.status == STARTED:
            # update params
            pass
        # *test_mouse4* updates
        
        # if test_mouse4 is starting this frame...
        if test_mouse4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_mouse4.frameNStart = frameN  # exact frame index
            test_mouse4.tStart = t  # local t and not account for scr refresh
            test_mouse4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_mouse4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('test_mouse4.started', t)
            # update status
            test_mouse4.status = STARTED
            test_mouse4.mouseClock.reset()
            prevButtonState = test_mouse4.getPressed()  # if button is down already this ISN'T a new click
        if test_mouse4.status == STARTED:  # only update if started and not finished!
            buttons = test_mouse4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(submit_text, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(test_mouse4):
                            gotValidClick = True
                            test_mouse4.clicked_name.append(obj.name)
                    x, y = test_mouse4.getPos()
                    test_mouse4.x.append(x)
                    test_mouse4.y.append(y)
                    buttons = test_mouse4.getPressed()
                    test_mouse4.leftButton.append(buttons[0])
                    test_mouse4.midButton.append(buttons[1])
                    test_mouse4.rightButton.append(buttons[2])
                    test_mouse4.time.append(test_mouse4.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial4" ---
    for thisComponent in trial4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('test_textbox4.text',test_textbox4.text)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('test_mouse4.x', test_mouse4.x)
    trials_4.addData('test_mouse4.y', test_mouse4.y)
    trials_4.addData('test_mouse4.leftButton', test_mouse4.leftButton)
    trials_4.addData('test_mouse4.midButton', test_mouse4.midButton)
    trials_4.addData('test_mouse4.rightButton', test_mouse4.rightButton)
    trials_4.addData('test_mouse4.time', test_mouse4.time)
    trials_4.addData('test_mouse4.clicked_name', test_mouse4.clicked_name)
    # the Routine "trial4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# --- Prepare to start Routine "TRIAL5" ---
continueRoutine = True
# update component parameters for each repeat
key_resp4.keys = []
key_resp4.rt = []
_key_resp4_allKeys = []
# keep track of which components have finished
TRIAL5Components = [TRIAL4_2, key_resp4]
for thisComponent in TRIAL5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TRIAL5" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TRIAL4_2* updates
    
    # if TRIAL4_2 is starting this frame...
    if TRIAL4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TRIAL4_2.frameNStart = frameN  # exact frame index
        TRIAL4_2.tStart = t  # local t and not account for scr refresh
        TRIAL4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TRIAL4_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TRIAL4_2.started')
        # update status
        TRIAL4_2.status = STARTED
        TRIAL4_2.setAutoDraw(True)
    
    # if TRIAL4_2 is active this frame...
    if TRIAL4_2.status == STARTED:
        # update params
        pass
    
    # *key_resp4* updates
    waitOnFlip = False
    
    # if key_resp4 is starting this frame...
    if key_resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp4.frameNStart = frameN  # exact frame index
        key_resp4.tStart = t  # local t and not account for scr refresh
        key_resp4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp4.started')
        # update status
        key_resp4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp4_allKeys.extend(theseKeys)
        if len(_key_resp4_allKeys):
            key_resp4.keys = _key_resp4_allKeys[-1].name  # just the last key pressed
            key_resp4.rt = _key_resp4_allKeys[-1].rt
            key_resp4.duration = _key_resp4_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TRIAL5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TRIAL5" ---
for thisComponent in TRIAL5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp4.keys in ['', [], None]:  # No response was made
    key_resp4.keys = None
thisExp.addData('key_resp4.keys',key_resp4.keys)
if key_resp4.keys != None:  # we had a response
    thisExp.addData('key_resp4.rt', key_resp4.rt)
    thisExp.addData('key_resp4.duration', key_resp4.duration)
thisExp.nextEntry()
# the Routine "TRIAL5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semantic priming/Conditions/final_condition5.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial5" ---
    continueRoutine = True
    # update component parameters for each repeat
    test_text5.setText(test_word)
    test_textbox5.reset()
    # setup some python lists for storing info about the test_mouse5
    test_mouse5.x = []
    test_mouse5.y = []
    test_mouse5.leftButton = []
    test_mouse5.midButton = []
    test_mouse5.rightButton = []
    test_mouse5.time = []
    test_mouse5.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trial5Components = [test_text5, test_textbox5, submit_text5, test_mouse5]
    for thisComponent in trial5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_text5* updates
        
        # if test_text5 is starting this frame...
        if test_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_text5.frameNStart = frameN  # exact frame index
            test_text5.tStart = t  # local t and not account for scr refresh
            test_text5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_text5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_text5.started')
            # update status
            test_text5.status = STARTED
            test_text5.setAutoDraw(True)
        
        # if test_text5 is active this frame...
        if test_text5.status == STARTED:
            # update params
            pass
        
        # if test_text5 is stopping this frame...
        if test_text5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_text5.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                test_text5.tStop = t  # not accounting for scr refresh
                test_text5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_text5.stopped')
                # update status
                test_text5.status = FINISHED
                test_text5.setAutoDraw(False)
        
        # *test_textbox5* updates
        
        # if test_textbox5 is starting this frame...
        if test_textbox5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox5.frameNStart = frameN  # exact frame index
            test_textbox5.tStart = t  # local t and not account for scr refresh
            test_textbox5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox5.started')
            # update status
            test_textbox5.status = STARTED
            test_textbox5.setAutoDraw(True)
        
        # if test_textbox5 is active this frame...
        if test_textbox5.status == STARTED:
            # update params
            pass
        
        # *submit_text5* updates
        
        # if submit_text5 is starting this frame...
        if submit_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text5.frameNStart = frameN  # exact frame index
            submit_text5.tStart = t  # local t and not account for scr refresh
            submit_text5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text5.started')
            # update status
            submit_text5.status = STARTED
            submit_text5.setAutoDraw(True)
        
        # if submit_text5 is active this frame...
        if submit_text5.status == STARTED:
            # update params
            pass
        # *test_mouse5* updates
        
        # if test_mouse5 is starting this frame...
        if test_mouse5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_mouse5.frameNStart = frameN  # exact frame index
            test_mouse5.tStart = t  # local t and not account for scr refresh
            test_mouse5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_mouse5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('test_mouse5.started', t)
            # update status
            test_mouse5.status = STARTED
            test_mouse5.mouseClock.reset()
            prevButtonState = test_mouse5.getPressed()  # if button is down already this ISN'T a new click
        if test_mouse5.status == STARTED:  # only update if started and not finished!
            buttons = test_mouse5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(submit_text, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(test_mouse5):
                            gotValidClick = True
                            test_mouse5.clicked_name.append(obj.name)
                    x, y = test_mouse5.getPos()
                    test_mouse5.x.append(x)
                    test_mouse5.y.append(y)
                    buttons = test_mouse5.getPressed()
                    test_mouse5.leftButton.append(buttons[0])
                    test_mouse5.midButton.append(buttons[1])
                    test_mouse5.rightButton.append(buttons[2])
                    test_mouse5.time.append(test_mouse5.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial5" ---
    for thisComponent in trial5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('test_textbox5.text',test_textbox5.text)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('test_mouse5.x', test_mouse5.x)
    trials_5.addData('test_mouse5.y', test_mouse5.y)
    trials_5.addData('test_mouse5.leftButton', test_mouse5.leftButton)
    trials_5.addData('test_mouse5.midButton', test_mouse5.midButton)
    trials_5.addData('test_mouse5.rightButton', test_mouse5.rightButton)
    trials_5.addData('test_mouse5.time', test_mouse5.time)
    trials_5.addData('test_mouse5.clicked_name', test_mouse5.clicked_name)
    # the Routine "trial5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
