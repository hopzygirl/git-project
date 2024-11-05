<<<<<<< HEAD
=======
def __dfs_util(self, v, visited):
    visited.add(v)
    for nb in self.graph[v]:
        if nb not in visited:
            self.__dfs_util(nb, visited)
>>>>>>> dev
