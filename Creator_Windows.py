import PySimpleGUI as sg
import os

sg.theme("DarkGrey15");

noMedia = False

def create_hda(Name, Location, Size, File_Type):
    os.system("powershell qemu-img create -f " + File_Type + " '" + Location + "/" + Name + "." + File_Type + "' " + Size)

def create_vm(Name, Accelorator, Location, File_Type, CPU, Cores, Memory, Media, Media_Type):
    if noMedia == False:
        command = "powershell qemu-system-x86_64 -accel " + Accelorator + " -cpu " + CPU + " -smp " + Cores + " -m " + Memory + " -hda '" + Location + "/" + Name + "." + File_Type + "' "
        if not os.path.exists("./VM"):
            os.system("powershell mkdir VM")
        os.system("powershell New-Item ./VM/" + Name + ".bat -ItemType File")
        file = open("VM/" + Name + ".bat", "w")
        file.write(command + "\n")
        file.close()
        command += "-drive file='" + Media + "',index=1,media=" + Media_Type + " -boot d"
        os.system(command)

sizes = ['K', 'M', 'G', 'T', 'P', 'E']
cpu_types = ['486', 'Broadwell', 'Cascadelake-Server', 'Conroe', 'Cooperlake', 'Denverton', 'Dhyana', 'EPYC', 'Haswell', 'Icelake-Client', 'Icelake-Server', 'IvyBridge', 'KnightsMill', 'Nehalem', 'Opteron_G1', 
             'Opteron_G2', 'Opteron_G3', 'Opteron_G4', 'Penryn', 'SandyBridge', 'Skylake-Client', 'Skylake-Server', 'Snowridge', 'Westmere', 'athlon' 'core2duo', 'coreduo', 'kvm32', 'kvm64', 'n270', 'pentium', 
             'pentium2', 'pentium3', 'phenom', 'qemu32', 'qemu64', 'base', 'host', 'max']
accel = ['tcg', 'whpx']
file_type = ['qcow2', 'raw', 'host_device', 'qcow', 'cow', 'vdi', 'vmdk', 'vpc', 'cloop']
media_types = ['cdrom', 'disk']

def Creator():
    cpu_list = sg.Combo(cpu_types, font=("Arial", 14), expand_x=True, enable_events=True, readonly=True, key="-CPU-")
    size_list = sg.Combo(sizes, font=("Arial", 14), expand_x=True, enable_events=True, readonly=True, key="-SIZES-")
    accel_list = sg.Combo(accel, font=("Arial", 14), expand_x=True, enable_events=True, readonly=True, key="-ACCEL-")
    file_type_list = sg.Combo(file_type, font=("Arial", 14), expand_x=True, enable_events=True, readonly=True, key="-FILE_TYPE-")
    media_type_list = sg.Combo(media_types, font=("Arial", 14), expand_x=True, enable_events=True, readonly=True, key="-MEDIA_TYPE-")
    layout = [
            [sg.Text("Qemu Creator")],
            [sg.Text("The Name of the VM: "), sg.Input()],
            [sg.Text("Which Accelorator: "), accel_list],
            [sg.Text("Where should be the Hda saved"), sg.FolderBrowse(key="-HDA-")],
            [sg.Text("What's the size of the Hda: "), sg.Input(), size_list],
            [sg.Text("What's the filetype for the Hda: "), file_type_list],
            [sg.Text("What's the CPU-Type: "), cpu_list],
            [sg.Text("How many Cores: "), sg.Input()],
            [sg.Text("What's the size of the Memory: "), sg.Input()],
            [sg.Text("Where is the Media Device: "), sg.FileBrowse(file_types=(("ISO Files", "*.iso"), ("Disk Image", "*.img")), key="-MEDIA-"), media_type_list], [sg.Button("Done")]
    ]
    window = sg.Window("Qemu Creator", icon="Icon.ico", element_justification='c').Layout(layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Done":
            name = values[0]
            accelorator = values["-ACCEL-"]
            save_loc = values["-HDA-"]
            size_hda = str(values[1] + values["-SIZES-"])
            file_type_hda = values["-FILE_TYPE-"]
            cpu_type = values["-CPU-"]
            cores = values[2]
            mem = values[3]
            media = values["-MEDIA-"]
            media_type = values["-MEDIA_TYPE-"]
            if media == None:
                noMedia = True
            create_hda(name, save_loc, size_hda, file_type_hda)
            create_vm(name, accelorator, save_loc, file_type_hda, cpu_type, cores, mem, media, media_type)
            window.close()
    return

if __name__ == "__main__":
    main()
