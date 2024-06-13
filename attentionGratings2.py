import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def hyper_ratio(params, centerContrast, surroundContrast):
    Rmax, c50, n, Rzero = params
    Cc = np.clip(centerContrast, 0, 1)  # Ensure center contrast is in the range [0,1]
    Cs = np.clip(surroundContrast, 0, 1)  # Ensure surround contrast is in the range [0,1]
    # Validate parameters
    if any(p <= 0 for p in [Rmax, c50, n]) or Rzero < 0:
        raise ValueError("Invalid parameters: Rmax, c50, and n must be positive, Rzero must be non-negative")

    # Calculate the response based on the input parameters
    response = Rzero + Rmax * Cc**n / (Cc**n + Cs**n + c50**n)
    return response

def make_grating(image_size, frequency, radius=None, phase_shift=0, orientation=0, contrast=.5, is_annulus=False, inner_radius=None):
    x = np.linspace(-image_size / 2, image_size / 2, image_size)  # Generate linear space for x-axis
    y = np.linspace(-image_size / 2, image_size / 2, image_size)  # Generate linear space for y-axis
    X, Y = np.meshgrid(x, y)  # Create a 2D meshgrid from x and y values

    theta = np.radians(orientation)  # Convert orientation from degrees to radians
    X_rot = X * np.cos(theta) + Y * np.sin(theta)  # Rotate the grid
    grating = np.sin(2 * np.pi * frequency * X_rot + phase_shift)  # Generate sinusoidal grating

    if radius is not None:
        if is_annulus and inner_radius is not None:
            R = np.sqrt(X**2 + Y**2)  # Calculate radial coordinates
            mask = (R >= inner_radius) & (R <= radius)  # Create a masked area between the inner and outer radius
        else:
            mask = np.sqrt(X**2 + Y**2) <= radius  # Create a circular mask of the specified radius
        grating *= mask  # Apply the mask to the grating

    return grating * contrast  # Scale the grating by contrast and return it
def compute_overlap_area(r_spotlight, r1, r2=None):
    if r2 is None:
        return np.pi * r1**2 if r_spotlight >= r1 else np.pi * r_spotlight**2  # Return area of full circle if within spotlight radius
    area_outer = np.pi * min(r_spotlight, r2)**2  # Compute area for the outer radius
    area_inner = np.pi * min(r_spotlight, r1)**2 if r_spotlight > r1 else 0  # Compute area for the inner radius if inside the spotlight
    return area_outer - area_inner  # Return the overlap area

image_size = 512  # Define the size of the image
probe_radius = [100, 100]  # Radius for probes
spotlight_radius = [95, 400]  # Spotlight radii for use in visualization
annulus_width = 80  # Width for annulus grating
gap = 10  # Space between inner radius of annulus and the probe
frequency = 8  # Frequency of the grating
contrast = 0.5  # Contrast of the grating
# Display setup
fig, axes = plt.subplots(1, len(probe_radius), figsize=(10, 5))  # Create subplot with specific size

for idx, radius in enumerate(probe_radius):
    grating = make_grating(image_size, frequency, radius, contrast=contrast)  # Create circular grating
    annulus = make_grating(image_size, frequency, radius + annulus_width, inner_radius=radius + gap, contrast=contrast, is_annulus=True)  # Create annular grating
    
    combined_image = grating + annulus  # Combine the two gratings
    axes[idx].imshow(combined_image, cmap='gray')  # Display the combined image in grayscale
    circle = Circle((image_size / 2, image_size / 2), spotlight_radius[idx], color='blue', alpha=0.2)  # Create a circle patch for spotlight
    axes[idx].add_patch(circle)  # Add the spotlight to the subplot
    axes[idx].axis('off')  # Turn off axis
plt.show()  # Display the plot
