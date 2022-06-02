package main

import "github.com/pulumi/pulumi/sdk/v3/go/pulumi"

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := zpa.ZPASegmentGroup(ctx, "folder", &zpa.SegmentGroup{
			Description: pulumi.String("A test folder"),
			ParentId:    pulumi.String("<personal folder id>"),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
