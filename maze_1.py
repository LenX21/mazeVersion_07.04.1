maze=[[1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,0,1],
      [1,1,1,1,1,1,1,1]]
if __name__ == "__main__":
    star=[len(maze)-1]
    end=maze[len(maze)-1]
    print(maze)
    print ("Start:%s END: %s" % (star, end))
