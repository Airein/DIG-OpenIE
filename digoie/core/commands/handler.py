


def cmd_hander(opt):
    if opt['--interactive']:
        pass
        # MyInteractive().cmdloop()
    elif opt['stream']:
        print 'stream handler'
    else:
        print(opt)