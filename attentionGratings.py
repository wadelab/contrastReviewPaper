
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def hyper_ratio(params, centerContrast, surroundContrast):
    Rmax, c50, n, Rzero = params
    Cc = np.clip(centerContrast, 0, 1)
    Cs = np.clip(surroundContrast, 0, 1)

    # Validate parameters
    if any(p <= 0 for p in [Rmax, c50, n]) or Rzero < 0:
        raise ValueError("Invalid parameters: Rmax, c50, and n must be positive, Rzero must be non-negative")

    response = Rzero + Rmax * Cc**n / (Cc**n + Cs**n + c50**n)
    return response

def make_grating(image_size, frequency, radius=None, phase_shift=0, orientation=0, contrast=.5, is_annulus=False, inner_radius=None):
    x = np.linspace(-image_size / 2, image_size / 2, image_size)
    y = np.linspace(-image_size / 2, image_size / 2, image_size)
    X, Y = np.meshgrid(x, y)

    theta = np.radians(orientation)
    X_rot = X * np.cos(theta) + Y * np.sin(theta)
    grating = np.sin(2 * np.pi * frequency * X_rot + phase_shift)

    if radius is not None:
        if is_annulus and inner_radius is not None:
            R = np.sqrt(X**2 + Y**2)
            mask = (R >= inner_radius) & (R <= radius)
        else:
            mask = np.sqrt(X**2 + Y**2) <= radius
        grating *= mask
    
    return grating * contrast

def compute_overlap_area(r_spotlight, r1, r2=None):
    if r2 is None:
        return np.pi * r1**2 if r_spotlight >= r1 else np.pi * r_spotlight**2
    area_outer = np.pi * min(r_spotlight, r2)**2
    area_inner = np.pi * min(r_spotlight, r1)**2 if r_spotlight > r1 else 0
    return area_outer - area_inner



def main():
    # Simulation parameters
    image_size = 512
    frequency = 8
    contrast = 0.5
    probe_radius = [100, 200]
    annulus_width = 50
    gap = 10
    spotlight_radius = [95, 400]
    attentionState = 0.7  # Example modulation by attention state

    # Contrast setup
    contrasts = np.logspace(-2, -.01, 100)
    responses = []

    # Plot preparation
    fig, axes = plt.subplots(2, len(probe_radius), figsize=(15, 10))  # Adjust subplots to have two rows

    for idx, radius in enumerate(probe_radius):
        # Create image, grating, and annulus
        grating = make_grating(image_size, frequency, radius, contrast=contrast)
        annulus = make_grating(image_size, frequency, radius + annulus_width, inner_radius=radius + gap, contrast=contrast, is_annulus=True)
        combined_image = grating + annulus

        # Display grating and annulus
        axes[0, idx].imshow(combined_image, cmap='gray')
        circle = Circle((image_size / 2, image_size / 2), spotlight_radius[idx], color='blue', alpha=0.2)
        axes[0, idx].add_patch(circle)
        axes[0, idx].axis('off')

        # Compute and plot response function depending on the spotlight
        response = []  # Storage for calculated responses
        for this_contrast in contrasts:
            # Recreate grating and annulus with different contrasts dynamically
            grating = make_grating(image_size, frequency, radius, contrast=this_contrast)
            annulus = make_grating(image_size, frequency, radius + annulus_width, inner_radius=radius + gap, contrast=this_contrast, is_annulus=True)

            # Example computation for response (will need actual calculations related to attentionState, etc.)
            propCenter = compute_overlap_area(spotlight_radius[idx], radius) / (np.pi * radius**2)
            propAnnulus = (compute_overlap_area(spotlight_radius[idx], radius + annulus_width, radius + gap) / (np.pi * ((radius + annulus_width)**2 - (radius + gap)**2)))

            hyperRatio = hyper_ratio([1, 0.05, 2, 0], this_contrast*propCenter, this_contrast*propAnnulus)
        

            response.append(hyperRatio)

        axes[1, idx].plot(contrasts, response)
        # Set x axis as log scale
        axes[1, idx].set_xscale('log')
        axes[1, idx].set_xlabel('Contrast')
        axes[1, idx].set_ylabel('Response')
        axes[1, idx].set_title(f'Radius: {radius} with Spotlight: {spotlight_radius[idx]}')
        axes[1, idx].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()