#!/usr/bin/env python3

import inkex

"""
Extension for InkScape
 
Author: Super Plis Plas
Mail: superplisplas@gmail.com
Date: 19.08.2022
Last Patch: 19.08.2022
License: GNU GPL v3
"""

class SwapColors(inkex.EffectExtension):
     
    def effect(self):
        if len(self.svg.selection) > 1:
            #Select first node of selection
            firstNode = self.svg.selection[0]
            #Select rest nodes of selection
            restNodes = self.svg.selection[1:]
            #Swap colors. Set color from first node
            self.swap_colors(firstNode, restNode)

    def swap_colors (pivotNode, nodes):
        if pivotNode is not None and len(nodes) > 0:
            color = self.getFillColor(pivotNode)
            if color is not None:
                for node in nodes:
                    self.setFillColor(node, color)

    #style="fill:#00bdff;stroke:#000000;stroke-width:1.058;stroke-dasharray:none;stroke-opacity:1;fill-opacity:1"
    #Get fill color of a node
    def getFillColor (self, node):
        result = None
        #style = node.get("style")
        style = node.attrib["style"] if "style" in node.attrib else None
        if style is not None:
            startIdx = style.find("fill:", 0)
            if startIdx >= 0:
                endIdx = style.find(";", startIdx + len("fill:"))
                result = style[startIdx + len("fill:"):endIdx] if endIdx >= 0 else style[startIdx + len("fill:"):]
        return result
   
    #Set fill color of a node
    def setFillColor (self, node, color):
        result = None
        style = node.attrib["style"] if "style" in node.attrib else None
        if style is not None:
            startIdx = style.find("fill:", 0)
            if startIdx >= 0:
                endIdx = style.find(";", startIdx + len("fill:"))
                result = style[startIdx + len("fill:"):endIdx] if endIdx >= 0 else style[startIdx + len("fill:"):]
                newStyle = style[0:startIdx] + style[endIdx:]
                node.attrib["style"] = newStyle
        else:
            node.attrib["style"] = ""
        node.attrib["style"] += ";fill:" + color
        return result

if __name__ == '__main__':            
    SwapColors().run()
