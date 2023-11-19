#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
    "HEADER_2_PREFIXES",
]


HEADER_2_SYMBOLS = {
    "type_traits": [
        "std::add_const",
        "std::add_const_t",
        "std::add_cv",
        "std::add_cv_t",
        "std::add_lvalue_reference",
        "std::add_lvalue_reference_t",
        "std::add_pointer",
        "std::add_pointer_t",
        "std::add_rvalue_reference",
        "std::add_rvalue_reference_t",
        "std::add_volatile",
        "std::add_volatile_t",
        "std::aligned_storage",
        "std::aligned_storage_t",
        "std::aligned_union",
        "std::aligned_union_t",
        "std::alignment_of",
        "std::alignment_of_v",
        "std::basic_common_reference",
        "std::bool_constant",
        "std::common_reference",
        "std::common_reference_t",
        "std::common_type",
        "std::common_type_t",
        "std::conditional",
        "std::conditional_t",
        "std::conjunction",
        "std::conjunction_v",
        "std::decay",
        "std::decay_t",
        "std::disjunction",
        "std::disjunction_v",
        "std::enable_if",
        "std::enable_if_t",
        "std::extent",
        "std::extent_v",
        "std::false_type",
        "std::has_unique_object_representations",
        "std::has_unique_object_representations_v",
        "std::has_virtual_destructor",
        "std::has_virtual_destructor_v",
        "std::integral_constant",
        "std::invoke_result",
        "std::invoke_result_t",
        "std::is_abstract",
        "std::is_abstract_v",
        "std::is_aggregate",
        "std::is_aggregate_v",
        "std::is_arithmetic",
        "std::is_arithmetic_v",
        "std::is_array",
        "std::is_array_v",
        "std::is_assignable",
        "std::is_assignable_v",
        "std::is_base_of",
        "std::is_base_of_v",
        "std::is_bounded_array",
        "std::is_bounded_array_v",
        "std::is_class",
        "std::is_class_v",
        "std::is_compound",
        "std::is_compound_v",
        "std::is_const",
        "std::is_const_v",
        "std::is_constant_evaluated",
        "std::is_constructible",
        "std::is_constructible_v",
        "std::is_convertible",
        "std::is_convertible_v",
        "std::is_copy_assignable",
        "std::is_copy_assignable_v",
        "std::is_copy_constructible",
        "std::is_copy_constructible_v",
        "std::is_corresponding_member",
        "std::is_default_constructible",
        "std::is_default_constructible_v",
        "std::is_destructible",
        "std::is_destructible_v",
        "std::is_empty",
        "std::is_empty_v",
        "std::is_enum",
        "std::is_enum_v",
        "std::is_final",
        "std::is_final_v",
        "std::is_floating_point",
        "std::is_floating_point_v",
        "std::is_function",
        "std::is_function_v",
        "std::is_fundamental",
        "std::is_fundamental_v",
        "std::is_integral",
        "std::is_integral_v",
        "std::is_invocable",
        "std::is_invocable_r",
        "std::is_invocable_r_v",
        "std::is_invocable_v",
        "std::is_layout_compatible",
        "std::is_layout_compatible_v",
        "std::is_literal_type",
        "std::is_literal_type_v",
        "std::is_lvalue_reference",
        "std::is_lvalue_reference_v",
        "std::is_member_function_pointer",
        "std::is_member_function_pointer_v",
        "std::is_member_object_pointer",
        "std::is_member_object_pointer_v",
        "std::is_member_pointer",
        "std::is_member_pointer_v",
        "std::is_move_assignable",
        "std::is_move_assignable_v",
        "std::is_move_constructible",
        "std::is_move_constructible_v",
        "std::is_nothrow_assignable",
        "std::is_nothrow_assignable_v",
        "std::is_nothrow_constructible",
        "std::is_nothrow_constructible_v",
        "std::is_nothrow_convertible",
        "std::is_nothrow_convertible_v",
        "std::is_nothrow_copy_assignable",
        "std::is_nothrow_copy_assignable_v",
        "std::is_nothrow_copy_constructible",
        "std::is_nothrow_copy_constructible_v",
        "std::is_nothrow_default_constructible",
        "std::is_nothrow_default_constructible_v",
        "std::is_nothrow_destructible",
        "std::is_nothrow_destructible_v",
        "std::is_nothrow_invocable",
        "std::is_nothrow_invocable_r",
        "std::is_nothrow_invocable_r_v",
        "std::is_nothrow_invocable_v",
        "std::is_nothrow_move_assignable",
        "std::is_nothrow_move_assignable_v",
        "std::is_nothrow_move_constructible",
        "std::is_nothrow_move_constructible_v",
        "std::is_nothrow_swappable",
        "std::is_nothrow_swappable_v",
        "std::is_nothrow_swappable_with",
        "std::is_nothrow_swappable_with_v",
        "std::is_null_pointer",
        "std::is_null_pointer_v",
        "std::is_object",
        "std::is_object_v",
        "std::is_pod",
        "std::is_pod_v",
        "std::is_pointer",
        "std::is_pointer_interconvertible_base_of",
        "std::is_pointer_interconvertible_base_of_v",
        "std::is_pointer_interconvertible_with_class",
        "std::is_pointer_v",
        "std::is_polymorphic",
        "std::is_polymorphic_v",
        "std::is_reference",
        "std::is_reference_v",
        "std::is_rvalue_reference",
        "std::is_rvalue_reference_v",
        "std::is_same",
        "std::is_same_v",
        "std::is_scalar",
        "std::is_scalar_v",
        "std::is_scoped_enum",
        "std::is_scoped_enum_v",
        "std::is_signed",
        "std::is_signed_v",
        "std::is_standard_layout",
        "std::is_standard_layout_v",
        "std::is_swappable",
        "std::is_swappable_v",
        "std::is_swappable_with",
        "std::is_swappable_with_v",
        "std::is_trivial",
        "std::is_trivial_v",
        "std::is_trivially_assignable",
        "std::is_trivially_assignable_v",
        "std::is_trivially_constructible",
        "std::is_trivially_constructible_v",
        "std::is_trivially_copy_assignable",
        "std::is_trivially_copy_assignable_v",
        "std::is_trivially_copy_constructible",
        "std::is_trivially_copy_constructible_v",
        "std::is_trivially_copyable",
        "std::is_trivially_copyable_v",
        "std::is_trivially_default_constructible",
        "std::is_trivially_default_constructible_v",
        "std::is_trivially_destructible",
        "std::is_trivially_destructible_v",
        "std::is_trivially_move_assignable",
        "std::is_trivially_move_assignable_v",
        "std::is_trivially_move_constructible",
        "std::is_trivially_move_constructible_v",
        "std::is_unbounded_array",
        "std::is_unbounded_array_v",
        "std::is_union",
        "std::is_union_v",
        "std::is_unsigned",
        "std::is_unsigned_v",
        "std::is_void",
        "std::is_void_v",
        "std::is_volatile",
        "std::is_volatile_v",
        "std::make_signed",
        "std::make_signed_t",
        "std::make_unsigned",
        "std::make_unsigned_t",
        "std::negation",
        "std::negation_v",
        "std::rank",
        "std::rank_v",
        "std::reference_constructs_from_temporary",
        "std::reference_constructs_from_temporary_v",
        "std::reference_converts_from_temporary",
        "std::reference_converts_from_temporary_v",
        "std::remove_all_extents",
        "std::remove_all_extents_t",
        "std::remove_const",
        "std::remove_const_t",
        "std::remove_cv",
        "std::remove_cv_t",
        "std::remove_cvref",
        "std::remove_cvref_t",
        "std::remove_extent",
        "std::remove_extent_t",
        "std::remove_pointer",
        "std::remove_pointer_t",
        "std::remove_reference",
        "std::remove_reference_t",
        "std::remove_volatile",
        "std::remove_volatile_t",
        "std::true_type",
        "std::type_identity",
        "std::type_identity_t",
        "std::underlying_type",
        "std::underlying_type_t",
        "std::unwrap_ref_decay",
        "std::unwrap_ref_decay_t",
        "std::unwrap_reference",
        "std::unwrap_reference_t",
        "std::void_t",
    ],
}


HEADER_2_PREFIXES = {
    "type_traits": [
        "std::false_type",
        "std::true_type",
    ],
}
