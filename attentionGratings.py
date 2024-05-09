#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def hyper_ratio(params, centerContrast, surroundContrast):
    # Returns a hyperbolic ratio of the form Rzero + Rmax * Cc^n / (Cc^n + Cs^n + c50^n)
    # Input params are [Rmax, c50, n, Rzero]
    # Either the center or the surround contrast or both can vary

    Rmax, c50, n, Rzero = params

    Cc = np.atleast_1d(centerContrast)
    Cs = np.atleast_1d(surroundContrast)

    # Force inputs to be between 0 and 1
    
    Cc[np.where(Cc>1)] = 1
    Cc[np.where(Cc<0)] = 0
    Cs[np.where(Cs>1)] = 1
    Cs[np.where(Cs<0)] = 0

    if np.any(Cc < 0) or np.any(Cc > 1):
        raise ValueError("Center contrast must be in the range [0,1]")
    if np.any(Cs < 0) or np.any(Cs > 1):
        raise ValueError("Surround contrast must be in the range [0,1]")
    
    # Ensure Cc and Cs are broadcastable to the same shape : Broadly, are they both vectors of the same shape?
    # Or is one a scalar and the other a vector?
    if Cc.shape != Cs.shape:
        if Cc.size == 1:
            Cc = np.full(Cs.shape, Cc)
        elif Cs.size == 1:
            Cs = np.full(Cc.shape, Cs)
            
        else:
            raise ValueError("Center and surround contrast arrays must be broadcastable to the same shape")
        
    # Validate parameters
    if Rmax <= 0:
        raise ValueError("Rmax must be positive")
    if n <= 0:
        raise ValueError("n must be positive")
    if Rzero < 0:
        raise ValueError("Rzero must be non-negative")
    if c50 <= 0:
        raise ValueError("c50 must be positive")

    # Calculate the hyperbolic ratio
   
    response = Rmax * (Cc**n) / ((Cc)**n+ c50**n+Cs**n)
    return response

