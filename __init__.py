from .node import SAM2ModelLoader, GroundingDinoModelLoader, GroundingDinoSAM2Segment, GroundingDinoDetector, InvertMask, IsMaskEmptyNode, BboxSam2IndexSelector

NODE_CLASS_MAPPINGS = {
    'SAM2ModelLoader (segment anything2)': SAM2ModelLoader,
    'GroundingDinoModelLoader (segment anything2)': GroundingDinoModelLoader,
    'GroundingDinoSAM2Segment (segment anything2)': GroundingDinoSAM2Segment,
    'GroundingDinoDetector (segment anything2)': GroundingDinoDetector,
    'InvertMask (segment anything)': InvertMask,
    "IsMaskEmpty": IsMaskEmptyNode,
    "BboxSam2IndexSelector (segment anything2)": BboxSam2IndexSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'SAM2ModelLoader': 'SAM2 Model Loader',
    'GroundingDinoModelLoader': 'Grounding Dino Model Loader',
    'GroundingDinoSAM2Segment': 'Grounding Dino SAM2 Segment',
    'GroundingDinoDetector': 'Grounding Dino Detector',
    'InvertMask': 'Invert Mask',
    "IsMaskEmpty": "Is Mask Empty",
    "BboxSam2IndexSelector": "Bbox SAM2 Index Selector",
}
