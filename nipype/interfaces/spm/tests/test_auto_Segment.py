# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.preprocess import Segment
def test_Segment_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    paths=dict(),
    clean_masks=dict(field='output.cleanup',
    ),
    bias_fwhm=dict(field='opts.biasfwhm',
    ),
    mask_image=dict(field='opts.msk',
    ),
    bias_regularization=dict(field='opts.biasreg',
    ),
    warp_frequency_cutoff=dict(field='opts.warpco',
    ),
    affine_regularization=dict(field='opts.regtype',
    ),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    warping_regularization=dict(field='opts.warpreg',
    ),
    use_mcr=dict(),
    gm_output_type=dict(field='output.GM',
    ),
    tissue_prob_maps=dict(field='opts.tpm',
    ),
    sampling_distance=dict(field='opts.samp',
    ),
    matlab_cmd=dict(),
    gaussians_per_class=dict(field='opts.ngaus',
    ),
    mfile=dict(usedefault=True,
    ),
    save_bias_corrected=dict(field='output.biascor',
    ),
    data=dict(copyfile=False,
    mandatory=True,
    field='data',
    ),
    wm_output_type=dict(field='output.WM',
    ),
    csf_output_type=dict(field='output.CSF',
    ),
    )
    inputs = Segment.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Segment_outputs():
    output_map = dict(bias_corrected_image=dict(),
    native_csf_image=dict(),
    normalized_wm_image=dict(),
    modulated_wm_image=dict(),
    modulated_input_image=dict(new_name='bias_corrected_image',
    deprecated='0.10',
    ),
    native_wm_image=dict(),
    inverse_transformation_mat=dict(),
    transformation_mat=dict(),
    normalized_csf_image=dict(),
    modulated_gm_image=dict(),
    modulated_csf_image=dict(),
    native_gm_image=dict(),
    normalized_gm_image=dict(),
    )
    outputs = Segment.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value