def make_circular_grating(image_size, frequency, radius=None, phase_shift=0, orientation=0,contrast=.5):
    """
    Creates a sinusoidal grating of a given size, frequency, phase shift, and orientation.
    The grating can be masked by a circle of a specified radius.

    Args:
        image_size (int): The size of the square image.
        frequency (float): The frequency of the sinusoidal grating.
        radius (int, optional): The radius of the circular mask. If None, no mask is applied.
        phase_shift (float, optional): The phase shift of the sinusoidal grating. Defaults to 0.
        orientation (float, optional): The orientation of the sinusoidal grating in degrees. Defaults to 0.

    Returns:
        numpy.ndarray: A 2D array representing the sinusoidal grating.
    """
    # Create a meshgrid for the x and y coordinates
    x = np.linspace(-image_size // 2, image_size // 2, image_size)
    y = np.linspace(-image_size // 2, image_size // 2, image_size)
    X, Y = np.meshgrid(x, y)

    # Rotate the coordinates based on the orientation
    theta = np.deg2rad(orientation)
    X_rot = X * np.cos(theta) + Y * np.sin(theta)

    # Create the sinusoidal grating
    grating = np.sin(2 * np.pi * frequency * X_rot + phase_shift)

    # Apply the circular mask if a radius is provided
    if radius is not None:
        mask = np.sqrt(X**2 + Y**2) <= radius
        grating *= mask*contrast
    
    return grating*contrast
def make_annulus(image_size, frequency, inner_radius, outer_radius, phase_shift=0, orientation=0,contrast=.5):
    """
    Creates an annulus containing a sinusoidal grating with a specified inner and outer radius, phase shift, and orientation.

    Args:
        image_size (int): The size of the square image.
        frequency (float): The frequency of the sinusoidal grating.
        inner_radius (int): The inner radius of the annulus.
        outer_radius (int): The outer radius of the annulus.
        phase_shift (float, optional): The phase shift of the sinusoidal grating. Defaults to 0.
        orientation (float, optional): The orientation of the sinusoidal grating in degrees. Defaults to 0.

    Returns:
        numpy.ndarray: A 2D array representing the annulus containing the sinusoidal grating.
    """
     # Create a meshgrid for the x and y coordinates
    x = np.linspace(-image_size // 2, image_size // 2, image_size)
    y = np.linspace(-image_size // 2, image_size // 2, image_size)
    X, Y = np.meshgrid(x, y)

    # Rotate the coordinates based on the orientation
    theta = np.deg2rad(orientation)
    X_rot = X * np.cos(theta) + Y * np.sin(theta)

    R = np.sqrt(X**2 + Y**2)
    mask = (R >= inner_radius) & (R <= outer_radius)
    grating = np.sin(2 * np.pi * frequency * X_rot + phase_shift)
    grating *= mask

    return grating*contrast

def compute_overlap_area(r_spotlight, r1, r2=None):
    """
    Computes the overlapping area of a spotlight with a central disk or an annulus.
    r_spotlight: Radius of the spotlight
    r1: Radius of the central disk or inner radius of the annulus
    r2: Outer radius of the annulus (if None, computes for a central disk)
    """
    if r2 is None:  # It's a central disk
        if r_spotlight < r1:
            return np.pi * r_spotlight**2
        else:
            return np.pi * r1**2
    else:  # It's an annulus
        area_outer = np.pi * (min(r_spotlight, r2)**2)
        area_inner = np.pi * (min(r_spotlight, r1)**2)
        return area_outer - area_inner
#%%
# Show an image of 2 gratings inside annuli with a gap between the inner circular grating and the outer annulus
image_size = 512
probeRadius = [100, 100]
attentionalSpotlightRadius = [95,400] # In the first case, the spotlight just covers the centre (the thing that generates the 1F SSVEP)
annulusWidth= 80
probeAnnulusGap=10 
probeContrast = 0.5

frequency = 8
gratings = []

# Create a single figure with multiple subplots
fig, axes = plt.subplots(1, len(probeRadius))  # 1 row, len(probeRadius) columns

for figureIndex, thisProbeRadius in enumerate(probeRadius):
    grating = make_circular_grating(image_size, frequency, thisProbeRadius, probeContrast)
    annulus = make_annulus(image_size, frequency, thisProbeRadius + probeAnnulusGap, thisProbeRadius + annulusWidth)
    
    image = np.zeros((image_size, image_size))
    image[grating != 0] = grating[grating != 0]
    image[annulus != 0] = annulus[annulus != 0]
    
    ax = axes[figureIndex]  # Select the subplot
    ax.imshow(image, cmap='gray')
    
    # Adding a transparent blue circle
    spotlight = Circle((image_size / 2, image_size / 2), attentionalSpotlightRadius[figureIndex], color='blue', alpha=0.2)
    ax.add_patch(spotlight)
    ax.axis('off')  # Hide axes

plt.show()

#%%

# Here we model attention on/off in two stimulus configurations (illustrated above)
# In the first, the attentional spotlight is small relative to the probe the centre of 
# the stimulus. In the second, the attentional spotlight is large relative to the probe 
# and extends into the high contrast surround.
# Attention is modeled as a multiplicative early modulation of the input
# - the qualitatively different types of attentional modulation are 
# due to the different stimulus configurations: Amplifying the surround as well as the
# center changes the gain control of the system.
# See 
# John H. Reynolds, David J. Heeger,
# The Normalization Model of Attention,
# Neuron, Volume 61, Issue 2,2009

# The parameters for the annulus, spotlight etc are defined above. We can use these directly 
# to compute the total amount of contrast available to the centre and suppressive surround
# This is an approximation because a) we don't know the exact dimensions or 
# envelope of the surround RF, nor the overall scale of the response of the two regions.

# Given the parameters above compute what area of a) the central disk and b) the annulus is 
# covered by the attentional spotlight in the two conditions


# Compute areas for each configuration and then compute the CRFs associated with on- and 
# off- attention conditions
standardCRFParams=[1,.05,1,0] # Rmax, c50, q, R0: Note R+H do their modeling with n=1

Ccenter=np.linspace(.01,.7,1000)
Cannulus=.5

# Generate a figure with two subplots across
# The first subplot shows attentional modulation for the small-spotlight case
# The second subplot shows attentional modulation for the large-spotlight case

fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Create a figure with two subplots


for figureIndex, thisProbeRadius in enumerate(probeRadius):
    r_grating = thisProbeRadius
    r_inner = thisProbeRadius + probeAnnulusGap
    r_outer = thisProbeRadius + annulusWidth
    r_spotlight = attentionalSpotlightRadius[figureIndex]

    total_areaGrating=np.pi*r_grating**2
    total_areaAnnulus=np.pi*r_outer**2-np.pi*r_inner**2

    area_gratingOverlap = compute_overlap_area(r_spotlight, r_grating)
    area_annulusOverlap = compute_overlap_area(r_spotlight, r_inner, r_outer)

    proportionSpotlightCenter=area_gratingOverlap/total_areaGrating
    proportionSpotlightAnnulus=area_annulusOverlap/total_areaAnnulus

    print(f"Configuration {figureIndex + 1}:")


    print(f"Proportion center covered by spotlight : {proportionSpotlightCenter:.2f} square units")
    print(f"Proportion annulus covered by spotlight: {proportionSpotlightAnnulus:.2f} square units")
    # Select the subplot (figureIndex) to plot on
    ax = axes[figureIndex]

    for attentionIndex,attentionState in enumerate([1.0,2]):
        # Compute the CRF for this configuration
        totalCenterDrive=Ccenter*attentionState*proportionSpotlightCenter+Ccenter*(1-proportionSpotlightCenter)
        totalAnnulusDrive=Cannulus*attentionState*proportionSpotlightAnnulus+Cannulus*(1-proportionSpotlightAnnulus)
        print(totalAnnulusDrive)

        crf=hyper_ratio(standardCRFParams, totalCenterDrive, totalAnnulusDrive)
        ax.plot(Ccenter,crf)
        
        # Make the x axis log scaled, set labels and titles
        ax.set_xscale('log')
        ax.set_xlabel('Probe contrast')
        ax.set_ylabel('Response')
        ax.set_title(f"Attentional spotlight radius = {r_spotlight:.2f} um")
        ax.legend(['Attn Off','Attn On'])
        ax.grid(True)

# %%
