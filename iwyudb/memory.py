#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
    "HEADER_2_PREFIXES",
]


HEADER_2_SYMBOLS = {
    "memory": [
        "std::addressof",
        "std::align",
        "std::allocate_at_least",
        "std::allocate_shared",
        "std::allocate_shared_for_overwrite",
        "std::allocation_result",
        "std::allocator",
        "std::allocator_arg",
        "std::allocator_arg_t",
        "std::allocator_traits",
        "std::assume_aligned",
        "std::bad_weak_ptr",
        "std::const_pointer_cast",
        "std::construct_at",
        "std::default_delete",
        "std::destroy",
        "std::destroy_at",
        "std::destroy_n",
        "std::dynamic_pointer_cast",
        "std::enable_shared_from_this",
        "std::get_deleter",
        "std::inout_ptr",
        "std::inout_ptr_t",
        "std::make_obj_using_allocator",
        "std::make_shared",
        "std::make_shared_for_overwrite",
        "std::make_unique",
        "std::make_unique_for_overwrite",
        "std::out_ptr",
        "std::out_ptr_t",
        "std::owner_less",
        "std::pointer_traits",
        "std::range::destroy",
        "std::range::destroy_at",
        "std::range::destroy_n",
        "std::range::uninitialized_copy",
        "std::range::uninitialized_copy_n",
        "std::range::uninitialized_fill",
        "std::range::uninitialized_fill_n",
        "std::range::uninitialized_move",
        "std::range::uninitialized_move_n",
        "std::ranges::construct_at",
        "std::ranges::uninitialized_default_construct",
        "std::ranges::uninitialized_value_construct",
        "std::reinterpret_pointer_cast",
        "std::shared_ptr",
        "std::static_pointer_cast",
        "std::to_address",
        "std::uninitialized_construct_using_allocator",
        "std::uninitialized_copy",
        "std::uninitialized_copy_n",
        "std::uninitialized_default_construct",
        "std::uninitialized_default_construct_n",
        "std::uninitialized_fill",
        "std::uninitialized_fill_n",
        "std::uninitialized_move",
        "std::uninitialized_move_n",
        "std::uninitialized_value_construct",
        "std::unique_ptr",
        "std::uses_allocator",
        "std::uses_allocator_construction_args",
        "std::uses_allocator_v",
        "std::weak_ptr",
    ],
    "new": [
        "std::align_val_t",
        "std::bad_alloc",
        "std::bad_array_new_length",
        "std::destroying_delete",
        "std::destroying_delete_t",
        "std::get_new_handler",
        "std::hardware_constructive_interference_size",
        "std::hardware_destructive_interference_size",
        "std::launder",
        "std::new_handler",
        "std::nothrow",
        "std::nothrow_t",
        "std::set_new_handler",
    ],
}


HEADER_2_PREFIXES = {
    "memory": [
        "std::allocator_arg_t",
        "std::bad_weak_ptr",
    ],
    "new": [
        "std::align_val_t",
        "std::bad_alloc",
        "std::bad_array_new_length",
        "std::destroying_delete_t",
        "std::nothrow_t",
    ],
}