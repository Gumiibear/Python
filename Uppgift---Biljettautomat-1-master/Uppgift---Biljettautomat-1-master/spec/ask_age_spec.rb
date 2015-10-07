require 'rspec'
require_relative '../lib/ticket'

describe 'ask_age' do

  before do
    $stdout = StringIO.new
  end

  after(:all) do
    $stdout = STDOUT
  end

  it 'should ask the user to enter their age' do
    ask_age
    expect( $stdout.string ).to eq "Enter your age\n"
  end

  it 'should let the user enter their age' do
    expect(self).to receive(:gets)
    ask_age
  end

  it 'should return the input age as a Fixnum' do
    allow(self).to receive(:gets) { "17\n" }
    expect( ask_age ).to eq 17

    allow(self).to receive(:gets) { "65\n" }
    expect( ask_age ).to eq 65

    allow(self).to receive(:gets) { "Grillkorv" }
    expect( ask_age ).to eq 0
  end

end
