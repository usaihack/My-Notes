**Without looking at your notes**, fill in this table in a file called `signal_test.txt`:

```
Signal Name | Signal Number | Keyboard Shortcut | Can it be ignored?

SIGINT      |               |                   |

SIGTERM     |               |                   |

SIGKILL     |               |                   |

SIGSTOP     |               |                   |

SIGSTP      |               |                   |

SIGCONT     |               |                   |
```



### Solution:

```
Signal Name | Signal Number | Keyboard Shortcut | Can it be ignored?

SIGINT      |    2         |       ctrl + C   |  yes

SIGTERM     |    15        |       nil        |   yes

SIGKILL     |    9         |       nil        |   no

SIGSTOP     |    19        |       nil        |   no

SIGSTP      |    20        |       ctrl + Z   |   yes

SIGCONT     |    18        |       nil        |   depends on the previous state
```


