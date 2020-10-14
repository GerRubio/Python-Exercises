# Example of Heritage.

# First class.
class File:
    def __init__(self, path):
        self.path = path
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    def show(self):
        print(self.contents)

    def rename(self, new_path):
        self.path = new_path
    
    def remove(self):
        self.path = None
        self.contents.clear()
    
    def size(self):
        sizes = []

        for iterator in self.contents:
            sizes.append(len(iterator))
        
        return sum(sizes)
    
    def info(self):
        return f'''
        Path: {self.path} 
        Size: {self.size()} MB.
        '''

# Second class.
class MediaFile(File):
    def __init__(self, path, codec, geoloc, duration):
        super().__init__(path)

        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration
    
    def info(self):
        file_info = super().info()
        
        return f'''
        {file_info}
        Codec: {self.codec}.
        Geolocalization: {self.geoloc}
        Duration: {self.duration} seconds.
        '''

# Third class.
class VideoFile(MediaFile):
    def __init__(self, path, codec, geoloc, duration, dimensions):
        super().__init__(path, codec, geoloc, duration)

        self.dimensions = dimensions

    def info(self):
        media_info = super().info()
            
        return f'''
        Media info: {media_info}
        Dimensions: {self.dimensions}
        '''

# Object.
video_file = VideoFile(
    '/home/python/vanrossum.mp4', 
    'H264', 
    (23.5454, 31.4343), 
    487, 
    (1920, 1080)
)

video_file.add_content('Hello')
video_file.add_content('World.')

print(video_file.info())