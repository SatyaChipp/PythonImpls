def remove_dups(self, head):
        current =head
        #using runner techinque -- two nodes - one slower than the other
        while current:
            runner=current
            while(runner.get_next()):
                if runner.get_next().data == current.data: #dup data
                    runner.set_next(runner.get_next().get_next())#skip dup and set it to next node
                else:
                    runner = runner.get_next()
            current = current.get_next()
