from build_frames import BuildFrames

new_ds = BuildFrames()

new_ds.get_clip(r"R:\\TemporaryFiles\Desktop\\mariotest.mp4")
new_ds.make_new_dir("mario_test_frames")
new_ds.make_frames()