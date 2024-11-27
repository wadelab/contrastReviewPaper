Comments to the Author
General Comments

Wade and Baker have written a very approachable and well-motivated review of the use of VEP measurements of visual contrast. The authors rightly focus on the importance of measuring contrast responses under a wide range of conditions, highlighting the ways in which human evoked responses can be made in informative in diverse contexts. The review should thus be of broad interest.

There are points where the review is overly broad and others that could use more detail. These are described below.

A central part of the review is the role of computational models and normalization models, in particular. The use of the normalization framework for describing the VEP contrast response function (CRF) has been fruitful in terms of mechanistic interpretation and linking to other measurements, such as single-unit physiology and fMRI.  This modeling approach assumes that the CRF reflects the activity of a more or less unitary population, and that the population response resembles that of the underlying individual neurons that make up the population.  

There are two edge-cases in the literature that suggest a more nuanced approach will be needed. It would be useful to be clearer on the assumptions of the modeling approach and what the significance is for interpretation of cases where the assumptions don’t hold.

Two-limbed contrast response functions. Campbell and Maffei (J. Physiol,1970) in the earliest measurements of the VEP contrast response function reported that it sometimes had two “limbs” – one at low contrast and a second one with a steeper slope at higher contrasts.  Two-limbed contrast response functions have also been found by Nakayama and Mackeben (Vision Res,1982) in macaque with electrodes on the dura, by Apkarian and Tyler (Vision Res, 1985),  Norcia et al., (Vision Res,1989) and Souza et al., (IOVS, 2007), to name a few.  As noted, the sigmoidal model assumes that the population response is unitary, but the two-limbed functions suggest that it is a mixture of populations. The two limbs may not be apparent when the function is sampled with only a few points over a wide range of contrast.

Harmonics with different CRFs.  Bobak et al., (IOVS, 1986), found that the first harmonic (1f) and second harmonic (2f) of the pattern onset/offset SSVEP had different thresholds but similar slopes once above threshold. Norcia et al., (TVST, 2024) found different thresholds and slope for 1f and 2f responses driven by contrast modulated dynamic noise. This again suggests the presence of multiple underlying populations.  The behavior also raises the question of whether to pool harmonics when estimating the response function. This was alluded to in the simulation, but could be expanded on.

The lack of dynamics in the normalization model, as presented should be discussed, the brief mention of Tsai et al. aside. The authors may wish to cite another framework that explicitly models dynamics (e.g. amplitude and phase) in the context of the contrast response function (Zemon and Gordon, Vision Res, 2006) .  


Specific comments

Adaptation effects.  Adapted contrast response functions have been measured by Nelson et al., (EEG Journal, 1984) by comparing CRFs measured by sweeping contrast from low to high vs high to low. They found that responses at low contrast were smaller in the “down” sweeps and attributed it to differences in prior adaptation.  Other studies also measured adaptation effects on the CRF Heinrich and Bach, (IOVS, 2001), Ross and Speed (1991, Proc Roy Soc). And the hard-to-find Bach, Greenlee and Buhler (Clin Vis Sci, 1996) paper that modeled the effect within a contrast gain control framework.
Gain control development.  Morrone and Burr (Nature, 1986) used frequency tagging to measure orientation dependence of masking in infants and adults, as did Candy et al. The difference in the two studies is that in adults Morrone and Burr found response gain for cross-oriented maskers but Candy et al found contrast gain.   Skoczenski and Norcia used a high contrast 30 Hz dynamic 2D noise masker and variable contrast reversing gratings. They found masking consistent with a contrast gain effect.

Page 5 bottom. The reciprocal effect of test and masker was first shown by Regan and Regan  (1988; cited)  for flicker modulation depth and then for gratings by Brown et al., (IOVS,  1999 for dichoptic masking) and  then  by candy et al., (J. Neurosci, 2001) along with Busse et al. (Neuron, 2009) as cited. It’s good to have cited Regan and Regan paper that introduced the notion of fingerprints in the spectrum being tied to the nature of the non-linearity. Maybe expand their “fingerprint” approacg a little more.

Figure 4. Oversaturation occurs because the denominator overtakes the numerator at high contrast as it has two terms in it, not the single term in the numerator. Would be worth showing total power not saturating. Is this a general effect?

