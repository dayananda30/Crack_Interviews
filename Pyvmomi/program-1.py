#!/usr/bin/env python
from __future__ import print_function
import atexit
from pyvim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim
from tools import cli
from tools import tasks

MAX_DEPTH = 100

class vCenterOperations:
    def __init__(self,host,username,pwd):
        self.host = host
        self.username = username
        self.pwd = pwd

    def connect_vcenter(self):
        self.si = None
        try:
            self.si = SmartConnectNoSSL(host=self.host,
                                   user=self.username,
                                   pwd=self.pwd,
                                   port=int('443'))
            atexit.register(Disconnect, self.si)
        except vim.fault.InvalidLogin:
            raise SystemExit("Unable to connect to host "
                             "with supplied credentials.")

        return  self.si

    def get_all_datacenters(self,si):
        content = si.RetrieveContent()
        datacenters = content.rootFolder.childEntity
        return  datacenters

    def get_all_vmfolders(self,datacenters):
        for datacenter in datacenters:
            print("Datacenter : {}".format(datacenter.name))
            vmFolders = datacenter.vmFolder.childEntity
            #self.get_all_vms(vmFolders)
            self.shutdown_vms(vmFolders)



    def shutdown_vms(self,vmFolders):
        try:
            for folder in vmFolders:
                if folder.name == 'Dayananda':
                    vmlist = folder.childEntity
                    for vm in vmlist:
                        self.printvminfo(vm)
                        self.kill(vm)
                    print("*"*30)
        except AttributeError as e:
            pass

    def kill(self,VM):
        print("Found: {0}".format(VM.name))
        print("The current powerState is: {0}".format(VM.runtime.powerState))
        if format(VM.runtime.powerState) == "poweredOn":
            print("Attempting to power off {0}".format(VM.name))
            TASK = VM.PowerOffVM_Task()
            tasks.wait_for_tasks(self.si, [TASK])
            print("{0}".format(TASK.info.state))
        else:
            TASK = VM.PowerOnVM_Task()
            tasks.wait_for_tasks(self.si, [TASK])
            print("{0}".format(TASK.info.state))

    def get_all_vms(self,vmFolders):
        print(vmFolders)
        try:
            for folder in vmFolders:
                print("Folder : {}".format(folder.name))
                vmlist = folder.childEntity
                for vm in vmlist:
                    self.printvminfo(vm)
                    print("*"*30)
        except AttributeError as e:
            pass

    def printvminfo(self,vm, depth=1):
        if hasattr(vm, 'childEntity'):
            if depth > MAX_DEPTH:
                return
            vmlist = vm.childEntity
            for child in vmlist:
                self.printvminfo(child, depth+1)
            return

        summary = vm.summary
        print(summary.config.name)





def main():
    c_instance = vCenterOperations('@@@@@','@@@@@@','@@@@@@')
    vc_inst = c_instance.connect_vcenter()
    datacenters = c_instance.get_all_datacenters(vc_inst)
    vmfolders = c_instance.get_all_vmfolders(datacenters)
    #c_instance.get_all_vms(vmfolders)
    #c_instance.shutdown_vms(vmfolders)


# Start program
if __name__ == "__main__":
    main()
