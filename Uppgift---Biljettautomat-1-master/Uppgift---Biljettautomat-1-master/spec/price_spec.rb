require 'rspec'
require_relative '../lib/ticket'


describe 'ticket_price' do

  before do
    @child_price = 10
    @adult_price = 20
    @senior_price = 15
  end

  it 'should take an age as an argument' do
    expect { ticket_price() }.to raise_error ArgumentError
    expect { ticket_price(13) }.not_to raise_error
  end

  it 'should return the correct price for children' do
    (0..17).each do |age|
      expect( ticket_price(age) ).to eq @child_price
    end
  end

  it 'should return the correct price for adults' do
    (18..64).each do |age|
      expect( ticket_price(age) ).to eq @adult_price
    end
  end

  it 'should return the correct price for seniors' do
    (65..120).each do |age|
      expect( ticket_price(age) ).to eq @senior_price
    end
  end

end
