import PySimpleGUI as sg
import subprocess
import sys
def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Enter Domain Name to resolve : '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')],
                [sg.Output(size=(80,20))]]
    # Create the Window
    window = sg.Window('DNS Lookup', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('Entered Domain Name : ', values[0])
        runCommand(["python","python.py",values[0]])
    window.close()
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me
    retval = p.wait(timeout)
    return (retval, output)                         # also return the output just for fun
if __name__ == '__main__':
    main()
