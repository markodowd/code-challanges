struct Ship {
    draft: u32,
    crew: u32,
}

impl Ship {
    fn is_worth_it(self) -> bool {
        if (self.draft as f32) - ((self.crew as f32) * 1.5) > 20.0 {
            return true;
        }

        false
    }
}
