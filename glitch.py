# glitch script for blender 2.8

import bpy
import random

def main():

    #export obj
    def exportOBJ():
        bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)


    #import OBJ
    def importOBJ():
        #delete all objects in scene
        bpy.ops.object.select_all(action = 'SELECT')
        bpy.ops.object.delete(use_global = False)

        #open glitched file
        bpy.ops.import_scene.obj(filepath = glitchedFile)


    #change numbers in obj file
    def randomNumbers(n):
        if n != 0:
            exportOBJ()
            f = open(exportedFile)
            fn = open(glitchedFile, 'w')
            for l in f:
                if l[0] == 'v':
                    if random.random() < n:
                        rn1 = random.choice(range(10))
                        rn2 = random.choice(range(10))
                        l = [str(rn1) if i == str(rn2) else i for i in l]

                fn.write(''.join(l))

            f.close()
            fn.close()
            importOBJ()
        else:
            pass


    #shuffle vertex lines
    def shuffleVertices(n):
        if n != 0:
            exportOBJ()
            f1 = open(exportedFile)
            f2 = open(exportedFile)
            fn = open(glitchedFile, 'w')

            a = [l for l in f1 if l[0:2] == 'v ']
            random.shuffle(a)

            for l in f2:
                if l[0:2] == 'v ':
                    if random.random() < n:
                        l = a[random.choice(range(len(a)))]

                fn.write(''.join(l))

            f1.close()
            f2.close()
            fn.close()
            importOBJ()
        else:
            pass


    #remove faces
    def removeFaces(n):
        if n != 0:
            exportOBJ()
            f = open(exportedFile)
            fn = open(glitchedFile, 'w')

            for l in f:
                if l[0] == 'f':
                    if random.random() < n:
                        l = ''

                fn.write(''.join(l))

            f.close()
            fn.close()
            importOBJ()
        else:
            pass


    def glitch(n1, n2, n3):
        shuffleVertices(n1)
        randomNumbers(n2)
        removeFaces(n3)


    def flatShadingAllObjects():
        for i in bpy.data.objects:
            if i.type == 'MESH':
                for p in i.data.polygons:
                    p.use_smooth = False


    #the obj file is saved to and loaded from the temp folder
    exportedFile = bpy.app.tempdir + 'modelExport.obj'
    glitchedFile = bpy.app.tempdir + 'modelGlitched.obj'


    #call the glitch function
    glitch(.1, .1, .1)
    flatShadingAllObjects()


if __name__ == '__main__':
    main()