Equation 3 is a special case where the neurons in the numerator are so selective that they don’t “see” the masker except by being influenced indirectly by the gain pool.  Putting the test and mask in the numerator and summing them before exponentiating yields robust IM. Weights can be used to reflect the neurons preference for the test vs the mask.  Does equation 3 produce IM?

Page 7 Mckeefry et al., (Vis Neuro, 1996) is a good reference for linking harmonics of on/off to transient sustained responses.

Page 8 figure 5. The extrapolation to zero amplitude method should be attributed to Cambell and Maffei (J Physiol) 1970). Campbell and Kulikowski (J Physiol, 1972) made a detailed comparison to psychophysics.

Figure 5 is an oversimplification. As it doesn’t take into account how the additive noise mixes with the internal VEP response.  This was modeled in Norcia et al., (Vision Res, 1989). The additive noise adds a bias to the measurement, especially if the slope of the response function is shallow. The authors should try to connect the linear regression approach for threshold measurement to the sigmoidal non-linearity, as they are different models of the CRF. In practice the difference at the low contrast end is probably too small to matter and the saturation region is excluded.

Page 9. The sweep method was first developed by David Regan (Vision Res, 1973) for use in objective refraction.

Page 9 “This approach” seems to refer to the sweep VEP, not the method of measuring at multiple contrast levels over a series of trials which was used in the Atkinson/Braddick papers. The sweep method refers to the approach of incrementing or decrementing the stimulus value within a single trial and then averaging the sweeps to get the response function.  Regan argued that this was a better way of estimating response functions because amplitude variations over a session are distributed over the whole response function shifting it up or down instead of distorting its shape (Regan (Vison Res, 1975, color coding).

Page 9 …chromatic and chromatic contrast as well as stereoscopic depth perception develops earlier than had been supposed previously based on behavioural readouts (Dobson et al., 1978; Norcia & Tyler, 1985b) with both chromatic and achromatic contrast detection reaching near-adult levels by around six months. Needs references for chromatic sensitivity and disparity sensitivity.

The DeVries Khoe and Spekreijse comparison between VEP and psychophysics was done above age 4 years and for acuity not for contrast sensitivity. The large discrepancies between VEP and FPL are in infancy for contrast sensitivity, as well as for acuity.  In the realm of contrast sensitivity, the differences are very large, up to a factor of 50.  Compare Norcia et al., 1990 Vision Res measurement to any behavioral data. Suggest making this comparison more quantitative.

The authors may wish to cite Norcia et al., (NeuroReport, 2000) for an early measurement of suppression in amblyopia using measurements of the contrast response function in each eye in the presence of a high contrast dichoptic masker in the other.  This study showed that amblyopic observers retain suppressive binocular interactions despite severely reduced stereopsis. The dominant eye exerted a greater suppressive effect on the non-dominant eye, suggesting that it maintains a relatively greater number, or more effective, inhibitory contacts with cortical cells.  Also may wish to cite recent work by Hou and colleagues using a similar approach, including application of normalization models.

Schade (JOSA, 1956) was the first to measure the contrast sensitivity function of the human visual system as noted by Campbell and Robson (J. Physiol, 1968). Campbell and Green (1965, cited) credit Schade for how to make sinewave gratings on an oscilloscope but not for having made the first measurement.

Villadaite, Norcia et al., (cited) did not find spatial frequency specific effects at 8 cpd as in Pei et al,. (cited). So it’s not really a replication of that study, but more of an extension to a measurement of CRF instead of SF tuning.

Page 12, better to state whether attention effects were consistent with response gain or contrast gain to make the result more concrete for the reader.

Discussion of time varying response paragraph on page 12 is not that relevant to contrast response function measurement, nor is the BCI section.  These applications of SSVEP and could be deleted or the relationship to contrast response function made clearer.

Page, 14. It’s not clear from the text how one would study feedback with the SSVEP, please elaborate.

In the last section, it would be worth mentioning that in order to “identify” a non-linear system, one needs multiple inputs. If the system is 2nd order, a minimum of two inputs is needed. If the system non-linearity is higher order than that, then more simultaneous inputs are needed (see Boyd, Tang and Chua 1983, IEEE Trans Circuits and Systems  and  Chua and Liao, 1991, Int. J. Circuit Theory and Applications).

.

