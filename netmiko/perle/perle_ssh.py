import time
from netmiko.cisco_base_connection import CiscoSSHConnection


class PerleSSH(CiscoSSHConnection):
  def session_preparation(self):
    """Prepare the session after the connection has been established"""
    self._test_channel_read(pattern=r"[#]")
    self.RETURN = '\r\n'
    self.set_base_prompt()
    # self.disable_paging()
    # self.set_terminal_width(command="terminal width 511")
    # Clear the read buffer
    time.sleep(0.3 * self.global_delay_factor)
    self.clear_buffer()
